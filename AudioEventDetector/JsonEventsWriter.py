import json


class JsonEventsWriter:
    def __init__(self, organised_events, file_name, destination_directory):
        self.organised_events = organised_events
        self.file_name = file_name
        self.destination_directory = destination_directory

    def create_events_in_json(self, ):
        events_for_json = {'All_Events': len(self.organised_events)}
        count = 1
        for event in self.organised_events:
            start, end, length = event
            events_for_json['Event_{}'.format(count)] = {'start': start, 'end': end, 'length': length}
            count += 1
        # events_for_json["File_name": '{}'.format(self.file_name)]
        json_events = json.dumps(events_for_json)
        return json_events

    def save_json_to_file(self,):
        json_events = self.create_events_in_json()
        json_file_name = '{}_events.json'.format(self.file_name.replace('.wav', '').replace('.WAV', ''))
        json_file_path = '{}/{}'.format(self.destination_directory, json_file_name)
        with open(json_file_path, 'w') as json_file:
            json_file.write(json_events)
        print('JSON file with events has been saved to: {}'.format(json_file_path))
        print('')



