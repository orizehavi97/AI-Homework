import threading
import time
import random
from concurrent.futures import ThreadPoolExecutor


# Step 1
def print_sequence(name, count):
    for i in range(count + 1):
        print(f"Thread {name}: i={i}")
        time.sleep(0.3)


thread1 = threading.Thread(target=print_sequence, args=("Alpha", 5))
thread2 = threading.Thread(target=print_sequence, args=("Beta", 3))
thread3 = threading.Thread(target=print_sequence, args=("Gamma", 4))
threads = [thread1, thread2, thread3]

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Step 1 complete")

# Step 2
with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(print_sequence, "Alpha", 5)
    executor.submit(print_sequence, "Beta", 3)
    executor.submit(print_sequence, "Gamma", 4)

print("Step 2 complete")

# Bonus
names = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon",
         "Zeta", "Eta", "Theta", "Iota", "Kappa"]
number_of_tuples = random.randint(5, 10)
tuples = []
for _ in range(number_of_tuples):
    name = random.choice(names)
    names.remove(name)
    cnt = random.randint(2, 6)
    tuples.append((name, cnt))

print(f"Running {len(tuples)} random tuples:\n", tuples, "\n")

with ThreadPoolExecutor(max_workers=4) as executor:
    for name, cnt in tuples:
        executor.submit(print_sequence, name, cnt)

print("All threads completed!")
