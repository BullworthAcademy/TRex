import random
import os
import time

load = 0.1  # 10% Smoke_x events
attempts = 10
input_rate_per_second = 100

for load in [0.1, 0.5, 0.9]:
    for i in range(attempts):
        os.system(f"java -jar TRex-client.jar localhost 50254 -pub 2626 attempt {i} scenario {load}")
        start_time = time.time()
        n_call = 0
        while time.time() - start_time < 15 or n_call == 0 < input_rate_per_second:
            n_call += 1
            temperature = round(random.uniform(0,100))
            composite_event_id = random.randint(1, 10)
            smoke_id = composite_event_id * 1000
            temp_id = composite_event_id * 1000 + 1
            if random.random() > load:
              os.system(f"java -jar TRex-client.jar localhost 50254 -pub {temp_id} area toto value {temperature}")
            else:
              os.system(f"java -jar TRex-client.jar localhost 50254 -pub {smoke_id} area toto")
            if n_call >= input_rate_per_second:
                print("über input_rate_per_second")
            if time.time() - start_time > 1:
                print(f"über Sekunden {n_call}")
        time.sleep(20)
    
    
