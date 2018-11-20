from Sample_dB_converter import SamplesConverter

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
