import math


class SamplesConverter:
    def samples_to_dB_FS_converter(self, bitdepth, samples):
        max_value = 2**(bitdepth - 1)
        converted_values = [20*math.log10(abs(sample)/max_value) for sample in samples]
        return converted_values

    def dB_FS_to_dB_A_converter(self, dB_values):
