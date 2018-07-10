import random

EB_MAX_SIZE = 10e6

class ExperienceBuffer:
    def __init__(self):
        self.size = 0
        self.data = []

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == EB_MAX_SIZE

    def add(self, new_el):
        if self.is_full():
            index = random.randrange(self.size)
            self.data[index] = new_el
        else:
            self.data.append(new_el)
            self.size += 1

    def get_batch(self, number_of_elements):
        if self.is_empty():
            raise Exception('ExperienceBuffer is empty!')
        return [self.data[random.randrange(self.size)] for i in range(number_of_elements)]

    def __str__(self):
        return str(self.data)
