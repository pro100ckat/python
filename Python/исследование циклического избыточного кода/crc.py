import random

def crc(sequence):
    polynom = [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1]
    message = []
    for i in str(sequence):
        message.append(int(i))
    registr = []
    leng = len(polynom)
    i = 0
    while leng <= len(message):
        if i == 0:
            registr = message[i:len(polynom) + i]
        else:
            registr.pop(0)
            registr.append(message[len(polynom) - 1 + i])
        if registr[0] == 1:
            for j in range(0, len(registr)):
                registr[j] = registr[j] ^ polynom[j]
        i += 1
        leng += 1
    registr.pop(0)
    for i in registr:
        sequence += str(i)
    print("Check", registr)
    return sequence


def crc_find(sequence):
    polynom = [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1]
    message = []
    for i in str(sequence):
        message.append(int(i))
    for i in range(1, len(polynom)):
        message.append(0)  #Добавляем недостающие нули как в степени. В данном случае 32 бита и 32 нуля
    registr = []
    leng = len(polynom)
    i = 0
    while leng <= len(message):
        if i == 0:
            registr = message[i:len(polynom) + i]
        else:
            registr.pop(0)
            registr.append(message[len(polynom) - 1 + i])
        if registr[0] == 1:
            for j in range(0, len(registr)):
                registr[j] = registr[j] ^ polynom[j]   #Операция XOR
        i += 1
        leng += 1
    registr.pop(0)
    for i in registr:
        sequence += str(i)
    print("Find", sequence)
    return sequence



def generator():
    ran = [1]
    for i in range(0, 999):
        ran.append(random.choice([1, 0]))
    print("Gen", ran)
    znach = ""
    for i in ran:
        znach += str(i)
    return znach


if __name__ == "__main__":
    crc(crc_find(generator()))
    #crc_find('1101011011')
    #generator()