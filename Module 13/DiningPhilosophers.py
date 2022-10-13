import time

from fork import Fork
from philosopher import Philosopher


def DiningPhilosophers():
    names = ["Plato", "Aristotle", "Buddha", "Marx", "Nietzsche"]
    # Create same number of forks per philosopher
    forks = [Fork() for _ in range(len(names))]
    philosophers = []

    i = 0
    # Create Philosopher instances of each philosopher listed
    # Assign a pair of forks to each philosopher
    for philosopher in names:
        if i == 4:
            philosophers.append(Philosopher(philosopher, forks[i], forks[0]))
            break
        philosophers.append(Philosopher(philosopher, forks[i], forks[i + 1]))

    # Start execution of philosopher threads
    for philosopher in philosophers:
        philosopher.start()

    time.sleep(10)
    # End execution of philosopher threads
    for philosopher in philosophers:
        philosopher.running = False


if __name__ == "__main__":
    DiningPhilosophers()
