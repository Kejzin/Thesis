import matplotlib.pyplot as plt
from Sample_dB_converter import SamplesConverter
from scipy import signal
import numpy as np


class Plotter:
    def __init__(self, file_path):
        self.file_path = file_path
    def simple_plot(self,):
        converter = SamplesConverter(self.file_path)
        print('robie wykres')
        tempf = []
        b, a = signal.butter(3, 0.0001)
        for _ in range(2):
            converter.filter_samples_with_weighting_filter()
            samples = converter.make_db_fs_a_samples()
            tempf += np.array(signal.filtfilt(b, a, samples)).tolist()
            print('tempf: {}'.format(tempf[1:3]))
        print(len(tempf))
        plt.plot(tempf)
        plt.show()

