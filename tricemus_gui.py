import sys  # sys нужен для передачи argv в QApplication

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from gui import Ui_MainWindow  # Это наш конвертированный файл дизайна
from tricemus import Tricemus
from utils import write, read


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле gui.py
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_encrypt.clicked.connect(self.encrypt)
        self.ui.button_decrypt.clicked.connect(self.decrypt)
        self.ui.Button_open_encrypt.clicked.connect(lambda: self.open_file("ENC"))
        self.ui.button_save_encrypt.clicked.connect(lambda: self.save_file("ENC"))
        self.ui.button_open_decrypt.clicked.connect(lambda: self.open_file("DEC"))
        self.ui.button_save_decrypt.clicked.connect(lambda: self.save_file("DEC"))
        self.ui.button_open_key.clicked.connect(self.open_key)
        self.ui.button_save_key.clicked.connect(self.save_key)

        self.tricemus = Tricemus()
        self.encrypted_text = None
        self.text = None
        self.decrypted_text = None

    def encrypt(self):
        self.encrypted_text = None
        self.decrypted_text = None
        self.text = read(self.ui.line_openfile_encrypt.text())
        keyword = self.ui.line_key.text()
        self.tricemus.change_key(keyword=keyword)
        encrypted_text = self.tricemus.encrypt(self.text)
        self.encrypted_text = encrypted_text
        write(self.ui.line_savefile_encrypt.text(), encrypted_text)

    def decrypt(self):
        self.decrypted_text = None
        text = read(self.ui.line_openfile_decrypt.text())
        keyword = self.ui.line_key.text()
        self.tricemus.change_key(keyword=keyword)
        decrypt_text = self.tricemus.decrypt(text)
        self.decrypted_text = decrypt_text
        write(self.ui.line_savefile_decrypt.text(), decrypt_text)

    def open_file(self, mode):
        fname, _ = QFileDialog.getOpenFileName(self,
                                               'Open file',
                                               '',
                                               'All files (*.*)',
                                               options=QFileDialog.DontUseNativeDialog)
        if mode == "ENC":
            self.ui.line_openfile_encrypt.setText(fname)
        if mode == "DEC":
            self.ui.line_openfile_decrypt.setText(fname)

    def save_file(self, mode):
        fname, _ = QFileDialog.getSaveFileName(self,
                                               'Save file',
                                               '',
                                               'All files (*.*)',
                                               options=QFileDialog.DontUseNativeDialog)
        if mode == "ENC":
            self.ui.line_savefile_encrypt.setText(fname)
        if mode == "DEC":
            self.ui.line_savefile_decrypt.setText(fname)

    def open_key(self):
        fname, _ = QFileDialog.getOpenFileName(self,
                                               'Open file',
                                               '',
                                               'Tricemus Key files (*.keytr)',
                                               options=QFileDialog.DontUseNativeDialog)
        if fname == '':
            return
        if fname.endswith(".keytr"):
            pass
        else:
            fname += ".keytr"
        key = read(fname)
        self.ui.line_key.setText(key)

    def save_key(self):
        fname, _ = QFileDialog.getSaveFileName(self,
                                               'Save file',
                                               '',
                                               'Tricemus Key files (*.keytr)',
                                               options=QFileDialog.DontUseNativeDialog)

        if fname == '':
            return
        if fname.endswith(".keytr"):
            pass
        else:
            fname += ".keytr"
        key = self.ui.line_key.text()
        write(fname, key)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
