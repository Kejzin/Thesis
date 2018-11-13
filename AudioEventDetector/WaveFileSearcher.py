import os
import sys
import logging


class WaveFileSearcher:
    def find_wave_files_paths(self, ):
        """
        Find wave files under path given in cmd.
        :return: list of wave files path
        :rtype: [str]
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
        :return: string from cmd
        :rtype: str
        """
        try:
            path = sys.argv[1]
        except IndexError:
            logging.error('please enter path to wave files')
            raise
        return path
