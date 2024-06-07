from PyQt5.QtWidgets import QLabel, QSlider, QComboBox, QPushButton, QScrollArea, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

def create_sidebar_menu(main_window, change_resolution_callback, quit_application_callback, camera_manager):
    sidebar = QWidget(main_window.central_widget)
    sidebar.setGeometry(0, 0, 250, main_window.height())
    sidebar.setStyleSheet("background-color: rgba(128, 128, 128, 0.5);")

    sidebar_scroll_area = QScrollArea(sidebar)
    sidebar_scroll_area.setWidgetResizable(True)
    sidebar_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    sidebar_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    sidebar_scroll_area.setGeometry(0, 0, sidebar.width(), sidebar.height())

    sidebar_scroll_content = QWidget(sidebar_scroll_area)
    sidebar_scroll_layout = QVBoxLayout(sidebar_scroll_content)
    sidebar_scroll_area.setWidget(sidebar_scroll_content)

    def toggle_sidebar():
        if sidebar.isVisible():
            sidebar.hide()
        else:
            sidebar.show()

    sidebar_button = QPushButton("Open Sidebar", main_window.central_widget)
    sidebar_button.setGeometry(10, 10, 150, 50)
    sidebar_button.clicked.connect(toggle_sidebar)

    close_sidebar_button = QPushButton("Close Sidebar")
    close_sidebar_button.clicked.connect(toggle_sidebar)
    sidebar_scroll_layout.addWidget(close_sidebar_button)

    exposure_label = QLabel("Exposure")
    sidebar_scroll_layout.addWidget(exposure_label)
    exposure_slider = QSlider(Qt.Horizontal)
    exposure_slider.valueChanged.connect(lambda value: camera_manager.setConfig("exposure", value))
    sidebar_scroll_layout.addWidget(exposure_slider)

    shutter_speed_label = QLabel("Shutter Speed")
    sidebar_scroll_layout.addWidget(shutter_speed_label)
    shutter_speed_slider = QSlider(Qt.Horizontal)
    shutter_speed_slider.valueChanged.connect(lambda value: camera_manager.setConfig("shutter_speed", value))
    sidebar_scroll_layout.addWidget(shutter_speed_slider)

    auto_exposure_label = QLabel("Auto Exposure Mode")
    sidebar_scroll_layout.addWidget(auto_exposure_label)
    auto_exposure_combo = QComboBox()
    auto_exposure_combo.addItems(["Mode 1", "Mode 2", "Mode 3"])
    auto_exposure_combo.currentTextChanged.connect(lambda mode: camera_manager.setConfig("auto_exposure", mode))
    sidebar_scroll_layout.addWidget(auto_exposure_combo)

    auto_focus_label = QLabel("Auto Focus Mode")
    sidebar_scroll_layout.addWidget(auto_focus_label)
    auto_focus_combo = QComboBox()
    auto_focus_combo.addItems(["Mode 1", "Mode 2", "Mode 3"])
    auto_focus_combo.currentTextChanged.connect(lambda mode: camera_manager.setConfig("auto_focus", mode))
    sidebar_scroll_layout.addWidget(auto_focus_combo)

    resolution_label = QLabel("Display Resolution")
    sidebar_scroll_layout.addWidget(resolution_label)
    resolution_combo = QComboBox()
    resolution_combo.addItems(["640x480", "800x600", "1024x768", "1280x720", "1920x1080", "Full Screen"])
    resolution_combo.currentTextChanged.connect(change_resolution_callback)
    sidebar_scroll_layout.addWidget(resolution_combo)

    power_menu_label = QLabel("Power Menu")
    sidebar_scroll_layout.addWidget(power_menu_label)
    quit_application_button = QPushButton("Quit Application")
    quit_application_button.clicked.connect(quit_application_callback)
    sidebar_scroll_layout.addWidget(quit_application_button)
    shutdown_machine_button = QPushButton("Shutdown Machine")
    sidebar_scroll_layout.addWidget(shutdown_machine_button)

    # Add more options here as needed
    for i in range(25):
        label = QLabel(f"Option {i+1}")
        sidebar_scroll_layout.addWidget(label)

    return sidebar