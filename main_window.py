import serial
from serial.tools import list_ports
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QVBoxLayout, QMessageBox
from PyQt6.QtCore import pyqtSlot, QThread, pyqtSignal
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mainWindow import Ui_MainWindow

class SerialThread(QThread):
    data_received = pyqtSignal(str)
    error_occurred = pyqtSignal(str)
    
    def __init__(self, port):
        super().__init__()
        self.port = port
        self.ser = None
        self._running = True

    def run(self):
        try:
            self.ser = serial.Serial(self.port, 9600, timeout=0.5)
            while self._running:
                data = self.ser.readline().decode("ASCII").strip()
                if data:
                    self.data_received.emit(data)
        except Exception as e:
            self.error_occurred.emit(str(e))
        finally:
            if self.ser and self.ser.is_open:
                self.ser.close()
    
    def stop(self):
        self._running = False
        self.wait()

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        self.ax = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)
        self.ax.set_title('Time-Data Plot')
        self.ax.set_xlabel('Time/s')
        self.ax.set_ylabel('F/g')
        self.line, = self.ax.plot([], [], 'r-')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.data = []
        self.time_values = []
        self.data_values = []
        self.serial_thread = None
        
        self.ui.pushButton_start.setEnabled(True)
        self.ui.pushButton_stop.setEnabled(False)
        self.ui.pushButton_save.setEnabled(False)
        self.ui.pushButton_clear.setEnabled(False)
        self.ui.com_show.setReadOnly(True)
        self.ui.com_show.setText("No COM port found.")
        
        # 初始化 Matplotlib 画布
        self.canvas = MplCanvas(self.ui.groupBox_figure)
        
        # 检查 groupBox_figure 是否已经有布局，如果没有则创建一个新的
        layout = self.ui.groupBox_figure.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.groupBox_figure)
        layout.addWidget(self.canvas)

        self.ui.pushButton_start.clicked.connect(self.start_reading)
        self.ui.pushButton_stop.clicked.connect(self.stop_reading)
        self.ui.pushButton_save.clicked.connect(self.save_data)
        self.ui.pushButton_clear.clicked.connect(self.clear_data)
        
    @pyqtSlot()
    def start_reading(self):
        self.ui.textBrowser_info.append("Starting reading...")
        ports = list_ports.comports()
        for port in ports:
            self.ui.com_show.setText(port.device)
            self.serial_thread = SerialThread(port.device)
            self.serial_thread.data_received.connect(self.update_data)
            self.serial_thread.error_occurred.connect(self.handle_error)
            self.serial_thread.start()
            self.ui.textBrowser_info.append(f"Serial port {port.device} opened.")
            break
        
        if not self.serial_thread or not self.serial_thread.isRunning():
            self.ui.textBrowser_info.append("No COM port found.")
            return

        self.ui.pushButton_start.setEnabled(False)
        self.ui.pushButton_stop.setEnabled(True)
        self.ui.pushButton_save.setEnabled(False)
        self.ui.pushButton_clear.setEnabled(False)

    @pyqtSlot(str)
    def update_data(self, data):
        self.data.append(data)
        self.ui.textBrowser_info.append(f"{data}")
        # 更新数据
        try:
            time, value = data.split(',')
            # 计算数据 F =  value * 30 / 2^20 * 0.0012 * 4.95; t = time * 10^-2
            F = float(value) * 30 / 2**20 * 0.0012 * 4.95
            t = float(time) * 10**(-2)
            self.data_values.append(F)
            self.time_values.append(t)
            
            # 更新绘图
            self.canvas.line.set_data(self.time_values, self.data_values)
            self.canvas.ax.relim()  # 重新调整坐标轴范围
            self.canvas.ax.autoscale_view()
            self.canvas.draw()
        except ValueError:
            self.ui.textBrowser_info.append(f"Invalid data format: {data}")
    
    @pyqtSlot(str)
    def handle_error(self, error_message):
        self.ui.textBrowser_info.append(f"Error: {error_message}")
        self.stop_reading()

    def stop_reading(self):
        self.ui.textBrowser_info.append("Stopping reading...")
        if self.serial_thread:
            self.serial_thread.stop()
            self.serial_thread = None
        self.ui.textBrowser_info.append("Reading stopped.")
        self.ui.pushButton_start.setEnabled(True)
        self.ui.pushButton_stop.setEnabled(False)
        self.ui.pushButton_save.setEnabled(True)
        self.ui.pushButton_clear.setEnabled(True)

    def save_data(self):
        self.ui.textBrowser_info.append("Saving data...")
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "CSV Files (*.csv)")
        if file_name:
            with open(file_name, "w") as f:
                f.write("Time,Data\n")
                for data in self.data:
                    try:
                        time, value = data.split(',')
                        # 计算数据 F = value * 30 / 2^20 * 0.0012 * 4.95; t = time * 10^-2
                        F = float(value) * 30 / 2**20 * 0.0012 * 4.95
                        t = float(time) * 10**-2
                        f.write(f"{t},{F}\n")
                    except ValueError:
                        self.ui.textBrowser_info.append(f"Invalid data format: {data}")
            self.ui.textBrowser_info.append(f"Data saved to {file_name}.")


    def clear_data(self):
        # 弹出确认对话框
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Confirmation")
        msg_box.setText("Are you sure to clear all data?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        if msg_box.exec() == QMessageBox.StandardButton.Yes:
            self.clear_data_confirmed()


    def clear_data_confirmed(self):
        self.ui.textBrowser_info.append("Clearing data...")
        self.data.clear()
        self.time_values.clear()
        self.data_values.clear()
        self.canvas.ax.clear()
        self.canvas.ax.set_title('F-t Plot')
        self.canvas.ax.set_xlabel('Time/s')
        self.canvas.ax.set_ylabel('F/g')
        self.canvas.line, = self.canvas.ax.plot([], [], 'r-')
        self.canvas.draw()
        self.ui.textBrowser_info.clear()
        self.ui.textBrowser_info.append("Data cleared.")

