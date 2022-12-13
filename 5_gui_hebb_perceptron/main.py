from PyQt5 import QtCore, uic, QtWidgets
from PyQt5.QtWidgets import QAction, QApplication, QLabel, QPushButton, QRadioButton, QSpinBox
import operacoes

train = [(1, 1, 1), (1, -1, 1), (-1, 1, 1), (-1, -1, 1)]
exp_outp = [1, -1, -1, -1]
w = []
hebb_bol = True
epoch = 0


def treino():
    global hebb_bol
    if hebb_bol:
        hebb()
    else:
        perceptroon()


def hebb_check():
    global hebb_bol
    hebb_bol = True


def percep_check():
    global hebb_bol
    hebb_bol = False


def hebb():
    epoch.setVisible(False)
    global train, exp_outp, w
    w = [0, 0, 0]
    for i in range(len(train)):
        for j in range(len(train[i]) - 1):
            w[j] = w[j] + (int(train[i][j]) * int(exp_outp[i]))
        w[2] = w[2] + int(exp_outp[i])

    w_values_1.setText('w1 = ' + str(w[0]))
    w_values_2.setText('w2 = ' + str(w[1]))
    w_values_baias.setText('wb = ' + str(w[2]))


def perceptroon():
    global train, exp_outp, w, epoch
    epoch.setVisible(True)
    epoch.setText('Epocas = ' + str(epoch))
    epoch = 0
    w = [0, 0, 0]
    a = 1
    t = 0
    test = 0

    learning = True
    while (learning):
        epoch += 1
        test = 0
        for i in range(len(train)):
            summ = 0
            summ += int(w[2])
            for j in range(len(train[i]) - 1):
                summ += int(train[i][j]) * int(w[j])

            if (summ > t):
                y = 1
            elif ((summ >= -t) and (summ <= t)):
                y = 0
            elif (summ < -t):
                y = -1

            if (int(exp_outp[i]) == y):
                test += 1
                if test == 1:
                    learning = False
            else:
                leng = len(w)
                for j in range(leng):
                    w[j] = int(w[j]) + (a * int(outp[j]) * summ)
                if j == leng - 1:
                    w[j] = int(w[j]) + (a * int(outp[j]))

    w_values_1.setText('w1 = ' + str(w[0]))
    w_values_2.setText('w2 = ' + str(w[1]))
    w_values_baias.setText('wb = ' + str(w[2]))
    epoch.setText('Epocas = ' + str(epoch))


def operar():
    global w
    x1 = entrada1.value()
    x2 = entrada2.value()

    if hebb_.isChecked():
        hebb()
        value = operacoes.hebb(x1, x2, w)
        resultado.setText('Resultado = ' + str(value))
    elif percep.isChecked():
        perceptron()
        value = operacoes.percp(x1, x2, w)
        resultado.setText('Resultado = ' + str(value))


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication([])

    Pyqt = uic.loadUi(r"interface.ui")

    # Labels
    epoch = Pyqt.findChild(QLabel, 'Época')
    epoch.setVisible(False)
    aprendizado = Pyqt.findChild(QLabel, 'Aprendizado')
    treinamento = Pyqt.findChild(QLabel, 'Treinamento')
    treinamento_text = Pyqt.findChild(QLabel, 'inputs_t')
    treinamento_text2 = Pyqt.findChild(QLabel, 'outputs')
    input_treinamento = Pyqt.findChild(QLabel, 'Input_value')
    input_treinamento.setText(str(train))
    output_treinamento = Pyqt.findChild(QLabel, 'output_values')
    output_treinamento.setText(str(exp_outp))
    peso_text = Pyqt.findChild(QLabel, 'w_label')
    w_values_1 = Pyqt.findChild(QLabel, 'Peso_1')
    w_values_2 = Pyqt.findChild(QLabel, 'Peso_2')
    w_values_baias = Pyqt.findChild(QLabel, 'Peso_bias')
    executando = Pyqt.findChild(QLabel, 'Executando')
    resultado = Pyqt.findChild(QLabel, 'Resultado')
    dados = Pyqt.findChild(QLabel, 'Dados')

    # Butões
    treinar = Pyqt.findChild(QPushButton, 'Treinar_but')
    treinar.clicked.connect(treino)

    testar = Pyqt.findChild(QPushButton, 'Testar')
    testar.clicked.connect(operar)

    hebb_ = Pyqt.findChild(QRadioButton, 'hebb')
    hebb_.setChecked(1)
    hebb_.toggled.connect(hebb_check)
    percep = Pyqt.findChild(QRadioButton, 'percep')
    percep.toggled.connect(percep_check)

    entrada1 = Pyqt.findChild(QSpinBox, 'Dado_1')
    entrada2 = Pyqt.findChild(QSpinBox, 'Dado_2')

    Pyqt.show()
    app.exec_()
