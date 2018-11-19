import wave
import struct


class WaveReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.audio_file = wave.open(file_path, 'rb')
        self.sample_width = self.audio_file.getsampwidth()
        self.channels = self.audio_file.getnchannels()
        self.frame_rate = self.audio_file.getframerate()

    def read_audio_data_chunk(self, seconds_to_read=60):
        """ Read audio data in chunks"""
        chunk_size = seconds_to_read * self.frame_rate
        print('frame rate is {}, chunk size is {}'.format(self.frame_rate, chunk_size))
        print('start reading {}'.format(self.file_path))
        while True:
            print('[read_audio_data_chunk]')
            start = self.audio_file.tell()
            samples = self.audio_file.readframes(chunk_size)
            print('I have read samples from {} to {}'.format(start, self.audio_file.tell()))
            if not samples:
                print('end reading {}. Read {} frames'.format(self.file_path, self.audio_file.tell()))
                return
            samples = self._decode_audio_chunk(samples)
            yield samples

    def _decode_audio_chunk(self, samples):
        fmt = '<{}h'.format(len(samples)//2)
        decoded_samples = struct.unpack(fmt, samples)
        return list(decoded_samples)


