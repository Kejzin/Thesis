from WaveReader import WaveReader
from WaveFileSearcher import WaveFileSearcher
from Sample_dB_converter import SamplesConverter
import logging

if __name__ == '__main__':
    wave_file_searcher = WaveFileSearcher()
    wave_files = wave_file_searcher.find_wave_files()
    print('elo')
    print('wave files: {}'.format(wave_files))
    for file in wave_files:
        print(file)
        print('jestem w for w main')
        # wave_reader = WaveReader(file)
        samples_converter = SamplesConverter(file)
        print('koncze')

