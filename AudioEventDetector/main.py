from WaveReader import WaveReader, WaveWriter
from WaveFileSearcher import WaveFileSearcher
from Sample_dB_converter import SamplesConverter
from PlotsMaker import Plotter
from Detectors import ThresholdCrossDetector
from Detectors import EventsOrganiser

if __name__ == '__main__':
    wave_file_searcher = WaveFileSearcher()
    wave_files = wave_file_searcher.find_wave_files_paths()
    print('[main]')
    print('wave files: {}'.format(wave_files))
    for file in wave_files:
        print('[main;for]{}'.format(file))
        samples_converter = SamplesConverter(file)
        # all_samples = samples_converter.convert_all_file_samples()
        # print('I have {} samples with are {}'.format(len(all_samples), type(all_samples)))
        plotter = Plotter()
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
        print('event lenghts {}'.format(EventsOrganiser.organise_events(events)))
        organised_events = EventsOrganiser.organise_events(events)
        print('i found {} events'.format(len(events)))
        wave_file_writer = WaveWriter()
        count = 0
        for event in organised_events:
            count += 1
            frames = wave_file_writer.read_defined_frames(file, event)
            wave_file_writer.write_defined_frames('{}_{}.wav'.format(file.replace('.wav', ''), count), frames)
        print('tadam')
    print("JUUUUUUUUUUUHUUUUUUUUUUUU")



