import sys
from pyfilterbank import splweighting
import numpy as np
from WaveReader import WaveReader
from acoustics import standards


class CmdInterface:
    @staticmethod
    def get_frequency_weighting_from_cmd():
        try:
            frequency_weighting = sys.argv[2]
            if frequency_weighting not in ['A', 'B', 'C']:
                raise ValueError('frequency weighting must be "A", "B" or "C" not {}'.format(frequency_weighting))
        except IndexError:
            frequency_weighting = 'A'
        return frequency_weighting

    @staticmethod
    def get_time_weighting_from_cmd():
        try:
            time_weighting = sys.argv[3]
            if time_weighting not in ['slow', 'fast']:
                raise ValueError('time weighting must be "slow" or "fast", not {}'.format(time_weighting))
        except IndexError:
            time_weighting = 'slow'
        return time_weighting


class SamplesConverter:
    """Convert samples from given wave file to frequency and time weighted signal according to IEC 61672-1:2013"""

    def __init__(self, file_path):
        self.wave_reader_object = WaveReader(file_path)
        self.audio_samples_generator = self.wave_reader_object.read_audio_data_chunk()
        self.frequency_weighting = CmdInterface.get_frequency_weighting_from_cmd()
        self.time_weighting = CmdInterface.get_time_weighting_from_cmd()

    def convert_all_file_samples(self,):
        all_converted_samples = []
        while True:
            try:
                all_converted_samples += next(self.convert_samples())
            except StopIteration as e:
                break
        return all_converted_samples

    def convert_samples(self,):
        """
        Make full conversion according to IEC-61672.
        :return:  db_fs_samples([float]): frequency and time weighted full scale level.
        """
        while True:
            try:
                samples = next(self.audio_samples_generator)
            except StopIteration:
                return
            frequency_weighted_samples = self._filter_samples_with_weighting_filter(samples)
            time_weighted_samples = self._filter_db_samples_samples_with_time_constant(frequency_weighted_samples**2)
            db_fs_samples = self._convert_samples_to_db_fs(time_weighted_samples)
            yield db_fs_samples

    def _filter_samples_with_weighting_filter(self, samples):
        """Filter samples with weighting filter. Use one of the weighting defined in IEC-61672. Weighting is defined in
        class variable.
        Parameters
        ---------------
            samples([float]): list of samples representing dynamic pressure level.
        :return:
            samples_weighted([float]): list of samples representing weighted samples of dynamic pressure level.

        """

        samples_weighted = splweighting.weight_signal(samples,
                                                      self.wave_reader_object.frame_rate,
                                                      self.frequency_weighting)
        return samples_weighted

    def _convert_samples_to_db_fs(self, energy_samples):
        """Convert samples in energy unit(preferably p^2) to dB FS.
        FS value is calculated from sample_width of read object.
        Args:
            energy_samples(list): list of samples in energy unit (e.x p^2).
        returns:
            list(samples_db_fs): list of samples in dB FS format.
        """
        # TODO: Verify if it is true dB FS, preferably in standard  AES17-1998,[13] IEC 61606
        # TODO: Check how RMS is measured. Mean is already did by time integration!
        max_value = 2**(self.wave_reader_object.sample_width*8 - 1)
        samples_db_fs = [20 * self._log_10_dealing_with_0(np.sqrt(sample/max_value**2)*np.sqrt(2))
                         for sample in energy_samples]
        return list(samples_db_fs)

    def _log_10_dealing_with_0(self, value):
        """Normal np.log10 but if value is 0 return dummy small value."""
        dummy_value = 10**-10
        if value == 0:
            result = dummy_value
        else:
            result = np.log10(value)
        return result

    def _filter_db_samples_samples_with_time_constant(self, samples):
        """Take dynamic pressure samples and integrate it with time constant defined in IEC-61672-2013.
        Interact which command line do take time constant to use. Allowed constants are "slow" or "fast".

        Parameters
        ----------
            samples: [float]
                    list of samples with dynamic pressure level.

        Returns
        --------
            list(time_weighted_samples): [float]
                                        list of samples weighted which defined time constant.

        """
        if self.time_weighting == 'slow':
            time_weighted_samples = standards.iec_61672_1_2013.slow(np.array(samples),
                                                                    self.wave_reader_object.frame_rate)
        else:
            time_weighted_samples = standards.iec_61672_1_2013.fast(np.array(samples),
                                                                    self.wave_reader_object.frame_rate)

        print('length changed from {} to {}'.format(len(samples),len(time_weighted_samples)))
        time_weighted_samples = list(time_weighted_samples)
        return time_weighted_samples
