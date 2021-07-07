#!/usr/bin/env python3
import random
import os
import time


def publish_events(seconds, load, attempts):
    for i in range(attempts):
        n_call = 0
        t_end = time.time() + seconds
        while time.time() < t_end:
            n_call += 1
            temperature = round(random.uniform(0,100))
            composite_event_id = random.randint(1, 10)
            smoke_id = composite_event_id * 1000
            temp_id = composite_event_id * 1000 + 1
            if random.random() > load:
                os.system(f"java -jar TRex-client.jar localhost 50254 -pub {temp_id} area toto value {temperature}")
            else:
                os.system(f"java -jar TRex-client.jar localhost 50254 -pub {smoke_id} area toto")
        print(f"Attempt {i+1}: {n_call/seconds} events/seconds")


if __name__ == "__main__":
    publish_events(seconds=10, load=0.9, attempts=3)
