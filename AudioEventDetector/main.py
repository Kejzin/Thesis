from WaveReader import WaveReader, WaveWriter
from WaveFileSearcher import WaveFileSearcher
from Sample_dB_converter import SamplesDbFsConverter, SamplesDbSPLConverter
from Detectors import ThresholdCrossDetector
from Detectors import EventsOrganiser
from JSON_events_writer import JsonEventsWriter
import ntpath
from PlotsMaker import Plotter


def convert_reference_file(reference_file_path):
    reference_file_converter = SamplesDbFsConverter(reference_file_path)
    converted_samples = reference_file_converter.convert_all_file_samples()
    reference = sum(converted_samples) / len(converted_samples)
    return reference


def find_events(file_path, reference_db_fs_value):
    samples_db_spl_converter = SamplesDbSPLConverter(file_path, reference_db_fs_value)
    samples_gen = samples_db_spl_converter.convert_samples()
    events_generator = ThresholdCrossDetector.count_occurrence(80)
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
    # Plotter.simple_plot(samples)
    return found_events, time_weighting


if __name__ == '__main__':
    wave_file_searcher = WaveFileSearcher()
    wave_files_paths, reference_file_path = wave_file_searcher.find_wave_files_paths()
    print(wave_files_paths)
    print(reference_file_path)
    reference_file_path = reference_file_path[0]
    reference_db_fs_value = convert_reference_file(reference_file_path)
    print("here i am before fir for!")
    for file_path in wave_files_paths:
        events, time_constant = find_events(file_path, reference_db_fs_value)
        organised_events = EventsOrganiser.organise_events(events, time_constant)
        print('i found {} events'.format(len(organised_events)))
        wave_file_writer = WaveWriter()
        count = 0
        for event in organised_events:
            count += 1
            print("DO I EVEN GO HERE? %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            frames_and_params = wave_file_writer.read_defined_frames(file_path, event)
            events_directory = '{}_events'.format(file_path.replace('.wav', '').replace('.WAV', ''))
            wave_file_writer.write_defined_frames(events_directory,
                                                  frames_and_params,
                                                  count)
            json_writer = JsonEventsWriter(organised_events, ntpath.basename(file_path), events_directory)
            json_writer.save_json_to_file()
        print("IT SHOULD NOT BE AT THE END")

    print("End")



