import wave
import struct


class WaveReader:
    def __init__(self, file_path):
        self.audio_file = wave.open(file_path, 'rb')
        self.sample_width = self.audio_file.getsampwidth()
        self.channels = self.audio_file.getnchannels()
        self.frame_rate = self.audio_file.getframerate()

    def read_audio_data_chunk(self, seconds_to_read=10):
        """ Read audio data in chunks"""
        chunk_size = seconds_to_read * self.frame_rate
        print('frame rate is {}, chunk size is {}'.format(self.frame_rate, chunk_size))
        while True:
            samples = self.audio_file.readframes(chunk_size)
            if samples is None:

                return
            samples = self._decode_audio_chunk(samples)
            yield samples

    def _decode_audio_chunk(self, samples):
        fmt = '<{}h'.format(len(samples)//2)
        decoded_samples = struct.unpack(fmt, samples)
        return decoded_samples


