# 1
import time

class Trafficlight:
    __color = ['красный', 'жёлтый', 'зеленый']
    def running(self):
        i = 0
        while i < 3:
            print(f'Сигнал светофора: {Trafficlight.__color[i]}')
            if i == 0 or 2:
                time.sleep(7)
            else:
                time.sleep(2)
            i += 1
tr1 = Trafficlight()
tr1.running()
# 2
class Road:
    depth = 5
    kg_per_depth = 25
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
    def asphalt_mass(self,_length, _width):
        mass = _length*_width*self.depth*self.kg_per_depth/1000
        return mass
r = Road(20,5000)
print(r.asphalt_mass(20,5000))
# 3
class Worker:
    def __init__(self,name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name,surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Полное имя: {self.name} {self.surname}')
    def get_total_income(self):
        inc = self.income.get('wage') + self.income.get('bonus')
        return inc
Pos1 = Position("Иван", "Иванов", 'стажер', 10000, 5000)
Pos1.get_full_name()
print(Pos1.get_total_income())

# 4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'Машина {self.name} поехала')
    def stop(self):
        print(f'Машина {self.name} остановилась')
    def turn(self, direction):
        self.d = direction
        print(f'Машина {self.name} повернула на {self.d}')
    def show_speed(self):
        print(f'Скорость: {self.speed}')

class Towncar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости")
        else:
            print(f'Скорость: {self.speed}')
class Workcar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости")
        else:
            print(f'Скорость: {self.speed}')
class Sportcar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def speed_test(self):
        if self.speed > 220 and self.is_police is True:
            print(f'Машина {self.name} прошла тест для спец отряда ДПС')
        elif self.speed < 220 and self.is_police is True:
            print(f'Машина {self.name} НЕ прошла тест для спец отряда ДПС')
        else:
            print(f'Машина {self.name} не тестируется для ДПС')
class Policecar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = True
    def alarm(self):
        print(f'Полицейская машина {self.name} включила сигнализацию')
c = Car(120,'красный','опель', False)
c.go()
c.turn("лево")
c.show_speed()
c.stop()
c.show_speed()
t = Towncar(100,'белый','мерседес', False)
t.show_speed()
w = Workcar(50, 'синий', 'джип', False)
w.show_speed()
ss = Sportcar(250,'белый','мерседес', False)
ss.speed_test()
ss1 = Sportcar(250,'белый','мерседес', True)
ss1.speed_test()
ss2 = Sportcar(200,'белый','мерседес', True)
ss2.speed_test()
pp = Policecar(250,'белый','мерседес', False)
pp.show_speed()
pp.alarm()

# 5

class Stationery:
    def __init__(self,title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

stat = Stationery("новый")
stat.draw()

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Начинаем использовать ручку с именем: {self.title}')
pen1 = Pen('красный')
pen1.draw()

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Начинаем использовать карандаш с именем: {self.title}')
penс1 = Pencil('синий')
penс1.draw()

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Отрисовка маркером с именем: {self.title}')
еее = Handle('розовый')
еее.draw()