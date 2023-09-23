import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QFormLayout
from PyQt5.QtGui import QFont
from PyQt5 import QtCore

import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

import numpy as np


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Plotting trigonometric functions in Qt')

        # create a layout
        layout = QFormLayout()
        self.setLayout(layout)


        label = QLabel('Function name - please press the button')
        label.setFont(QFont('Arial', 12))
        label.setStyleSheet("background-color : white; color : darkblue")
        label.setAlignment(QtCore.Qt.AlignCenter)
      
        layout.addWidget(label)

        
        sc = MplCanvas(self, width=6, height=5, dpi=100)

        layout.addWidget(sc)

       
        titles = ['Plot cos wave', 'Plot sin wave', 'Exit']
        buttons = [QPushButton(title) for title in titles]
        for button in buttons:
            layout.addWidget(button)

        buttons[0].setToolTip("Press button for plot cos wave!!!")
        buttons[0].setStyleSheet("background-color : darkblue; color : white")
        buttons[0].clicked.connect(lambda: self.plot_cos(sc, label))

        buttons[1].setToolTip("Press button for plot sin wave!!!")
        buttons[1].setStyleSheet("background-color : darkblue; color : white")
        buttons[1].clicked.connect(lambda: self.plot_sin(sc, label))

        buttons[2].setToolTip("Press button for closing app!!!")
        buttons[2].setStyleSheet("background-color : darkblue; color : white")
        buttons[2].clicked.connect(app.exit)

        
        self.setStyleSheet('''QToolTip { 
                           background-color: darkblue; 
                           color: white; 
                           border: white solid 1px
                           }''')
        
      
        self.show()

    def change_text(self, label, gon):
        if gon == "sin":
            label.setText('SIN WAVE')
        elif gon == "cos":
            label.setText('COS WAVE')
        label.setStyleSheet("background-color : lightgrey; color : darkblue")

    def plot_sin(self, sin_plot, label):
        sin_plot.axes.cla()
        time = np.arange(0, 10, 0.1)
        amplitude = np.sin(time)
        sin_plot.axes.plot(time, amplitude)
        sin_plot.axes.set_title("Sin Wave")
        sin_plot.axes.set_xlabel("Time")
        sin_plot.axes.set_ylabel('Amplitude = sin(time)')
        sin_plot.draw()
        self.change_text(label, "sin")

    def plot_cos(self, cos_plot, label):
        cos_plot.axes.cla()
        time = np.arange(0, 10, 0.1)
        amplitude = np.cos(time)
        cos_plot.axes.plot(time, amplitude)
        cos_plot.axes.set_title("Cosine Wave")
        cos_plot.axes.set_xlabel("Time")
        cos_plot.axes.set_ylabel('Amplitude = cos(time)')
        cos_plot.draw()
        self.change_text(label, "cos")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())