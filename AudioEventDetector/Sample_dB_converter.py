import sys
from pyfilterbank import splweighting
import numpy as np
from WaveReader import WaveReader


class SamplesConverter:
    def __init__(self, file_path):
        self.wave_reader_object = WaveReader(file_path)
        self.audio_samples_generator = self.wave_reader_object.read_audio_data_chunk()
        self.weighting = self._get_weighting_from_cmd()
        self._samples = []
        self._filtered_samples = []

    def convert_samples_to_db_fs(self,):
        max_value = 2**(self.wave_reader_object.sample_width*8 - 1)
        print('[convert_samples_to_db_fs] sample width is: {}'.format(self.wave_reader_object.sample_width))
        converted_values = [20*np.log10(np.abs(sample)/max_value) for sample in self._filtered_samples if sample]
        return converted_values

    def filter_samples_with_weighting_filter(self,):
        try:
            self._samples = next(self.audio_samples_generator)
        except StopIteration :
            raise
        self._filtered_samples = splweighting.weight_signal(self._samples,
                                                            self.wave_reader_object.frame_rate,
                                                            self.weighting)

    def convert_filtered_samples_to_db_fs(self,):
        try:
            self.filter_samples_with_weighting_filter()
        except StopIteration:
            print('plik przeczytany w calosci!')
            raise
        converted_samples = self.convert_samples_to_db_fs()
        return converted_samples

    def apply_time_constant_to_db_samples(self, ):
        pass

    def _get_weighting_from_cmd(self,):
        try:
            weighting = sys.argv[2]
        except IndexError as e:
            weighting = 'A'
        return weighting

    def _get_audio_chunk(self,):
        self._samples = next(self.audio_samples_generator)

