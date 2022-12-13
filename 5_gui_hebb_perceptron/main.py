from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QComboBox


def choose(self):
    if opt.currentText() == "Hebb":
        input = [[int(x1.currentText()), int(y1.currentText())], [int(x2.currentText()), int(y2.currentText())],
                 [int(x3.currentText()), int(y3.currentText())], [int(x4.currentText()), int(y4.currentText())]]
        target = [int(out1.currentText()), int(out2.currentText()), int(out3.currentText()), int(out4.currentText())]

        class Neuron:
            def __init__(self, input, outputs) -> None:
                self.input = input
                self.target = outputs
                self.w = [0, 0, 0]

            def update_weight(self):
                self.old_weight = self.w
                for i in range(len(self.input)):
                    for j in range(len(self.w)):
                        if j > 1:
                            self.w[j] = self.old_weight[j] + self.target[i]
                        else:
                            self.w[j] = self.old_weight[j] + self.input[i][j] * self.target[i]

            def test(self, input):
                self.y = 0
                for i in range(len(input)):
                    self.y += input[i] * self.w[i]
                self.y += self.w[2]

                if self.y > 0:
                    self.y = 1
                else:
                    self.y = -1
                return self.y

        global neuron
        neuron = Neuron(input, target)
        neuron.update_weight()
        w1.setText(str(neuron.w[0]))
        w2.setText(str(neuron.w[1]))
        w3.setText(str(neuron.w[2]))

    elif opt.currentText() == "Perceptron":
        input = [[int(x1.currentText()), int(y1.currentText())], [int(x2.currentText()), int(y2.currentText())],
                 [int(x3.currentText()), int(y3.currentText())], [int(x4.currentText()), int(y4.currentText())]]
        target = [int(out1.currentText()), int(out2.currentText()), int(out3.currentText()), int(out4.currentText())]

        class Perceptron:
            def __init__(self, input, outputs) -> None:
                self.input = input
                self.target = outputs
                self.teta = 0
                self.w = [0, 0, 0]
                self.alpha = 1

            def update_weight(self):
                self.stop = 0
                self.Y = 0
                self.times = 0
                self.y_output = 0
                while self.stop == 0:
                    self.sum = 0
                    for i in range(len(self.input)):

                        for j in range(len(self.input[i])):
                            self.y_output += self.input[i][j] * self.w[j]

                        self.y_output += self.w[2] * 1
                        if self.y_output > self.teta:
                            self.Y = 1
                        elif self.y_output < self.teta:
                            self.Y = -1
                        elif self.y_output >= self.teta or self.y_output <= self.teta:
                            self.Y = 0
                        self.y_output = 0
                        if self.Y != self.target[i]:
                            self.old_weight = self.w
                            for k in range(len(self.w)):
                                if k < 2:
                                    self.w[k] = self.old_weight[k] + self.input[i][k] * self.target[i] * self.alpha
                                else:
                                    self.w[k] = self.old_weight[k] + self.target[i] * self.alpha

                        else:
                            self.sum += 1
                    self.times += 1
                    if self.sum == len(self.target):
                        self.stop = 1

            def test(self, input):
                self.y = 0
                for i in range(len(input)):
                    self.y += input[i] * self.w[i]
                self.y += self.w[2]

                if self.y > self.teta:
                    self.y = 1
                else:
                    self.y = -1
                return self.y

        global perceptron
        perceptron = Perceptron(input, target)
        perceptron.update_weight()
        w1.setText(str(perceptron.w[0]))
        w2.setText(str(perceptron.w[1]))
        w3.setText(str(perceptron.w[2]))


def Run():
    if opt.currentText() == "Hebb":
        ent = [int(input1.currentText()), int(input2.currentText())]
        y = neuron.test(ent)
        out.setText(str(y))
    elif opt.currentText() == "Perceptron":

        ent = [int(input1.currentText()), int(input2.currentText())]
        y = perceptron.test(ent)
        out.setText(str(y))


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication([])

    window = uic.loadUi('C:/Users/jesse/Desktop/Facul/ia-cc-2022-2-jessegabriel/5_gui_hebb_perceptron/gui.ui')

    x1 = window.findChild(QComboBox, 'input1_x')
    x2 = window.findChild(QComboBox, 'input2_x')
    x3 = window.findChild(QComboBox, 'input3_x')
    x4 = window.findChild(QComboBox, 'input4_x')

    y1 = window.findChild(QComboBox, 'input1_y')
    y2 = window.findChild(QComboBox, 'input2_y')
    y3 = window.findChild(QComboBox, 'input3_y')
    y4 = window.findChild(QComboBox, 'input4_y')

    out1 = window.findChild(QComboBox, 'out1')
    out2 = window.findChild(QComboBox, 'out2')
    out3 = window.findChild(QComboBox, 'out3')
    out4 = window.findChild(QComboBox, 'out4')

    input1 = window.findChild(QComboBox, 'inputTest1')
    input2 = window.findChild(QComboBox, 'inputTest2')

    w1 = window.findChild(QLabel, 'w1')
    w2 = window.findChild(QLabel, 'w2')
    w3 = window.findChild(QLabel, 'w3')
    out = window.findChild(QLabel, 'out')
    opt = window.findChild(QComboBox, 'comboBox')
    train = window.findChild(QPushButton, 'btnTrain')
    train.clicked.connect(choose)

    run = window.findChild(QPushButton, 'RUN')
    run.clicked.connect(Run)
    window.show()

    app.exec_()
