import os
import sys
import logging

class WaveFileSearcher:
    def find_wave_files(self, ):
        path = self._get_path_from_cmd()
        wave_files_paths = []
        if os.path.isfile(path):
            wave_files_paths.append(path)
        elif os.path.isdir(path):
            path_content = os.listdir(path)
            wave_files_paths = [path for path in path_content if '.wav' in path]
        else:
            logging.error('there is no valid path')
        return wave_files_paths

    def _get_path_from_cmd(self, ):
        try:
            path = sys.argv[1]
        except IndexError:
            logging.error('please enter path to wave files')
            raise
        return path
