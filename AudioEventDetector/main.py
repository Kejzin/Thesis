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
        all_samples = []
        while True:
            try:
                print(' [while]')
                try:
                    all_samples += next(converted_samples_generator)
                except ValueError as e:
                    print(e, 'but okay!')
            except StopIteration:
                print('[main:for:while]is there stop iteration?')
                break
        print(all_samples[0:10])
        print('I have {} samples with are {}'.format(len(all_samples), type(all_samples)))
        plotter = Plotter()
        plotter.simple_plot(all_samples)
        print('tadam')



