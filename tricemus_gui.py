import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from tricemus import Tricemus
from gui import Ui_MainWindow  # Это наш конвертированный файл дизайна


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле gui.py
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.open_file_pushButton.clicked.connect(self.open_file)
        self.ui.save_to_pushButton.clicked.connect(self.save_file)
        self.ui.load_text_pushButton.clicked.connect(self.load_text)
        self.ui.save_text_pushButton.clicked.connect(self.save_text)
        self.ui.encrypt_pushButton.clicked.connect(self.encrypt)
        self.ui.decrypt_pushButton.clicked.connect(self.decrypt)

    def encrypt(self):
        pass

    def decrypt(self):
        pass

    def load_text(self):
        pass

    def save_text(self):
        pass

    def open_file(self):
        fname, _ = QFileDialog.getOpenFileName(self,
                                               'Open file',
                                               '',
                                               'All files (*.*)',
                                               options=QFileDialog.DontUseNativeDialog)
        self.ui.open_file_lineEdit.setText(fname)

    def save_file(self):
        fname, _ = QFileDialog.getOpenFileName(self,
                                               'Save file',
                                               '',
                                               'All files (*.*)',
                                               options=QFileDialog.DontUseNativeDialog)
        self.ui.save_to_lineEdit.setText(fname)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
