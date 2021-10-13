import threading
import time


class Phil(threading.Thread):
    
    flag = True

    def __init__(self, index, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while self.flag is True:
            time.sleep(10)
            print(f'Philosopher {self.index} is hungry.')
            self.swap()
        print(f'\033[2;31;43m Philosopher {self.index} is out of table. \033[0;0m')

    def swap(self):
        fork1, fork2 = self.left_fork, self.right_fork
        while self.flag:
            fork1.acquire()
            locked = fork2.acquire(False)
            if locked:
                break
            fork1.release()
            print(f'Philosopher {self.index} swaps forks.')
            fork1, fork2 = fork2, fork1
        else:
            return
        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        print(f'Philosopher {self.index} begins eating.')
        time.sleep(10)
        print(f'Philosopher {self.index} finishes eating and leaves to think.')


forks = [threading.Semaphore() for n in range(5)]
phils = [Phil(i, forks[i % 5], forks[(i + 1) % 5]) for i in range(5)]
Phil.flag = True
for p in phils:
    p.start()
time.sleep(50)
Phil.flag = False
print("\033[2;31;43m Stopping processes... \033[0;0m")
