import sys
import logging


class CmdInterface:
    @staticmethod
    def get_path_from_cmd():
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

    @staticmethod
    def get_frequency_weighting_from_cmd():
        """Read second argument from cmd which should be frequency weighting. Can be "A", "B" or "C".
        Returns:
        -------
            frequency_weighting: str
        """
        try:
            frequency_weighting = sys.argv[2]
            if frequency_weighting not in ['A', 'B', 'C']:
                raise ValueError('frequency weighting must be "A", "B" or "C" not {}'.format(frequency_weighting))
        except IndexError as e:
            logging.error('Please enter a time weighting which can be "A", "B" or "C"')
            raise e
        return frequency_weighting

    @staticmethod
    def get_time_weighting_from_cmd():
        """Read third argument from cmd which should be time weighting. Can be "slow" or "fast".
        Returns:
        -------
            time_weighting: str
        """
        try:
            time_weighting = sys.argv[3]
            if time_weighting not in ['slow', 'fast']:
                raise ValueError('time weighting must be "slow" or "fast", not {}'.format(time_weighting))
        except IndexError:
            logging.error('Please enter time weighting with can be "slow" or "fast"')
            raise
        return time_weighting
    
    @staticmethod
    def get_reference_db_spl():
        """Read fourth argument from cmd which should be time reference dB SPL value.
        Returns:
        -------
            reference_db_spl: str
        """
        try:
            reference_db_spl = sys.argv[4]
            try:
                reference_db_spl = float(reference_db_spl)
            except ValueError:
                logging.error('please enter a number not {}'.format(reference_db_spl))
                raise
        except IndexError:
            logging.error('Please enter reference db spl')
            raise
        return reference_db_spl

    @staticmethod
    def get_threshold():
        """Read fifth argument from cmd which should be threshold in dB SPL.
        Returns:
        -------
            threshold: str
        """
        try:
            threshold = sys.argv[5]
            try:
                threshold = float(threshold)
            except ValueError:
                logging.error('Threshlod must be a number, not {}'.format(threshold))
                raise
        except IndexError:
            logging.error('Please enter threshold for acoustic event (in DB SPL value)')
            raise
        return threshold
