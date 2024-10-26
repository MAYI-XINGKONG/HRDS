from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QMenu, QAction


class MainWindowUI(QWidget):
    def __init__(self, window):
        super().__init__()
        self.window = window

        # 创建整体布局
        self.layout = QVBoxLayout()

        # 创建一个水平布局用于放置按钮和文件列表
        self.h_layout = QHBoxLayout()

        # 创建加载文件列表按钮
        self.load_button = QPushButton("加载文件列表")
        self.h_layout.addWidget(self.load_button)

        # 创建文件列表部件
        self.file_list_widget = QListWidget()
        self.file_list_widget.setStyleSheet("background-color: lightgray;")
        self.h_layout.addWidget(self.file_list_widget)

        # 将水平布局添加到整体布局中
        self.layout.addLayout(self.h_layout)

        # 创建配置菜单
        self.menu_bar = self.window.menuBar()
        self.config_menu = self.menu_bar.addMenu("配置")

        # 创建工作目录子菜单
        self.work_dir_action = QAction("工作目录", self.window)
        self.config_menu.addAction(self.work_dir_action)

        # 设置自身布局
        self.setLayout(self.layout)