
from random import randint




class Tank:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.points = 100
        self.direction = 'n'
        self.directions = {'n': 'north', 's': 'south', 'e': 'east', 'w': 'west'}
        self.shoot = {'n': 0, 's': 0, 'e': 0, 'w': 0}

    def go_fowards(self):
        self.y += 1
        self.direction = 'n'
        self.points -= 10
        print('Moves forward')

    def go_backwards(self):
        self.y -= 1
        self.direction = 's'
        self.points -= 10
        print('Moves backwards')

    def turn_left(self):
        self.x -= 1
        self.direction = 'w'
        self.points -= 10
        print('Turns left')

    def turn_right(self):
        self.x += 1
        self.direction = 'e'
        self.points = -10
        print('Turns right')

    def sight(self, target_x, target_y):
        if self.x == target_x:
            if target_y > self.y and self.direction == 'n':
                return True
            elif target_y < self.y and self.direction == 's':
                return True
            return False
        if self.y == target_y:
            if target_x > self.x and self.direction == 'e':
                return True
            elif target_x < self.x and self.direction == 'w':
                return True
            return False

    def shots(self):
        self.shoot[self.direction] += 1
        self.points = -10

    def info(self):
        self.points = -10
        print('\n')
        print(f'Directions: {self.directions[self.direction]}')
        print(f'Tank coordinates: {self.x}, {self.y}')
        print(f'Shots: north: {self.shoot["n"]}, south: {self.shoot["s"]},'
              f' east: {self.shoot["e"]}, west: {self.shoot["w"]}')


class Target():
    def __init__(self, x, y):
        self.x = x
        self.y = y

tank = Tank()
target = Target(randint(-5, 6), randint(-5 ,6))

while True:
    print(f'[{tank.points}][target: {(target.x, target.y)}]\n'
          f'f - forward, b - backwards, l - left, r- right, shoot, info, end')
    choice = input('write number')
    if choice == 'f':
        tank.go_fowards()
    elif choice == 'b':
        tank.go_backwards()
    elif choice == 'l':
        tank.turn_left()
    elif choice == 'r':
        tank.turn_right()
    elif choice == 'shoot':
        tank.shots()
        if tank.sight(target.x, target.y):
            print('Hit')
            tank.points += 100
            target = Target(randint(-5, 6), randint(-5, 6))

        else:
            tank.points -= 10
            print('Missed')

    elif choice == 'info':
        tank.info()
    elif choice == 'end':
        break
    else:
        'Choice unavailable action. Try again'

