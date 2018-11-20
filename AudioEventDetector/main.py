from WaveReader import WaveReader
from WaveFileSearcher import WaveFileSearcher
from Sample_dB_converter import SamplesConverter
from PlotsMaker import Plotter
from Detectors import TresholdCrossDetector
import pydoc

if __name__ == '__main__':
    wave_file_searcher = WaveFileSearcher()
    wave_files = wave_file_searcher.find_wave_files_paths()
    print('[main]')
    print('wave files: {}'.format(wave_files))
    for file in wave_files:
        print('[main;for]{}'.format(file))
        samples_converter = SamplesConverter(file)
        # all_samples = samples_converter.convert_all_file_samples()
        # print('I have {} samples with are {}'.format(len(all_samples), type(all_samples)))
        plotter = Plotter()
        samples_gen = samples_converter.convert_samples()
        occurrence_gen = TresholdCrossDetector.count_occurence(-25)
        occurrence = []
        while True:
            try:
                samples = next(samples_gen)
            except StopIteration:
                break
            next(occurrence_gen)
            occurrence += occurrence_gen.send(samples)
        print('i found {} occurrence'.format(len(occurrence)))
        print(occurrence)
        print('tadam')
    print("JUUUUUUUUUUUHUUUUUUUUUUUU")



