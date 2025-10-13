import json
import GetFilePath

class Data:
    def __init__(self):
        self.oGetFilePath = GetFilePath.GetFilePath()

    def load_data(self, filename):
        with open(self.oGetFilePath.load_datafile(filename=filename)) as read_file:
            self.data = json.load(fp=read_file)
        return self.data
    
    def dump_data(self, filename, data):
        with open(self.oGetFilePath.load_datafile(filename=filename), 'w') as write_file:
            json.dump(data, fp=write_file)