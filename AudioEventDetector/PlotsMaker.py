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
        b, a = signal.zpk2tf([], [-1], 1)
        filter = signal.freqs(b, a)
        filter1 = signal.bilinear(b, a)
        print(filter1)
        plt.plot(filter1) #, filter)
        plt.show

        #TODO FFT, mnozenie i odwrotne FFT
        while False:
            try:
                converter.filter_samples_with_weighting_filter()
            except StopIteration:
                print('stop')
                break
            samples = converter.convert_filtered_samples_to_db_fs()
            tempf += np.array(signal.filtfilt(b, a, samples)).tolist()
            # tempf += signal.convolve(filter1, samples)
            print('tempf: {}'.format(tempf[1:3]))
        print('koncze czytac')
        print(len(tempf))
        plt.plot(tempf)
        plt.show()

