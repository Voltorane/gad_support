import numpy as np
from numpy.lib.function_base import insert

class Record:
    def __init__(self, element, probe_position):
        self.element = element
        self.probe_position = probe_position
    def __repr__(self) -> str:
        return f'{self.element} : {self.probe_position}'
        

table = list()
for i in range(11):
    table.append(0)

def get_location(record):
    if record.probe_position % 2 == 0:
        return (record.element + (int)(record.probe_position/2))%11
    else:
        return (11 + record.element - ((int)(record.probe_position/2)+1))%11


def ins(element):
    record = Record(element, 0)
    while True:
        location = get_location(record=record)
        if table[location] == 0:
            table[location] = record
            return
        if table[location].probe_position < record.probe_position:
            tmp = table[location]
            table[location] = record
            record = tmp
        record.probe_position += 1

ins(67)
print(table)
ins(47)
print(table)
ins(57)
print(table)
ins(25)
print(table)
ins(56)
print(table)
ins(58)
print(table)