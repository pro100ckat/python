import psycopg2  # Import library postgres
from prettytable import PrettyTable
import sys
import datetime
flag = True
try:
    print("Connecting to database..")
    conn = psycopg2.connect("host=" + "localhost" + " port=" + "5432" + " dbname=" + "test" + " user=" + "postgres" + " password=" + "10217200")
    print("Connected!\n")
except psycopg2.ProgrammingError:
    print("Connection error.")
    flag = False


def show_drivers(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM drivers")  # Selecting all columns from table seller
    row = cursor.fetchone()
    table = PrettyTable(('id_drivers','number_drivers','drivers_name','category','stage','adress','driving_year'))
    while row is not None:  # Fetching row
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table

def insert_drivers(conn):
    cursor = conn.cursor()
    number = input("Input number drivers: ")
    name = input("Input name: ")
    category = input("Input category: ")
    stage = input("Input hstager: ")
    adress = input("Input sadress ")
    year = input("Input year ")
    sql = "INSERT INTO PUBLIC.\"drivers\"(\"number_drivers\", \"drivers_name\", \"category\", \
    \"stage\", \"adress\", \"drivers_year\") VALUES (%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, (number, name, category, stage, adress, year))
    conn.commit()


def edit_drivers(conn):
    new_id = input("Input firm ID you want to edit - ")
    number = input("Input number drivers: ")
    name = input("Input name: ")
    category = input("Input category: ")
    stage = input("Input hstager: ")
    adress = input("Input sadress ")
    year = input("Input year ")
    cursor = conn.cursor()
    sql = "UPDATE PUBLIC.\"drivers\" SET \"number_drivers\" = %s, \"drivers_name\" =%s, category=%s, stage,adress,drivers_year=%s WHERE \"id_drivers\" = \'{}\'".format(
        new_id)
    cursor.execute(sql, (number, name, category, stage, adress, datetime(year)))
    conn.commit()

def delete_drivers(conn):
    try:
        cursor = conn.cursor()
        deleteid = int(input("Input ID of drivers you want to DELETE - "))
        cursor = conn.cursor()
        sql = "DELETE FROM PUBLIC.\"drivers\" WHERE \"id_drivers\" = \'{}\' ".format(deleteid)
        cursor.execute(sql)
        conn.commit()
        print("Succefull deleting")
    except psycopg2.IntegrityError:
        print("You need to delete orders!")
        sys.exit()



def show_cars(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cars")  # Selecting all columns from table seller
    row = cursor.fetchone()
    table = PrettyTable(('id_cars','number_cars','mark','probeg','gruz'))
    while row is not None:  # Fetching row
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table

def delete_cars(conn):
    try:
        cursor = conn.cursor()
        deleteid = int(input("Input ID of cars you want to DELETE - "))
        cursor = conn.cursor()
        sql = "DELETE FROM PUBLIC.\"cers\" WHERE \"id_cars\" = \'{}\' ".format(deleteid)
        cursor.execute(sql)
        conn.commit()
        print("Succefull deleting")
    except  psycopg2.IntegrityError:
        print("You need to delete orders!")
        sys.exit()

def edit_cars(conn):
    cursor = conn.cursor()
    new_id = input("Input provider ID you want to edit - ")
    number = input("Input number_cars: ")
    mark = input("Input mark: ")
    probeg = input("Input probeg")
    gruz = input("Input gruz: ")
    cursor = conn.cursor()
    sql = "UPDATE PUBLIC.\"cars\" SET \"number_cars\" = %s, \"mark\" =%s, probeg=%s, gruz=%s WHERE \"id_cars\" = \'{}\'".format(new_id)
    cursor.execute(sql, (number, mark, probeg, gruz))
    conn.commit()

def insert_cars(conn):
    cursor = conn.cursor()
    number = input("Input number_cars: ")
    mark = input("Input mark: ")
    probeg  = input("Input probeg")
    gruz = input("Input gruz: ")
    sql = "INSERT INTO PUBLIC.\"cars\"(\"number_cars\", \"mark\", \"probeg\", \
    \"gruz\") VALUES (%s,%s,%s,%s)"
    cursor.execute(sql, (number, mark, probeg, gruz))

def show_orders(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")  # Selecting all columns from table seller
    row = cursor.fetchone()
    table = PrettyTable(('id','date_z','orders_name','orders_nubmer_cars','km','massa','price','orders_id_cars','orders_id_drivers'))
    while row is not None:  # Fetching row
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table

def insert_orders(conn):
    cursor = conn.cursor()
    data = input("Input date: ")
    name = input("Input orders_name ")
    cars = input("Innput orders_nubmer_cars: ")
    km = input("Input km: ")
    massa = input("Input massa: ")
    price = input("Input price ")
    id_cars= input("Input id_cars ")
    orders_id_drivers = input("Input orders_id_drivers ")
    sql = "INSERT INTO PUBLIC.\"orders\"(\"date_z\", \"orders_nubmer_cars\", \"category\", \
    \"km\", \"adress\", \"massa\", \"price\", \"orders_id_cars\", \"orders_id_drivers\") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, (data, name, cars, km, massa, price, id_cars, orders_id_drivers))
    conn.commit()


def delete_orders(conn):
         deleteid = int(input("Input ID of orders you want to DELETE - "))
         cursor = conn.cursor()
         sql = "DELETE FROM PUBLIC.\"orders\" WHERE \"id\" = \'{}\' ".format(deleteid)
         cursor.execute(sql)
         conn.commit()
         print("Succefull deleting")
def edit_orders(conn): ###############################################################3
    cursor = conn.cursor()
    new_id = input("Input provider ID you want to edit - ")
    data = input("Input date: ")
    name = input("Input orders_name ")
    cars = input("Innput orders_nubmer_cars: ")
    km = input("Input km: ")
    massa = input("Input massa: ")
    price = input("Input price ")
    id_cars = input("Input id_cars ")
    orders_id_drivers = input("Input orders_id_drivers ")
    cursor = conn.cursor()
    sql = "UPDATE PUBLIC.\"orders\" SET \"date_z\" = %s,  \"orders_name\" =%s, \"orders_number_cars\" =%s, \"km=%s\", \"massa=%s\", \"price=%s\", \"orders_id_cars=%s\",\"orders_id_drivers=\"%s WHERE \"id\" = \'{}\'".format(new_id)
    cursor.execute(sql, (data, name, cars, km,massa, price, id_cars, orders_id_drivers))
    conn.commit()







#по указанному водителю – перечень выполненных заказов за указанный период;
def zap1(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, date_z, orders_name, orders_number_cars, km, massa, price, orders_id_cars, orders_id_drivers FROM PUBLIC.cars, public.orders\
    where date_z BETWEEN '2012-01-05 00:00:00' AND '2018-06-06 00:00:00' AND orders_name = 'Толя'\
    GROUP BY id")
    row = cursor.fetchone()
    table = PrettyTable(('id', 'date_z', 'orders_name', 'orders_number_car', 'km', 'massa', 'price', 'orders_id_cars', 'orders_id_drivers'))
    while row is not None:
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table
#по указанной машине – общий пробег и общую массу перевезенных грузов;
def zap2(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id_cars, mark, probeg, sum(orders.km),sum(massa) FROM PUBLIC.cars, public.orders\
    where id_cars=orders_id_cars and id_cars='2'\
    GROUP BY id_cars")
    row = cursor.fetchone()
    table = PrettyTable(('id', 'Марка', 'Пробег', 'км заказа', 'масса грузов' ))
    while row is not None:
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table

def zap3(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT drivers_name, SUM(price)*0.2 AS price, SUM(massa) AS massa, COUNT(drivers_name) AS km FROM PUBLIC.drivers, public.orders\
    where date_z BETWEEN '2012-01-05 00:00:00' AND '2018-06-06 00:00:00' AND orders_name = 'Толя'\
    GROUP BY drivers_name")
    row = cursor.fetchone()
    table = PrettyTable(('Имя', 'Заработанные деньги', 'общая масса перевезенных грузов', 'Кол-во поездок'))
    while row is not None:
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table

#•	по автомашине с наибольшим общим пробегом – все сведения.
def zap4(conn):
    cursor = conn.cursor()
    cursor.execute(" SELECT * FROM public.cars\
    WHERE probeg = (SELECT MAX(probeg) FROM public.cars)")
    row = cursor.fetchone()
    table = PrettyTable(('id', 'Номер', 'Марка', 'Пробег', 'Грузоподьемность'))
    while row is not None:
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table

#•	Агрегатная функция COUNT: подсчитать количество одинаковых марок.
def zap5(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT Mark, COUNT(*) FROM Cars\
    GROUP BY Mark;")
    row = cursor.fetchone()
    table = PrettyTable(('Марка', 'Количество'))
    while row is not None:
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table

#COUNT 2
def zap6(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT Mark, probeg, COUNT(*) FROM Cars\
    GROUP BY Mark, probeg")
    row = cursor.fetchone()
    table = PrettyTable(('Марка', 'Пробег', 'Выч'))
    while row is not None:
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table


#AVG
def zap7(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT category, AVG(stage) FROM Drivers\
    GROUP BY Category")
    row = cursor.fetchone()
    table = PrettyTable(('Категория', 'Средний стаж'))
    while row is not None:
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table

#Самый младший водитель
def zap8(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT drivers_name, drivers_year FROM Drivers\
    WHERE drivers_year = (SELECT MAX(drivers_year) from Drivers);")
    row = cursor.fetchone()
    table = PrettyTable(('Имя', 'ДР'))
    while row is not None:
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table

#Общий пробег марки
def zap9(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT Mark, SUM(probeg) FROM Cars\
    GROUP BY Mark;")
    row = cursor.fetchone()
    table = PrettyTable(('Марка', 'Сумма пробега'))
    while row is not None:
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table


#5.Создать запрос: вывести всех водителей, у которых в таблице заказов масса груза от 50 до 120, стоимость перевозки меньше 4000, километраж больше 10
def zap10(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT drivers.* FROM drivers\
    JOIN orders ON Drivers.drivers_name = orders.orders_name\
    WHERE orders.massa BETWEEN 10 AND 120\
    AND orders.price < 4000\
    AND orders.km > 10")
    row = cursor.fetchone()
    table = PrettyTable(('ID', 'Номер', 'Имя','Категоия','Стаж','Адрес','Год рождения'))
    while row is not None:
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table


print(zap10(conn))
conn.close()


