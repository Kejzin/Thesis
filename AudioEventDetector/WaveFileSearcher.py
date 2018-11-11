import os


class WaveFileSearcher:
    @property
    def find_wave_file(self,):
        path = self.get_path_from_cmd()
        if os.path.isfile(path):
            wave_files_paths = path
        elif os.path.isdir(path):
            path_content = os.listdir(path)
            wave_files_paths = [path for path in path_content if '.wav' in path]
        else:
            logging.info('there is no valid path')
        return wave_files_paths

    def get_path_from_cmd(self,):
        pass