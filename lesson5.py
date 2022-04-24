# 1
f = open(r'D:\Таня\GB системный аналитик\pythonProject\test.txt', 'w', encoding='utf-8')
while True:
        line = input("Введите текст :")+"\n"
        if line == '\n':
            break
        else:
            f.writelines(line)
f.close()
f = open(r'D:\Таня\GB системный аналитик\pythonProject\test.txt', 'r', encoding='utf-8')
f_f = f.readlines()
print(f_f)

# 2
f = open(r'D:\Таня\GB системный аналитик\pythonProject\l5_file', 'r', encoding='utf-8')
text = f.readlines()
n_row = len(text)
print(n_row)
for el in text:
    print("В элементе ", el, "слов : ", len(el.split()))
f.close()
# 3
from statistics import mean
s_f = open(r'salary3', 'r', encoding='utf-8')
li = s_f.readlines()
sal = []
for el in li:
    li2 = el.split()
    sal.append(li2[1])
sal_fl = map(float, sal)
print("Средняя зарплата равна: ", round(mean(sal_fl),2))

small_sal = []
for el in li:
    if float(el.split()[1]) < 20000:
        small_sal.append(el.split()[0])
print('Зарплата ниже 20000 руб.:', small_sal)

s_f.close()

# 4
translate = {'One': 'Один', "Two": 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open (r'1234','r', encoding='utf-8') as f:
    content = f.readlines()
    new_content = []
    for el in content:
        li = el.split()
        new_content.append((translate[li[0]])+li[1]+li[2]+"\n")
print(new_content)
with open (r'1234_rus','w', encoding='utf-8') as ff:
    ff.writelines(new_content)
# 5
with open (r'sum_num.txt','w+', encoding='utf-8') as fff:
    new = [i for i in range(10, 43) if i % 2 ==0 or i % 3 == 0]
    f1 = ""
    for i in new:
        f1 += str(i) + " "
    fff.write(f1)
    fff.seek(0)
    cont = fff.read().split()
    cont_num = list(map(int, cont))
    print((sum(cont_num)))

# 6
import re
with open (r'D:\Таня\GB системный аналитик\pythonProject\6_dict','r', encoding='utf-8') as my_f:
    new = my_f.readlines()
    plan = {}
    for el in new:
        li = el.split()
        str_ = " ".join(map(str,li))
        num = re.findall(r'\d+', str_)
        num_n = list(map(int, num))
        plan[li[0]] = sum(num_n)
    print(plan)
