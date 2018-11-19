Sample

class TresholdCrossDetector:
    def colect_data(self,):
        data_generator =
        all_samples = []
        while True:
            try:
                print(' [while]')
                try:
                    all_samples += next(converted_samples_generator)
                except ValueError as e:
                    print(e, 'but okay!')
            except StopIteration:
                print('[main:for:while]is there stop iteration?')
                break
        return all_samples