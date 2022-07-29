#Массивы
cities = ['New York', 'Moscow', 'SPB', 'Tyla']

print(cities)

print(len(cities)) #длина массива

print(cities[0]) #вывод 0 элемента
print(cities[-2].upper) #вывод с конца

cities[2] = 'Banaul'
print(cities)

cities.append('Kursk')
print(cities)

cities.insert(1, 'Feodos')
print(cities)

del cities[-2]
print(cities)

cities.remove('Kursk')
print(cities)

deleted_city = cities.pop()
print("deleted city is " + deleted_city)
cities.sort(reverse=True)
print(cities)

cities.reverse()
print(cities)

for i in cities:
    print(i + " ")
    
mylist = list(range(0, 10))
print(mylist)

for i in mylist:
    i = i*2
    print(i)
mylist.sort(reverse = True)
print(mylist)

print("max = " + str(max(mylist)))
print(min(mylist))
print(sum(mylist))

newc = cities[0:2] #от какого индекса сколько добавить включая его 
print(newc)
newx2 = cities[:] # скопировать массив
print(newx2)

