# https://pythonworld.ru/numpy/4.html модуль numpy.linalg, позволяющий делать многие операции из линейной алгебры
# Первоисточник функции http://python.su/forum/topic/28267/

#-------------------------------------------------------------------------------------------
import re #для re.findall - для поиска в строке, возращает список всех найденных совпадений


def myGauss(m):
    #eliminate columns
    for col in range(len(m[0])):
        for row in range(col+1, len(m)):
            r = [(rowValue * (-(m[row][col] / m[col][col]))) for rowValue in m[col]]
            m[row] = [sum(pair) for pair in zip(m[row], r)]
    #now backsolve by substitution
    ans = []
    m.reverse() #makes it easier to backsolve
    for sol in range(len(m)):
            if sol == 0:
                ans.append(m[sol][-1] / m[sol][-2])
            else:
                inner = 0
                #substitute in all known coefficients
                for x in range(sol):
                    inner += (ans[x]*m[sol][-2-x])
                #the equation is now reduced to ax + b = c form
                #solve with (c - b) / a
                ans.append((m[sol][-1]-inner)/m[sol][-sol-2])
    ans.reverse()
    return ans


first_file = 'input.txt' #входной файл
second_file = 'output.txt' #выходной файл

matrix = [] #создаем пустой массив
lines = 0   #обнуляем счетчик для строк по файлу

f1 = open(first_file)
for line in f1:
    lines += 1
    m = []
    for x in re.findall(r'-?\d*\.?\d+', line): #исключает из строки все лишние символы
        m.append(float(x)) #Добавляет в локальный массив исключаемый символ с преобразованием его в числовой тип данных 
    matrix.append(m) #добавляет в матрицу данные из локальной матрицы
    
print(matrix)

result = myGauss(matrix)

print("Ответ: " + str(result))

f2 = open(second_file, 'w')
for i in result:
    f2.write(str(i) + '\n')
f2.close()
f1.close()
