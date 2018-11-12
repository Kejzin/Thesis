import math
from pyfilterbank import splweighting
import sys
from WaveReader import WaveReader


class SamplesConverter:
    def __init__(self, file_path):
        self.wave_reader_object = WaveReader(file_path)
        self._samples = [1]
        self.audio_samples_generator = self.wave_reader_object.read_audio_data_chunk()
        self.weighting = self._get_weighting_from_cmd()
        self.filtered_samples = self.filter_samples_with_weighting_filter()

    def convert_samples_to_db_fs(self,):
        max_value = 2**(self.wave_reader_object.sample_width - 1)
        converted_values = [20*math.log10(abs(sample)/max_value) for sample in self._filtered_samples]
        return converted_values

    def filter_samples_with_weighting_filter(self, ):
        filtered_samples = []
        for _ in range(5):
            self._samples = next(self.audio_samples_generator)
            print(self._samples[1:10])
            filtered_samples.append(splweighting.weight_signal(self._samples, self.wave_reader_object.frame_rate, 'A'))
            print('filtered_samples = {}'.format(filtered_samples))
        return filtered_samples

    def _get_weighting_from_cmd(self, ):
        try:
            weighting = sys.argv[2]
        except IndexError as e:
            weighting = 'A'
        return weighting

    def _get_audio_chunk(self, ):
        self._samples = next(self.audio_samples_generator)

