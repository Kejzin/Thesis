import wave
import struct


class WaveWriter:
    def __init__(self,):
        """Write audio files which audio events."""
        pass

    def read_defined_frames(self, file_path, event):
        start, end, length = event
        audio_file = wave.open(file_path, 'rb')
        audio_file.rewind()
        frame_rate = audio_file.getframerate()
        audio_file.setpos(audio_file.tell() + start*frame_rate)
        frames = audio_file.readframes(length*frame_rate)
        params = audio_file.getparams()
        print("[read_defined_frames] {}".format(len(frames)))
        frames_and_params = (frames, params)
        return frames_and_params

    def write_defined_frames(self, file_path, frames_and_params):
        frames, params = frames_and_params
        audio_file = wave.open(file_path, 'wb')
        audio_file.setparams(params)
        audio_file.writeframes(frames)
        print('new file is {} sampwidth'.format(audio_file.getsampwidth()))
        audio_file.close()


class WaveReader:
    def __init__(self, file_path):
        """"Read audio file in small chunk. Decode data from bytes to float value.
        Parameters
        ----------
            file_path: str
                path to file or directory contained files. Must be absolute path.
            """
        self.file_path = file_path
        self.audio_file = wave.open(file_path, 'rb')
        self.sample_width = self.audio_file.getsampwidth()
        self.channels = self.audio_file.getnchannels()
        self.frame_rate = self.audio_file.getframerate()

    def read_audio_data_chunk(self, seconds_to_read=60):
        """ Read audio data in chunks.
        Parameters
        ----------
            seconds_to_read: int
                define how many seconds will be read from file.
        Returns
        -------
            samples: [float]
                list of value of audio samples."""
        chunk_size = seconds_to_read * self.frame_rate
        print('frame rate is {}, chunk size is {}'.format(self.frame_rate, chunk_size))
        print('start reading {}'.format(self.file_path))
        print('total lenght is {}'.format(self.audio_file.getnframes()))
        while True:
            print('[read_audio_data_chunk]')
            start = self.audio_file.tell()
            samples = self.audio_file.readframes(chunk_size)
            print('I have read samples from {} to {}'.format(start, self.audio_file.tell()))
            print('I try to read {} samples'.format(self.audio_file.tell()-start))
            if not samples:
                print('end reading {}. Read {} frames'.format(self.file_path, self.audio_file.tell()))
                return
            samples = self.decode_audio_chunk(samples)
            yield samples

    # TODO: Check what exactly size must be here
    @staticmethod
    def decode_audio_chunk(samples):
        fmt = '<{}h'.format(len(samples)//2)
        print(struct.calcsize(fmt))
        print("FMT IS {}".format(fmt))
        decoded_samples = struct.unpack(fmt, samples)
        return list(decoded_samples)


