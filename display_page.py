from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

class DisplayPage(QWidget):
    def __init__(self, parent, image_folder):
        super().__init__(parent)
        self.setGeometry(0, 0, parent.width(), parent.height())
        self.image_folder = image_folder
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        self.back_button = QPushButton("Back", self)
        self.back_button.setGeometry(20, 20, 100, 50)
        self.back_button.clicked.connect(self.go_back)

        self.image_index = 0
        self.update_image()

    def update_image(self):
        image_files = os.listdir(self.image_folder)
        if image_files:
            image_path = os.path.join(self.image_folder, image_files[self.image_index])
            self.display_image(image_path)

    def display_image(self, image_path):
        image = QPixmap(image_path)
        scaled_image = self.scale_image(image)
        self.image_label.setPixmap(scaled_image)
        self.image_label.setAlignment(Qt.AlignCenter)

    def scale_image(self, image):
        return image.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

    def go_back(self):
        self.parent().show_camera_page()
        self.hide()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.image_index = (self.image_index - 1) % len(os.listdir(self.image_folder))
            self.update_image()
        elif event.key() == Qt.Key_Right:
            self.image_index = (self.image_index + 1) % len(os.listdir(self.image_folder))
            self.update_image()