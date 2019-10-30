import re
import datetime
from enum import Enum

class Event_Type(Enum):
    SHIFT_START = 1
    WAKE_UP = 2
    FALL_ASLEEP = 3 

class Event:
    def __init__(self, time, event_type, guard_id = None):
        self.timestamp = time
        self.event_type = event_type
        self.guard = guard_id
    
    def __repr__(self):
        return '{0} - type: {1} - guard: {2}'.format(self.timestamp, self.event_type, self.guard)

class Guard:
    def __init__(self, g_id):
        self.id = g_id
        self.events = []
        self.sleep_time = 0
        self.most_likely_asleep = None
        self.most_likely_minute_frequency = 0
    
    def __repr__(self):
        return '<Guard, of id:{0} with {1} events'.format(self.id, len(self.events))

    def __str__(self):
        representation = 'Guard #{0}, sleep time: {1} minutes, most likely at: {2}]'.format(self.id, self.sleep_time, self.most_likely_asleep)
        if len(self.events) != 0:
            representation += "\n-------Events---------"
        for event in self.events:
            representation += '\n' + repr(event)

        return representation

    def add_event(self, ev):
        self.events.append(ev)

    # Goes through all events connected to guard, calculates 
    # the metrics we need and stores in the guard object.
    def calc_sleep_time(self):
        start_time = None
        sleeping_minutes = dict((i, 0) for i in range(0,60))

        for e in self.events:
            if e.event_type is Event_Type.FALL_ASLEEP:
                start_time = e.timestamp
            elif e.event_type is Event_Type.WAKE_UP:
                minutes_slept = int((e.timestamp - start_time).total_seconds() / 60)
                self.sleep_time += minutes_slept
                start_minute = start_time.minute
                
                # For each minute during this nap, increase the count and update
                # the most slept minute count continously.
                for i in range(0, minutes_slept):
                    minute = (start_minute + i) % 60
                    sleeping_minutes[minute] += 1
                    if sleeping_minutes[minute] > self.most_likely_minute_frequency:
                        self.most_likely_minute_frequency = sleeping_minutes[minute]
                        self.most_likely_asleep = minute

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
active_guard  = None
for i in range(0,len(events)):
    if events[i].event_type is Event_Type.SHIFT_START:
        guard_id = events[i].guard
        if guard_id not in guards:
            active_guard = Guard(guard_id)
            guards[active_guard.id] = active_guard
        else:
            active_guard = guards[guard_id]
        
    elif events[i].event_type is Event_Type.FALL_ASLEEP and active_guard is not None:
        active_guard.add_event(events[i])
        events[i].guard = active_guard.id
    elif events[i].event_type is Event_Type.WAKE_UP and active_guard is not None:
        active_guard.add_event(events[i])
        events[i].guard = active_guard.id
    else:
        raise Exception('Could not parse event:', event[i])


for gid in guards: 
    guards[gid].calc_sleep_time()

# Sort guards based on sleep time, print guard according to strategy 1
strategy1_sorted = sorted(guards.items(), key=lambda g: g[1].sleep_time, reverse = True)
guard1 = strategy1_sorted[0][1]
print('Guard id * minute chosen = {0}'.format(guard1.id * guard1.most_likely_asleep))

# Sort guards based on amount of times slept the same minute, print guard according to stragegy 2
strategy2_sorted = sorted(guards.items(), key=lambda g: g[1].most_likely_minute_frequency, reverse=True)
guard2 = strategy2_sorted[0][1]

print('Guard id * minute chosen = {0}'.format(guard2.id * guard2.most_likely_asleep))


        

