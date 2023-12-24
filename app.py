import sys
from validacpf import validacpf
from gerador_cpf import geradorcpf
from PyQt6.QtWidgets import QApplication, QMainWindow

print(geradorcpf())
import design


class GeraValidaCpf(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btn_gera.clicked.connect(self.geracpf)
        self.btn_valida.clicked.connect(self.valida)

    def geracpf(self):
        print('gera')

    def valida(self):
        cpf = self.input_valida.text()
        self.labelRetorno.setText(str(validacpf(cpf)))


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_valida_cpf = GeraValidaCpf()
    gera_valida_cpf.show()
    qt.exec()
