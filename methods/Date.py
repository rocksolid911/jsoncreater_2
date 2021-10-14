# def Date(min, max, format):
#     assert 'ToDo: must be implement!'
#
import time

from random import seed, randint
from datetime import datetime


class DateTimeGenerator:
    format: str
    randomize_lower: int
    randomize_upper: int

    def __init__(self, formatt="%Y-%m-%dT%H:%M:%SZ", randomize_lower=0, randomize_upper=0):
        self.format = formatt
        self.randomize_upper = randomize_upper
        self.randomize_lower = randomize_lower

    def get_val(self):
        seed()
        random_range = randint(0, (self.randomize_upper - self.randomize_lower))
        mytime = time.time() + self.randomize_lower + random_range
        return datetime.fromtimestamp(mytime).strftime(self.format)
