import math
from pyfilterbank import splweighting
import WaveReader

class SamplesConverter:
    def convert_samples_to_db_fs(self, bitdepth, samples):
        max_value = 2**(bitdepth - 1)
        converted_values = [20*math.log10(abs(sample)/max_value) for sample in samples]
        return converted_values

    def a_weighting_filters(self, samples, frame_rate):
        filtered_samples = splweighting.weight_signal(samples, frame_rate, 'A')
        return filtered_samples

