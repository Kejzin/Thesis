import os
import sys
import logging


class WaveFileSearcher:
    def find_wave_files_paths(self, ):
        """
        Find wave files under path given in cmd.
        return:
            wave_files_paths([str]) list of strings wave files path
        """
        path = self._get_path_from_cmd()
        wave_files_paths = []
        if os.path.isfile(path):
            wave_files_paths.append(path)
        elif os.path.isdir(path):
            path_content = os.listdir(path)
            wave_files_paths = [path for path in path_content if '.wav' in path]
        else:
            logging.error('{} is no valid path'.format(path))
            raise FileNotFoundError('{} is not a valid path'.format(path))
        assert wave_files_paths, 'there is no any wave file under given path'
        return wave_files_paths

    def _get_path_from_cmd(self, ):
        """
        get firs argument from cmd. In use case it should be wave files path
        return:
            path(str): first argument from cmd, should be path to wave files
        """
        try:
            path = sys.argv[1]
        except IndexError:
            logging.error('Path not entered. Please enter path to wave files')
            sys.exit()
        return path

# TODO find reference wave and compute dB SPL.
