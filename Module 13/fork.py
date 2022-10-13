import threading


class Fork:
    def __init__(self):
        self._lock = threading.Lock()

    def acquire_fork(self):
        """Return True if you can acquire self.lock, False otherwise"""
        if self._lock.acquire():
            return True
        else:
            return False

    def release_fork(self):
        """Release lock on fork"""
        self._lock.release()
