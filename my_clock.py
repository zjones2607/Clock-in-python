import time
from datetime import datetime
from abc import ABC, abstractmethod

class TimeDisplay(ABC):
    def __init__(self, time_format="%I:%M:%S %p"):
        self._time_format = time_format 
        self.__last_displayed_time = None 

    def get_time_format(self):
        return self._time_format

    def set_time_format(self, new_format):
        self._time_format = new_format

    def get_current_time(self):
        now = datetime.now()
        current_time = now.strftime(self._time_format)
        self.__last_displayed_time = current_time
        return current_time

    def get_last_displayed_time(self):
        return self.__last_displayed_time

    @abstractmethod
    def display(self):
        """Abstract method - must be implemented by child classes."""
        pass

class ConsoleTimeDisplay(TimeDisplay):
    def display(self):
        try:
            while True:
                current_time = self.get_current_time()
                print("Current time (child):", current_time, end='\r')
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nStopped by user.")

if __name__ == "__main__":
    child_display = ConsoleTimeDisplay()
    child_display.display()
