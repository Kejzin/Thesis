class EventsOrganiser:
    @staticmethod
    def organise_events(events, time_constant):
        """Search in events list and prepare easy to use list of touples.
        Parameters
        ----------
            events: [(float, float)]
                List of two element touples. Must contain list of all events to organise, where first value of every
                touple is value of sample, second is number of it position in file. Must contain every starts
                and endings of events(except first and last).
        Returns
        -------
            events_starts_ends_lengths: [(float, float, float)]
                List of three element touple which contains starts, endings and lengths of all founded events.
        """
        time_constant_ms = {'slow': 1,
                            'fast': 0.125}

        events_starts = [time*time_constant_ms[time_constant] for _, time in events[::2]]
        events_ends = [time*time_constant_ms[time_constant] for _, time in events[1::2]]
        events_length = []
        events_starts_ends_lengths = []
        for event_number in range(len(events_starts)):
            try:
                events_length.append(events_ends[event_number] - events_starts[event_number])
            except IndexError:
                print('there is an event which has only start')
                break
            events_starts_ends_lengths.append((events_starts[event_number],
                                               events_ends[event_number],
                                               events_length[event_number]))
        return events_starts_ends_lengths


class ThresholdCrossDetector:
    @staticmethod
    def count_occurrence(threshold, _last_previous_index=0, _found=0):
        """Detect starts and ends acoustic events. Events are all samples above threshold.
        Parameters
        ----------
            threshold: float
                Variable which defined starts and ends events. Expected value depends on yielded data.
            _last_previous_index: int
                Internal variable use for keeping memory of previous data.
            _found: int
                Internal variable use for keeping memory of founded events.
        Returns
        -------
            events: [(float, float)]
                List of touples of two parameters. First defined detected value, second number of sampel in whole file
                If use properly it keep memory of previous data.
        """
        while True:
            data = yield
            first_index_of_chunk = _last_previous_index
            _last_previous_index = len(data) + first_index_of_chunk
            events = []
            for value in data:
                if _found % 2 == 0 and value >= threshold:
                    events += [(value, data.index(value)+first_index_of_chunk)]
                    _found += 1
                    print('event started in {} sample'.format(data.index(value)+first_index_of_chunk))
                if _found % 2 != 0 and value <= threshold:
                    events += [(value, data.index(value)+first_index_of_chunk)]
                    print('event end in {} sample'.format(data.index(value)+first_index_of_chunk))
                    _found += 1
            yield events
