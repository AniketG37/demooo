class Processor:
    def __init__(self, name):
        self.name = name

    def process(self, data):
        print(f"{self.name} is processing: {data}")