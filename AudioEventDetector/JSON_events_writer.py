import json


class JsonEventsWriter:
    def __init__(self, organised_events, file_name, destination_directory):
        self.organised_events = organised_events
        self.file_name = file_name
        self.destination_directory = destination_directory

    def create_events_in_json(self, ):
        events_for_json = {}
        count = 1
        for event in self.organised_events:
            start, end, length = event
            events_for_json['Event_{}'.format(count)] = {'start': start, 'end': end, 'length': length}
            count += 1
        events_for_json["File_name": self.file_name]
        json_events = json.dumps(events_for_json)
        return json_events

    def save_json_to_file(self,):
        json_events = self.create_events_in_json()
        with open('{}/{}_events'.format(self.destination_directory, self.file_name), 'w') as json_file:
            json_file.write(json_events)



