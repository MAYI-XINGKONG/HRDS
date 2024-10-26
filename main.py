import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui.main_window_ui import MainWindowUI
from logic.file_operation_logic import load_txt_files, choose_work_dir


def main():
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setGeometry(100, 100, 800, 600)
    window.setWindowTitle("HRDS")

    # 创建主窗口UI实例并设置到主窗口
    main_window_ui = MainWindowUI(window)
    window.setCentralWidget(main_window_ui)

    # 定义并初始化局部的工作目录变量
    current_work_dir = os.getcwd()

    def on_load_button_clicked():
        load_txt_files(main_window_ui.file_list_widget, current_work_dir)

    # 连接加载文件列表按钮的点击事件
    main_window_ui.load_button.clicked.connect(on_load_button_clicked)

    # 连接选择工作目录菜单动作的触发事件
    def on_work_dir_action_triggered():
        nonlocal current_work_dir
        new_work_dir = choose_work_dir()
        current_work_dir = new_work_dir

    main_window_ui.work_dir_action.triggered.connect(on_work_dir_action_triggered)

    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main();