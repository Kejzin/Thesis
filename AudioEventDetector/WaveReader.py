import wave
import logging


class WaveReader:
    def __init__(self, file_path):
        self.audio_file = wave.open(file_path, 'rb')
        self.sample_width = self.audio_file.getsampwidth()
        self.channels = self.audio_file.getnchannels()
        self.frame_rate = self.audio_file.getframerate()

    def audio_data_chunk_reader(self, seconds_to_read = 10):
        """ Read audio data in chunks"""
        chunk_size = seconds_to_read * self.frame_rate
        while True:
            try:
                data = self.audio_file.readnframes(chunk_size)
            except Exception as e:
                # TODO make more concrete exception
                logging.info('full file read', e)
                self. audio_file.close()
                break
            yield data
