import wave
import struct
import ntpath


class WaveWriter:
    def __init__(self, ):
        """Write audio files which audio events."""
        pass

    def read_defined_frames(self, file_path, event):
        """Read events from audio file
        Params
        ------
            file_path: str
                path to audio file which will be read
            event: (float, float, float)
                touple containing start, end and lenth of event
        Returns
        -------
            frames_and_params: (b, ())
                touple containing frames which event and params of file.
            """
        start, end, length = event
        audio_file = wave.open(file_path, 'rb')
        audio_file.rewind()
        frame_rate = audio_file.getframerate()
        start_position = audio_file.tell() + int(start * frame_rate)
        audio_file.setpos(start_position)
        frames_to_read = int(length * frame_rate)

        print('Read frames from {} to {}'.format(start_position, start_position + frames_to_read))

        frames = audio_file.readframes(frames_to_read)

        print('Samples from {} to {} has been read.'.format(start_position, audio_file.tell()))
        print('')

        params = audio_file.getparams()
        frames_and_params = (frames, params)
        return frames_and_params

    def write_defined_frames(self, file_dir_path, frames_and_params, count):
        """Write frames to file under defined path.
        Params
        ------
            file_dir_path: str
                path to dir where file should be save.
            frames_and_params: (b, ())
                frames to write and params of audio file
            count: int
                value to different each event"""
        frames, params = frames_and_params
        file_name = '{}/event_{}.wav'.format(file_dir_path, count)
        audio_file = wave.open(file_name, 'wb')
        audio_file.setparams(params)
        audio_file.writeframes(frames)
        print('Wrote file {}'.format(file_name))
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

    def read_audio_data_chunk(self, seconds_to_read=30):
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
        total_length = round(self.audio_file.getnframes() / self.audio_file.getframerate(), 2)
        print('Read file {}'.format(ntpath.abspath(self.file_path)))
        print(('frame rate is {}, chunk size is {}'.format(self.frame_rate, chunk_size)))
        print('total length is {} s'.format(total_length))

        while True:
            start = self.audio_file.tell()

            print('Read samples from {} to {}'.format(start, start + chunk_size))
            samples = self.audio_file.readframes(chunk_size)

            print('Samples from {} to {} has been read'.format(start, self.audio_file.tell()))

            if not samples:
                print('End reading {}. Read {} frames '.format(ntpath.basename(self.file_path), self.audio_file.tell()))
                print('')
                self.audio_file.close()
                return
            print('')
            samples = self.decode_audio_chunk(samples)
            yield samples

    @staticmethod
    def decode_audio_chunk(samples):
        fmt = '<{}h'.format(len(samples) // 2)
        decoded_samples = struct.unpack(fmt, samples)
        return list(decoded_samples)
