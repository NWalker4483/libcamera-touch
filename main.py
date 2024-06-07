from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QFile, QIODevice, QTextStream, QTimer, Qt
import sys
from camera_manager import CameraManager
from sidebar_menu import create_sidebar_menu
import cv2
import os
from elements import RoundButton
from display_page import DisplayPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Camera Settings")
        self.setGeometry(100, 100, 800, 600)
        self.showFullScreen()
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.webcam_label = QLabel(self.central_widget)
        self.layout.addWidget(self.webcam_label)
        self.camera_manager = CameraManager()
        self.sidebar = create_sidebar_menu(self, self.change_resolution, self.quit_application, self.camera_manager)
        self.sidebar.hide()

        self.capture_button = RoundButton(self.central_widget)
        self.capture_button.setGeometry(self.width() - 120, self.height() - 220, 100, 100)
        self.capture_button.clicked.connect(self.capture_image)

        self.display_button = QPushButton("Display", self.central_widget)
        self.display_button.setGeometry(self.width() - 120, self.height() - 100, 100, 50)
        self.display_button.clicked.connect(self.open_display_page)

        self.pixmap = QPixmap()
        self.webcam_label.setPixmap(self.pixmap)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_camera_feed)
        self.timer.start(30)

        self.image_folder = "captured_images"
        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder)
        self.display_page = DisplayPage(self.central_widget, self.image_folder)
        self.display_page.hide()

        self.load_style_sheet()

    def change_resolution(self, resolution):
        if resolution == "Full Screen":
            self.showFullScreen()
        else:
            width, height = map(int, resolution.split("x"))
            self.resize(width, height)
            self.showNormal()

    def quit_application(self):
        QApplication.quit()

    def update_camera_feed(self):
        frame = self.camera_manager.capture_frame()
        if frame is not None:
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QPixmap.fromImage(QImage(rgb_image.data, rgb_image.shape[1], rgb_image.shape[0], QImage.Format_RGB888))
            scaled_image = self.scale_image(image)
            self.webcam_label.setPixmap(scaled_image)

    def scale_image(self, image):
        return image.scaled(self.webcam_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

    def closeEvent(self, event):
        self.camera_manager.release_camera()
        event.accept()

    def load_style_sheet(self):
        file = QFile("style.qss")
        file.open(QIODevice.ReadOnly | QIODevice.Text)
        stream = QTextStream(file)
        self.setStyleSheet(stream.readAll())

    def capture_image(self):
        frame = self.camera_manager.capture_frame()
        if frame is not None:
            image_path = os.path.join(self.image_folder, f"image_{len(os.listdir(self.image_folder))}.jpg")
            cv2.imwrite(image_path, frame)
            print(f"Image saved to {image_path}")

    def open_display_page(self):
        self.webcam_label.hide()
        self.capture_button.hide()
        self.display_button.hide()
        self.sidebar.hide()
        self.timer.stop()
        self.display_page.show()

    def show_camera_page(self):
        self.display_page.hide()
        self.webcam_label.show()
        self.capture_button.show()
        self.display_button.show()
        self.sidebar.show()
        self.timer.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())