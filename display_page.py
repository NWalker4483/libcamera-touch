from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap
import os

class DisplayPage(QWidget):
    def __init__(self, parent=None, image_folder="captured_images"):
        super().__init__(parent)
        self.image_folder = image_folder
        self.current_image_index = 0
        self.image_files = self.get_image_files()

        self.image_label = QLabel(self)
        self.image_label.setScaledContents(True)

        self.prev_button = QPushButton("Previous", self)
        self.prev_button.clicked.connect(self.show_previous_image)

        self.next_button = QPushButton("Next", self)
        self.next_button.clicked.connect(self.show_next_image)

        self.camera_button = QPushButton("Go to Camera", self)
        self.camera_button.clicked.connect(self.go_to_camera)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.prev_button)
        button_layout.addWidget(self.camera_button)
        button_layout.addWidget(self.next_button)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.image_label)
        main_layout.addLayout(button_layout)

        self.show_image()

    def get_image_files(self):
        return [f for f in os.listdir(self.image_folder) if f.endswith(".jpg")]

    def show_image(self):
        if self.image_files:
            image_path = os.path.join(self.image_folder, self.image_files[self.current_image_index])
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap)

    def show_previous_image(self):
        self.current_image_index = (self.current_image_index - 1) % len(self.image_files)
        self.show_image()

    def show_next_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.image_files)
        self.show_image()

    def go_to_camera(self):
        self.parent().show_camera_page()