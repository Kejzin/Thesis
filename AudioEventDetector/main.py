from WaveReader import WaveReader, WaveWriter
from WaveFileSearcher import WaveFileSearcher
from Sample_dB_converter import SamplesConverter
from PlotsMaker import Plotter
from Detectors import ThresholdCrossDetector
from Detectors import EventsOrganiser


def find_events():
    global events
    samples_gen = samples_converter.convert_samples()
    events_generator = ThresholdCrossDetector.count_occurrence(-25)
    events = []
    while True:
        try:
            samples = next(samples_gen)
        except StopIteration:
            break
        next(events_generator)
        events += events_generator.send(samples)
    return events


if __name__ == '__main__':
    wave_file_searcher = WaveFileSearcher()
    wave_files = wave_file_searcher.find_wave_files_paths()
    for file in wave_files:
        samples_converter = SamplesConverter(file)
        plotter = Plotter()
        events = find_events()
        organised_events = EventsOrganiser.organise_events(events)
        print('i found {} events'.format(len(organised_events)))
        wave_file_writer = WaveWriter()
        count = 0
        print(file)
        for event in organised_events:
            count += 1
            frames = wave_file_writer.read_defined_frames(file, event)
            wave_file_writer.write_defined_frames('{}_{}.wav'.format(file.replace('.wav', ''), count), frames)
        print('tadam')
    print("JUUUUUUUUUUUHUUUUUUUUUUUU")



