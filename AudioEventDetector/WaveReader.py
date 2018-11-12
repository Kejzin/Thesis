import wave
import logging
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
        samples = (1)
        print('frame rate is {}, chunk size is {}'.format(self.frame_rate, chunk_size))
        while samples:
            print('czytamy od probki')
            print(self.audio_file.tell())
            samples = self.audio_file.readframes(chunk_size)
            # print('samples: {}'.format(samples[0:10]))
            samples = self._decode_audio_chunk(samples)
            # print(samples[0])
            yield samples

    def _decode_audio_chunk(self, samples):
        fmt = '<{}h'.format(len(samples)//2)
        decoded_samples = struct.unpack(fmt, samples)
        return decoded_samples


