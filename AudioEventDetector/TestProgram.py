from .WaveReader import WaveReader
import pytest
import logging


class TestWaveReader:
    def test_wave_sample_width_channels_sample_rate_reader(self,
                                                           file_path="C:\\Users\\kejzin\\Documents\\"
                                                                      "Thesis\\Thesis\\TestFiles\\Test_wave.wav"):
        wave_reader_obj = WaveReader()
        wave_data = wave_reader_obj.wave_sample_width_channels_sample_rate_reader(file_path)
        logging.info(wave_data)
        assert wave_data == ("C:\\Users\\kejzin\\Documents\\Thesis\\Thesis\\TestFiles\\Test_wave.wav", 16, 1, 48000)
        logging.info('sialala')


if __name__ == "__main__":
    Test = TestWaveReader()
    Test.test_wave_sample_width_channels_sample_rate_reader()
