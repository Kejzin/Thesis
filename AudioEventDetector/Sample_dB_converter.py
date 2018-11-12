from pyfilterbank import splweighting
import sys
import numpy as np
from WaveReader import WaveReader


class SamplesConverter:
    def __init__(self, file_path):
        self.wave_reader_object = WaveReader(file_path)
        self.audio_samples_generator = self.wave_reader_object.read_audio_data_chunk()
        self.weighting = self._get_weighting_from_cmd()
        self._samples = []
        self._filtered_samples = []

  def convert_samples_to_db_fs(self, ):
        
        max_value = 2**(self.wave_reader_object.sample_width - 1)
        
        converted_values = []
        for sample in self._filtered_samples:
            new_converted_value = 0
            if(sample > 0):
                new_converted_value = 20*math.log10(abs(sample)/max_value)
            
            converted_values.append(new_converted_value);

        return converted_values

    def filter_samples_with_weighting_filter(self, ):
        try:
            self._samples = next(self.audio_samples_generator)
            self._filtered_samples = splweighting.weight_signal(self._samples, self.wave_reader_object.frame_rate, 'A')
        except StopIteration as e:
            raise

    def _get_weighting_from_cmd(self,):
        try:
            weighting = sys.argv[2]
        except IndexError as e:
            weighting = 'A'
        return weighting

    def _get_audio_chunk(self, ):
        self._samples = next(self.audio_samples_generator)

    def convert_all_audio_file(self,):
        while True:
            try:
                self.filter_samples_with_weighting_filter()
                self.convert_samples_to_db_fs()
                # print('original sample: {}, filtered sample: {}'.format(self._samples[0], self._filtered_samples[0]))
            except StopIteration:
                print('wszystko gra, sialala!')
                break
