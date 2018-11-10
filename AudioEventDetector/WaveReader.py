import wave
import logging

class WaveReader:
    def wave_sample_width_channels_sample_rate_reader(self, file_path):
        """Read basic wave parameters and return it as a tuple """
        audio_file = wave.open(file_path, 'rb')
        sample_width = audio_file.getsampwidth()
        print(sample_width)
        channels = audio_file.getnchannels()
        rate = audio_file.getframerate()
        audio_data = (file_path, sample_width, channels, rate)
        logging.info(audio_data)
        return audio_data

    def audio_data_chunk_reader(self, wave_object, chunk_size=512):
        """ Read audio data in chunks"""
        while True:
            data = wave_object.readnframes(chunk_size)
            if not data:
                break
            yield data
