import random


class ReservoirSample(object):

    def __init__(self, size):
        self._size = size
        self._counter = 0
        self._sample = []

    def feed(self, item):
        self._counter += 1
        # ii <= k
        if len(self._sample) < self._size:
            self._sample.append(item)
            return self._sample
        # ii > kk / i
        rand_int = random.randint(1, self._counter)
        if rand_int <= self._size:
            self._sample[rand_int - 1] = item
        return self._sample