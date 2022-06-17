from abc import ABC, abstractmethod

class BasePipeline(ABC):

    @abstractmethod
    def data_collect(self):
        ...

    @abstractmethod
    def api_request(self,):
        ...

    @abstractmethod
    def create_buckets(self, *args):
        ...