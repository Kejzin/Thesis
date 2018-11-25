import os
import sys
import logging


class WaveFileSearcher:
    def find_wave_files_paths(self, ):
        """
        Find wave files under path given in cmd. Path can be file or directory.
        Returns
        -------
            wave_files_paths: [str]
                list of strings wave files path
        """
        path = self._get_path_from_cmd()
        wave_files_paths = []
        if os.path.isfile(path):
            wave_files_paths.append(path)
        elif os.path.isdir(path):
            path_content = os.listdir(path)
            wave_files_paths = ["{}/{}".format(path, file_path) for file_path in path_content if '.wav' in file_path
                                and "REFERENCE" not in file_path]
            reference_file_path = ["{}/{}".format(path, file_path) for file_path in path_content
                                   if file_path == "REFERENCE.wav"]
        else:
            logging.error('{} is no valid path'.format(path))
            raise FileNotFoundError('{} is not a valid path'.format(path))
        assert wave_files_paths, 'there is no any wave file under given path'
        wave_files_and_reference_paths = (wave_files_paths, reference_file_path)
        return wave_files_and_reference_paths

    def _get_path_from_cmd(self, ):
        """
        get firs argument from cmd. In use case it should be wave files path
        Returns
        -------
            path: str
                first argument from cmd, should be path to wave files
        """
        try:
            path = sys.argv[1]
        except IndexError:
            logging.error('Path not entered. Please enter path to wave files')
            sys.exit()
        return path

# TODO find reference wave and compute dB SPL.
