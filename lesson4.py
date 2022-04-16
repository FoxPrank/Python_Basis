
#1
from sys import argv
def my_salary(hour, per_hour,bonus):
    salary = (hour*per_hour) + bonus
    print('Salary: ', salary)
hour, per_hour, bonus = map(int, argv[1:])
my_salary(hour, per_hour, bonus)

2
li = [333,12,17,1,1,5]
new = [li[i] for i in range(2,len(li)) if li[i]> li[i-1]]
print(new)

# 3
new = [i for i in range(20, 241) if i % 20 ==0 or i % 21 == 0]
print(new)

# 4
li = [2,2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new = [el for el in li if li.count(el) == 1]
print(new)

# 5
from functools import reduce

def multiply(a,b):
  return a*b
print(reduce(multiply, [i for i in range(100, 1001, 2)]))

# 6
from itertools import count, cycle

for i in count(3):
    print(i)
    if i == 10:
        break

i = 0
for el in cycle([1, 2, 3, 'елочка', 'гори', '!']):
    print(el)
    i+= 1
    if i == 12:
        break

# 7
import math
def func(n):
    new = (i for i in range(1,n+1))
    for el in new:
        yield math.factorial(el)

for el in func(4):
    print(el)

