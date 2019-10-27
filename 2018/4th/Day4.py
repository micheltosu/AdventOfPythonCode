import re
import datetime
from enum import Enum
class Event:
    def __init__(self, time, event_type, guard_id = None):
        self.timestamp = time
        self.event_type = event_type
        self.guard = guard_id
        

    def __repr__(self):
        return '{0} - type: {1}'.format(self.timestamp, self.event_type)

class Event_Type(Enum):
    SHIFT_START = 1
    WAKE_UP = 2
    FALL_ASLEEP = 3 


class Guard:
    def __init__(self, g_id):
        self.id = g_id
        self.events = []

    def add_event(ev):
        self.events.append(ev)

#Read the input
input_arr = open('input.txt').read().split('\n')

while input_arr[len(input_arr) - 1] == '':
    print('popping:', repr(input_arr.pop()))


# Parse events
events = list()
for event in input_arr:
    r = re.search(r'\[(\d{4})\-(\d{2})\-(\d{2}) (\d{2}):(\d{2})\]\s(.*)', event)

    time_values = r.group(1,2,3,4,5)
    time_values = map(lambda x: int(x), time_values)

    dt = datetime.datetime(*time_values)
    e_string = r.expand(r'\6')

    if '#' in e_string:
        e_type = Event_Type.SHIFT_START
        e_guard = int(re.search(r'#(\d*)', e_string).expand(r'\1'))
    elif e_string == 'wakes up': 
        e_type = Event_Type.WAKE_UP
    elif e_string == 'falls asleep':
        e_type = Event_Type.FALL_ASLEEP

    e_obj = Event(dt, e_type)
    if e_obj.event_type is Event_Type.SHIFT_START:
        e_obj.guard = e_guard
   
    events.append(e_obj)

events = sorted(events,key=lambda x: x.timestamp)

#Parse guard events
guards = dict()
for i in range(0,len(events)):
    #No active shift
    if events[i] is 

        

