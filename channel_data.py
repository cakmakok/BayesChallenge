class ChannelData:
    def __init__(self, last_average=None, first_average=None, last_majority=None, first_majority=None, *args, **kwargs):
        self._last_average = last_average
        self._first_average = first_average
        self._last_majority = last_majority
        self._first_majority = first_majority

    def update(self, average, majority, *args, **kwargs):
        if not self._first_average:
            self._first_average = average
        self._last_average = average

        if not self._first_majority:
            self._first_majority = majority
        self._last_majority = majority

    def get_average(self, reverse):
        return self._first_average if reverse else self._last_average

    def get_majority(self, reverse):
        return self._first_majority if reverse else self._last_majority
