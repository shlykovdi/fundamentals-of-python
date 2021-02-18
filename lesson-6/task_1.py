from enum import Enum
import threading


class Color(Enum):
    NONE = 0
    RED = 1
    YELLOW = 2
    GREEN = 3


class TrafficLight:
    def __init__(self):
        self.__color = Color.NONE
        self.__selector = {
            Color.NONE: (Color.RED, 7),
            Color.RED: (Color.YELLOW, 2),
            Color.YELLOW: (Color.GREEN, 5),
            Color.GREEN: (Color.RED, 7)
        }

    def running(self):
        self.__color, seconds = self.__selector[self.__color]
        print(f'Traffic light color: {self.__color}')
        threading.Timer(seconds, self.running).start()


traffic_light = TrafficLight()
traffic_light.running()
