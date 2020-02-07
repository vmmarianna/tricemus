import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from tricemus import Tricemus
from gui import Ui_MainWindow  # Это наш конвертированный файл дизайна
from utils import write, read

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
        self.tricemus = Tricemus()
        self.crypted_text = None
        self.text = None
        self.decrypted_text = None

    def encrypt(self):
        self.crypted_text = None
        keyword = self.ui.keyword_lineEdit.text()
        self.tricemus.change_key(keyword=keyword)
        crypted_text = self.tricemus.encrypt(self.text)
        self.crypted_text = crypted_text

    def decrypt(self):
        self.text = None
        keyword = self.ui.keyword_lineEdit.text()
        self.tricemus.change_key(keyword=keyword)
        text = self.tricemus.decrypt(self.crypted_text)
        self.text = text

        print('decrypt_pushButton')

    def load_text(self):
        load_path = self.ui.open_file_lineEdit.text()
        read_load_path = read(load_path)
        self.text = read_load_path
        print('load_text_pushButton')

    def save_text(self):
        save_path = self.ui.save_to_lineEdit.text()
        write(save_path, self.crypted_text)
        print('save_to_pushButton')

    def open_file(self):
        fname, _ = QFileDialog.getOpenFileName(self,
                                               'Open file',
                                               '',
                                               'All files (*.*)',
                                               options=QFileDialog.DontUseNativeDialog)
        self.ui.open_file_lineEdit.setText(fname)

    def save_file(self):
        fname, _ = QFileDialog.getSaveFileName(self,
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
