from WaveReader import WaveReader, WaveWriter
from WaveFileSearcher import WaveFileSearcher
from SampledBConverter import SamplesDbFsConverter, SamplesDbSPLConverter
from Detectors import ThresholdCrossDetector
from Detectors import EventsOrganiser
from JsonEventsWriter import JsonEventsWriter
import ntpath
import os
from CmdInterface import CmdInterface
from PlotsMaker import Plotter


def convert_reference_file(reference_file_path):
    reference_file_converter = SamplesDbFsConverter(reference_file_path)
    converted_samples = reference_file_converter.convert_all_file_samples()
    reference = sum(converted_samples) / len(converted_samples)
    print('')
    print()
    print(sum(converted_samples))
    print(len(converted_samples))
    print('Convert reference file return: {}'.format(reference))
    print('')
    return reference


def find_events(file_path, reference_db_fs_value):
    threshold = CmdInterface.get_threshold()
    samples_db_spl_converter = SamplesDbSPLConverter(file_path, reference_db_fs_value)
    samples_gen = samples_db_spl_converter.convert_samples()
    events_generator = ThresholdCrossDetector.count_occurrence(threshold)
    time_weighting = samples_db_spl_converter.time_weighting
    found_events = []
    samples_to_plot = []
    while True:
        try:
            samples = next(samples_gen)
            samples_to_plot += samples
        except StopIteration:
            break
        next(events_generator)
        found_events += events_generator.send(samples)
    return found_events, time_weighting


if __name__ == '__main__':
    wave_file_searcher = WaveFileSearcher()
    wave_files_paths, reference_file_path = wave_file_searcher.find_wave_files_paths()
    reference_file_path = reference_file_path[0]
    reference_db_fs_value = convert_reference_file(reference_file_path)
    for file_path in wave_files_paths:
        events, time_constant = find_events(file_path, reference_db_fs_value)
        organised_events = EventsOrganiser.organise_events(events, time_constant)
        if organised_events:
            print('Found {} events'.format(len(organised_events)))
        else:
            print('No events has been found in {}'.format(ntpath.abspath(file_path)))
        print('')
        wave_file_writer = WaveWriter()
        count = 0
        if not organised_events:
            pass
        for event in organised_events:
            count += 1
            frames_and_params = wave_file_writer.read_defined_frames(file_path, event)
            events_directory = '{}_events'.format(file_path.replace('.wav', '').replace('.WAV', ''))
            if not os.path.isdir(events_directory):
                os.makedirs(events_directory)
            wave_file_writer.write_defined_frames(events_directory,
                                                  frames_and_params,
                                                  count)
            json_writer = JsonEventsWriter(organised_events, ntpath.basename(file_path), events_directory)
            json_writer.save_json_to_file()
    print("Program ends normally.")



