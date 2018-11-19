from WaveReader import WaveReader
from WaveFileSearcher import WaveFileSearcher
from Sample_dB_converter import SamplesConverter
from PlotsMaker import Plotter
import numpy as np
import pydoc


def read_all_samples():
    samples = []
    while True:
        try:
            try:
                samples += next(converted_samples_generator)
            except ValueError as e:
                print(e, 'but okay!')
        except StopIteration as e:
            print('[for:while] {}'.format(e))
            break
    return samples

if __name__ == '__main__':
    wave_file_searcher = WaveFileSearcher()
    wave_files = wave_file_searcher.find_wave_files_paths()
    print('[main]')
    print('wave files: {}'.format(wave_files))
    for file in wave_files:
        print('[main;for]{}'.format(file))
        samples_converter = SamplesConverter(file)
        converted_samples_generator = samples_converter.convert_samples()
        all_samples = read_all_samples()
        print('I have {} samples with are {}'.format(len(all_samples), type(all_samples)))
        plotter = Plotter()
        # plotter.simple_plot(all_samples)
        print('tadam')
    print("JUUUUUUUUUUUHUUUUUUUUUUUU")



