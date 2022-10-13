import random
import threading
import time

from fork import Fork


class Philosopher(threading.Thread):
    running = True

    def __init__(self, name: str, left_fork: Fork, right_fork: Fork):
        # Call 'threading' superclass constructor, set daemon to True
        # Allows thread to close without full completion
        super(Philosopher, self).__init__(daemon=True)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        """ Called by start(), starts the thread, runs until running = False
        """
        while self.running:
            self.think()
            self.eat()
            print(f"{self.name} is cleaning up.")

    def think(self):
        """Make philosopher think for a random number of seconds"""
        thinking = random.uniform(3, 5)
        print(f"{self.name} is thinking for {thinking} seconds.")
        time.sleep(thinking)
        print(f"{self.name} is now hungry.")

    def eat(self):
        """Attempt to acquire two forks
        If successful, eat for 3-5 seconds, then release both forks.
        If unsuccessful, go back to thinking
        """
        if self.left_fork.acquire_fork():
            if self.right_fork.acquire_fork():
                eating = random.uniform(3, 5)
                print(f"{self.name} is eating for {eating} seconds.")
                time.sleep(eating)
                self.right_fork.release_fork()
                print(f"{self.name} has put down his right fork.")
            self.left_fork.release_fork()
            print(f"{self.name} has put down his left fork.")
        else:
            return
