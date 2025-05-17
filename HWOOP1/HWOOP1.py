import time
from datetime import datetime

class Timer:
    def __init__(self, name, duration):
        print('New timer created!')
        self.name = name
        self.duration = duration
        self.started_at = datetime.now()

    def __str__(self) -> str:
        return f"Timer '{self.name}' set for {self.duration} minutes " + \
               f"(started at: {self.started_at})"

    def __repr__(self) -> str:
        return f"Timer('{self.name}', '{self.duration}', '{self.started_at}')"

    def __del__(self):
        print(f"Timer {self.name} is being removed!")

# Create 2 new timers
timer1 = Timer("workout", 45)
timer2 = Timer("meditation", 10)

# Add a 'paused' attribute dynamically and delete it
timer1.paused = False
del timer1.paused

# Store all timers in a list and print it
timers: list[Timer] = [timer1, timer2]
print(timers)

# Clone timer1 using eval
timer3=eval(repr(timer1.__repr__()))
print(f"timer1:{timer1.__repr__()}\ntimer3:{timer3}")

# Simulate the timer running
time.sleep(1)
print(f"{(datetime.now()-timer1.started_at).seconds} seconds passed since timer1 started")
