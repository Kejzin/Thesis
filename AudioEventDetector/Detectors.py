class EventsOrganiser:
    @staticmethod
    def organise_events(events):
        events_starts = [time for _, time in events[::2]]
        print('all event starts are {}'.format(events_starts))
        events_ends = [time for _, time in events[1::2]]
        print('all event ends are {}'.format(events_ends))
        events_length = []
        events_starts_ends_lengths = []
        for event_number in range(len(events_starts)):
            print(event_number)
            print('hej ho')
            try:
                events_length.append(events_ends[event_number] - events_starts[event_number])
            except IndexError:
                print('there is an event which has only start')
                break
            events_starts_ends_lengths.append((events_starts[event_number],
                                               events_ends[event_number],
                                               events_length[event_number]))
        return events_starts_ends_lengths


class TresholdCrossDetector:
    @staticmethod
    def count_occurence(treshold, last_previous_index=0, found=0):
        while True:
            data = yield
            print("I yield {}".format(data[0:5]))
            first_index_of_chunk = last_previous_index
            last_previous_index = len(data)+first_index_of_chunk
            events = []
            for value in data:
                if found % 2 == 0 and value >= treshold:
                    events += [(value, data.index(value)+first_index_of_chunk)]
                    found += 1
                    print('event started in {} s'.format(data.index(value)+first_index_of_chunk))
                if found % 2 != 0 and value <= treshold:
                    events += [(value, data.index(value)+first_index_of_chunk)]
                    print('event end in {} s'.format(data.index(value)+first_index_of_chunk))
                    found += 1
            yield events
