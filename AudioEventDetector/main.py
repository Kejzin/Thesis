from WaveReader import WaveReader, WaveWriter
from WaveFileSearcher import WaveFileSearcher
from Sample_dB_converter import SamplesConverter
from Detectors import ThresholdCrossDetector
from Detectors import EventsOrganiser
from JSON_events_writer import JsonEventsWriter
import ntpath


def convert_reference_file(reference_file_path):
    reference_file_converter = SamplesConverter(reference_file_path)
    converted_samples = reference_file_converter.convert_all_file_samples()
    reference = sum(converted_samples) / len(converted_samples)
    return reference

def find_events(file_path, reference_db_fs_value):
    samples_converter = SamplesConverter(file_path, reference_db_fs_value)
    samples_gen = samples_converter.convert_samples()
    events_generator = ThresholdCrossDetector.count_occurrence(25)
    time_weighting = samples_converter.time_weighting
    found_events = []
    while True:
        try:
            samples = next(samples_gen)
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
        events, time_constant_ms = find_events(file_path, reference_db_fs_value)
        organised_events = EventsOrganiser.organise_events(events, time_constant_ms)
        print('i found {} events'.format(len(organised_events)))
        wave_file_writer = WaveWriter()
        count = 0
        print(file_path)
        for event in organised_events:
            count += 1
            frames = wave_file_writer.read_defined_frames(file_path, event)
            wave_file_writer.write_defined_frames('{}_/{}.wav'.format(file_path.replace('.wav', ''), count), frames)
            json_writer = JsonEventsWriter(organised_events, ntpath.basename(file_path), file_path.replace('.wav', ''))

    print("End")



