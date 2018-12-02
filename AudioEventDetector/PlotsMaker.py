import matplotlib.pyplot as plt
from SampledBConverter import SamplesDbFsConverter
from scipy import signal
import numpy as np


class Plotter:
    @staticmethod
    def simple_plot(data):
        print('i want to plot something')
        plt.plot(data)
        plt.show()

