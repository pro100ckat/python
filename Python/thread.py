from threading import Thread 
from random import randint 
from time import time 

number_elements = 10000
threads_count = 4 
finish_sum = 0 

def make_start_nums(): 
    start_numbers = [0] 
    for i in range(threads_count - 1): 
        start_numbers.append(randint(start_numbers[i],start_numbers[i]+randint(round(number_elements/(threads_count*2)),round(number_elements/threads_count)))) 
        start_numbers.append(number_elements) 
    return start_numbers 

sn = make_start_nums() 

def calculate(sp, part): 
    sum = 0 
    for i in range(sn[part], sn[part+1]): 
        sum += sp[i] 
    global finish_sum
    finish_sum = 0 
    finish_sum += sum 
    return sum 

def make_sp(n): 
    sp = [] 
    for i in range(n): 
        sp.append(randint(0,100)) 
    return sp 


sp = make_sp(number_elements) 
sp2 = sp 
start_time = time() 


thread1 = Thread(target=calculate, args=(sp, 0)) 
thread2 = Thread(target=calculate, args=(sp, 1)) 
thread3 = Thread(target=calculate, args=(sp, 2)) 
thread4 = Thread(target=calculate, args=(sp, 3)) 
#thread5 = Thread(target=calculate, args=(sp, 4)) 
#thread6 = Thread(target=calculate, args=(sp, 5)) 
#thread7 = Thread(target=calculate, args=(sp, 6)) 
#thread8 = Thread(target=calculate, args=(sp, 7)) 

thread1.start() 
thread2.start() 
thread3.start() 
thread4.start() 
#thread5.start() 
#thread6.start() 
#thread7.start() 
#thread8.start() 

thread1.join() 
thread2.join() 
thread3.join() 
thread4.join() 
#thread5.join() 
#thread6.join() 
#thread7.join() 
#thread8.join() 

print("Sum of odd elements: ", finish_sum) 
print("Program work time: ", time() - start_time)
