from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    PINK = 4


class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    BACK = 3


class Car:
    def __init__(self, color, name):
        self.speed = 0.0
        self.color = color
        self.name = name
        self.is_police = False

    def go(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0.0

    def turn(self, direction: Direction):
        pass

    def show_speed(self):
        print(f'Speed: {self.speed} kmph')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60.0:
            print(f'The speed is too fast: {self.speed} kmph! Slow down to 60 kmph.')
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40.0:
            print(f'The speed is too fast: {self.speed} kmph! Slow down to 40 kmph.')
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)
        self.is_police = True


town_car = TownCar(Color.RED, 'A')
sport_car = SportCar(Color.GREEN, 'B')
work_car = WorkCar(Color.BLUE, 'C')
police_car = PoliceCar(Color.PINK, 'D')

town_car.go(50.0)
town_car.show_speed()
town_car.go(80.0)
town_car.show_speed()

work_car.go(30.0)
work_car.show_speed()
work_car.go(50.0)
work_car.show_speed()

sport_car.go(258.0)

print(f'Sport car {sport_car.name}, {sport_car.color}, {sport_car.is_police}, {sport_car.speed}')
print(f'Police car: {police_car.name}, {police_car.color}, {police_car.is_police}, {police_car.speed}')
