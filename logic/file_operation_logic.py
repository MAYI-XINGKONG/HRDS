import os
from PyQt5.QtWidgets import QFileDialog, QListWidget


def load_txt_files(file_list_widget, work_dir):
    file_list_widget.clear()
    txt_files = []

    if work_dir:
        for root, dirs, files in os.walk(work_dir):
            for file in files:
                if file.endswith(".txt"):
                    txt_files.append(os.path.join(root, file))

        for txt_file in txt_files:
            file_list_widget.addItem(txt_file)


def choose_work_dir():
    new_work_dir = QFileDialog.getExistingDirectory(None, "选择工作目录")
    return new_work_dir