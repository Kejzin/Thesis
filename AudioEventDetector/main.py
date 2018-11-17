from WaveReader import WaveReader
from WaveFileSearcher import WaveFileSearcher
from Sample_dB_converter import SamplesConverter
from PlotsMaker import Plotter
import numpy as np

if __name__ == '__main__':
    wave_file_searcher = WaveFileSearcher()
    wave_files = wave_file_searcher.find_wave_files_paths()
    print('[main]')
    print('wave files: {}'.format(wave_files))
    for file in wave_files:
        print('[main;for]{}'.format(file))
        SamplesConverter = SamplesConverter(file)
        converted_samples_generator = SamplesConverter.convert_samples()
        all_samples = np.empty(1)
        while True:
            try:
                print(' [while]')
                all_samples = np.add(all_samples, next(converted_samples_generator))
            except StopIteration:
                print('[main:for:while]is there stop iteration?')
                break
        print(list(all_samples))
        plotter = Plotter()
        plotter.simple_plot(all_samples)
        print('tadam')



