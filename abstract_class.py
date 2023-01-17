from abc import ABC, abstractmethod
class Stream(ABC):
    @abstractmethod
    def read(self):
        pass

class StreamFile(Stream):
    def read(self):
        print('Reading from file')

class StreamNetwork(Stream):
    def read(self):
        print('Reading from Network')

class OtherStream(Stream):
    def read(self):
        print('reading from Other stream')

# stream = Stream().read()
# stream_file = Stream().read()
# stream_network = StreamNetwork().read()
# stream_other = OtherStream()stream_other.read()