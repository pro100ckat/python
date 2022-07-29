import psycopg2  # Import library postgres
import postgresql
import sys
from prettytable import PrettyTable
import datetime
# Function for shows
def show_firms(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM firm")#Selecting all columns from table firm
    row = cursor.fetchone()
    table = PrettyTable(('id', 'firm', 'country', 'address', 'phone_number', 'site'))
    while row is not None: #Fetching row
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table
def show_sellers(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM seller")  # Selecting all columns from table seller
    row = cursor.fetchone()
    table = PrettyTable(('id','name','address','phone_number','experience','seller_type'))
    while row is not None:  # Fetching row
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table
def show_equipment(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM equipment")  # Selecting all columns from table seller
    row = cursor.fetchone()
    table = PrettyTable(('id','name','price','size','date', 'country','firm_id','provider_id','eq_type_id','seller_id'))
    while row is not None:  # Fetching row
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table
def show_equipment_type(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM equipment_type")  # Selecting all columns from table seller
    row = cursor.fetchone()
    table = PrettyTable(('id','type'))
    while row is not None:  # Fetching row
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table
def show_provider(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM provider")  # Selecting all columns from table seller
    row = cursor.fetchone()
    table = PrettyTable(('id','name','country','address','phone_number'))
    while row is not None:  # Fetching row
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table
# ------------------------------------------------------------------------------------
# Function for adding
def insert_firm(conn):
    cursor = conn.cursor()
    name = input("Input firm's name: ")
    country_name = input("Input firm's country: ")
    address = input("Input firm's address: ")
    phone = input("Input phone number: ")
    site = input("Input site's address: ")
    sql = "INSERT INTO PUBLIC.\"firm\"(\"firm_name\", \"country\", \"address\", \
    \"firm_number\", \"site\") VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql, (name, country_name, address, phone, site))
    conn.commit()
def insert_provider(conn):
    cursor = conn.cursor()
    name = input("Input provider's name: ")
    country_name = input("Input provider's country: ")
    address = input("Input provider's address: ")
    phone = input("Input phone number: ")
    sql = "INSERT INTO PUBLIC.\"provider\"(\"provider_name\", \"provider_country\", \"provider_address\", \
    \"provider_number\") VALUES (%s,%s,%s,%s)"
    cursor.execute(sql, (name, country_name, address, phone))
    conn.commit()
def insert_seller(conn):
    cursor = conn.cursor()
    name = input("Input seller's name: ")
    address = input("Input seller's address: ")
    phone = input("Input phone number: ")
    experience = int(input("Input seller's experience: "))
    sel_type = input("Input seller's type: ")
    sql = "INSERT INTO PUBLIC.\"seller\"(\"name_seller\", \"seller_address\", \"seller_number\", \
    \"experience\", \"seller_type\") VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql, (name, address, phone, experience, sel_type))
    conn.commit()
def insert_eq_type(conn):
    cursor = conn.cursor()
    nametype = str(input("Input equipment type's name: "))
    sql = "INSERT INTO PUBLIC.\"equipment_type\"(\"equipment_type_name\") VALUES (%s)"
    cursor.execute(sql, (str(nametype)))
    conn.commit()
def insert_equipment(conn):
    name = input("Input a name of equipment: ")
    price = input("Input price of equipment: ")
    size = input("Input a size: ")
    year = int(input("Input year of arrival: "))
    month = int(input("Input month of arrival: "))
    day = int(input("Input day of arrival: "))
    arrival_date = datetime.date(year, month, day)
    while True:
        country = input("Input a Country (print \"help\" to show list of country) - ")
        if country == "help":
            print(show_firms(conn))
        else:
            break
    while True:
        firm = input("Input a firm id (print \"help\" to show list of firm) - ")
        if firm == "help":
            print(show_firms(conn))
        else:
            break
    while True:
        provider = input("Input a provider id (print \"help\" to show list of providers) - ")
        if provider == "help":
            print(show_provider(conn))
        else:
            break
    while True:
        type = input("Input a equipment type id (print \"help\" to show list of providers) - ")
        if type == "help":
            print(show_equipment_type(conn))
        else:
            break
    while True:
        seller = input("Input a seller id (print \"help\" to show list of sellers - ")
        if seller == "help":
            print(show_sellers(conn))
        else:
            break
    cursor = conn.cursor()
    sql = "INSERT INTO PUBLIC.\"equipment\"(\"equiment_name\", \"equipment_price\", \"equipment_size\", \"equipment_date\",\"equipment_country\", \"id_firm\", \"id_provider\", \"id_equipment_type\",\"id_seller\") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, (name, price, size, arrival_date, country, firm, provider, type, seller))
    conn.commit()
# --------------------------------------------------------------------------------------
#function deleting
def DeleteSellers(conn):
    try:
        print(show_sellers(conn))
        deleteid = int(input("Input ID of seller you want to DELETE - "))
        cursor = conn.cursor()
        sql = "DELETE FROM PUBLIC.\"seller\" WHERE \"id_sellerss\" = \'{}\' ".format(deleteid)
        cursor.execute(sql)
        conn.commit()
        print("Succefull deleting")
    except psycopg2.IntegrityError:
        print("You need to delete equipment!")
        sys.exit()
def DeleteEquipment(conn):
    cursor = conn.cursor()
    deleteid = int(input("Input ID of Equipment you want to DELETE - "))
    cursor = conn.cursor()
    sql = "DELETE FROM PUBLIC.\"equipment\" WHERE \"equipment_key\" = \'{}\' ".format(deleteid)
    cursor.execute(sql)
    conn.commit()
    print("Succefull deleting")
def deletefirm(conn):
    try:
        print(show_firms(conn))
        deleteid = int(input("Input ID of firms you want to DELETE - "))
        cursor = conn.cursor()
        sql = "DELETE FROM PUBLIC.\"firm\" WHERE \"firm_id\" = \'{}\' ".format(deleteid)
        cursor.execute(sql)
        conn.commit()
    except psycopg2.IntegrityError:
        print("You need to delete equipment!")
        sys.exit()
def deleteprovider(conn):
    try:
        print(show_provider(conn))
        deleteid = int(input("Input ID of provider you want to DELETE - "))
        cursor = conn.cursor()
        sql = "DELETE FROM PUBLIC.\"provider\" WHERE \"provider_id\" = \'{}\' ".format(deleteid)
        cursor.execute(sql)
        conn.commit()
    except psycopg2.IntegrityError:
        print("You need to delete equipment!")
        sys.exit()
def delete_eq_type(conn):
    try:
        print(show_equipment_type(conn))
        deleteid = int(input("Input ID of equipment_type you want to DELETE - "))
        cursor = conn.cursor()
        sql = "DELETE FROM PUBLIC.\"equipment_type\" WHERE \"equipment_type_id\" = \'{}\' ".format(deleteid)
        cursor.execute(sql)
        conn.commit()
    except psycopg2.IntegrityError:
        print("You need to delete equipment!")
        sys.exit()
# --------------------------------------------------------------------------------------
#function edit
def editprovider(conn):
    print(show_provider(conn))
    new_id = input("Input provider ID you want to edit - ")
    new_name = input("Input the name  - ")
    new_country = input("Input the country - ")
    new_address = input("Input the adress - ")
    new_number = input("Input number) - ")
    cursor = conn.cursor()
    sql = "UPDATE PUBLIC.\"provider\" SET \"provider_name\" = %s, \"provider_country\" =%s, provider_address=%s, provider_number=%s WHERE \"provider_id\" = \'{}\'".format(new_id)
    cursor.execute(sql, (new_name, new_country, new_address, new_number))
    conn.commit()
def editseller(conn):
    print(show_sellers(conn))
    new_id = input("Input seller ID you want to edit - ")
    new_name = input("Input the name  - ")
    new_address = input("Input the address - ")
    new_number = input("Input the number - ")
    new_exper = input("Input the exoerience - ")
    new_type = input("Input the type - ")
    cursor = conn.cursor()
    sql = "UPDATE PUBLIC.\"seller\" SET \"name_seller\" = %s, \"seller_address\" =%s, seller_number=%s, experience=%s, seller_type=%s WHERE \"id_sellerss\" = \'{}\'".format(new_id)
    cursor.execute(sql, (new_name, new_address, new_number, new_exper,new_type))
    conn.commit()
def editfirm(conn):
    print(show_firms(conn))
    new_id = input("Input firm ID you want to edit - ")
    new_name = input("Input the firm name  - ")
    new_country = input("Input the country - ")
    new_address = input("Input the address - ")
    new_number = input("Input the number - ")
    new_site = input("Input the site - ")
    cursor = conn.cursor()
    sql = "UPDATE PUBLIC.\"firm\" SET \"firm_name\" = %s, \"country\" =%s, address=%s, firm_number=%s, site=%s WHERE \"firm_id\" = \'{}\'".format(new_id)
    cursor.execute(sql, (new_name, new_country, new_address, new_number, new_site))
    conn.commit()
def editequipment(conn):
    print(show_equipment(conn))
    new_id = input("Input equipment ID you want to edit - ")
    new_name = input("Input the name  - ")
    new_price = input("Input the price  - ")
    new_size = input("Input the size - ")
    year = int(input("Input year of arrival: "))
    month = int(input("Input month of arrival: "))
    day = int(input("Input day of arrival: "))
    arrival_date = datetime.date(year, month, day)

    while True:
        new_country = input("Input a Country (print \"help\" to show list of country) - ")
        if new_country == "help":
            print(show_firms(conn))
        else:
            break
    while True:
        firm = input("Input a firm id (print \"help\" to show list of firm) - ")
        if firm == "help":
            print(show_firms(conn))
        else:
            break
    while True:
        provider = input("Input a provider id (print \"help\" to show list of providers) - ")
        if provider == "help":
            print(show_provider(conn))
        else:
            break
    while True:
        type = input("Input a equipment type id (print \"help\" to show list of providers) - ")
        if type == "help":
            print(show_equipment_type(conn))
        else:
            break
    while True:
        seller = input("Input a seller id (print \"help\" to show list of sellers - ")
        if seller == "help":
            print(show_sellers(conn))
        else:
            break
    cursor = conn.cursor()
    sql = "UPDATE PUBLIC.\"equipment\" SET \"equiment_name\" = %s, \"equipment_price\" =%s, equipment_size=%s, equipment_date=%s, equipment_country=%s, id_firm=%s, id_provider =%s, id_equipment_type = %s, id_seller= %s  WHERE \"equipment_key\" = \'{}\'".format(new_id)
    cursor.execute(sql, (new_name, new_price, new_size, arrival_date, new_country, firm, provider, type, seller))
    conn.commit()
# --------------------------------------------------------------------------------------
#Function for showing menu
def delete_menu(conn):
    flag = True
    while flag:  # Printing menu of commands
        vod = input("Select the action: \n1) Delete Firms \n2) Delete Sellers  \n3) Delete Providers  \n4) Delete Equipment \n5) Delete equipment type \n6) Back\n")
        if vod == '1':
            deletefirm(conn)
        elif vod == '2':
            DeleteSellers(conn)
        elif vod == '3':
            deleteprovider(conn)
        elif vod == '4':
            DeleteEquipment(conn)
        elif vod == '5':
            delete_eq_type(conn)
        elif vod == '6':
            flag = False
        else:
            print('Wrong action!')
def adding_menu(conn):
    flag = True
    while flag:  # Printing menu of commands
        vod = input(
            "Select the action: \n1) Insert Firms \n2) Insert Sellers  \n3) Insert Providers  \n4) Insert Equipment \n5) Back\n")
        if vod == '1':
            insert_firm(conn)
        elif vod == '2':
            insert_seller(conn)
        elif vod == '3':
            insert_provider(conn)
        elif vod == '4':
            insert_equipment(conn)
        elif vod == '5':
            flag = False
        else:
            print('Wrong action!')
def Update_menu(conn):
    flag = True
    while flag:  # Printing menu of commands
        vod = input("Select the action: \n1) Update Firms \n2) Update Sellers  \n3) Update Providers  \n4) Update Equipment \n5) Back\n")
        if vod == '1':
            editfirm(conn)
        elif vod == '2':
            editseller(conn)
        elif vod == '3':
            editprovider(conn)
        elif vod == '4':
            editequipment(conn)
        elif vod == '5':
            flag = False
        else:
            print('Wrong action!')
def display_menu(conn):
    flag = True
    while flag:  # Printing menu of commands
        vod = input("Select the action: \n1) Show firms \n2) Show sellers \n3) Show provider \n4) Show equipment \n5) Show equipment type \n6) Back\n")
        if vod == '1':
            print(show_firms(conn))
        elif vod == '2':
            print(show_sellers(conn))
        elif vod == '3':
            print(show_provider(conn))
        elif vod == '4':
            print(show_equipment(conn))
        elif vod == '5':
            print(show_equipment_type(conn))
        elif vod == '6':
            flag = False
        else:
            print('Wrong action!')
def cross_menu(conn):
        flag = True
        while flag:  # Printing menu of commands
            vod = input(
                "Select the action: \n1) Сумма контрактов по странам фирм \n2) Сумма контрактов по странам фирм со стажем  > 3 \n3) Контаркты конкретного поставшщка \n4) Контракты по стране в конкретный год \n5) Поиск поставщиков по фирме изготовителя с ценой > 2000 \n6) Back\n")
            if vod == '1':
                print(sum_price_by_country(conn))
            elif vod == '2':
                print(sum_price_by_counrty_staj3(conn))
            elif vod == '3':
                print(contract_provider(conn))
            elif vod == '4':
                print(coutry_year(conn))
            elif vod == '5':
                print(provider_firm_price(conn))
            elif vod == '6':
                flag = False
            else:
                print('Wrong action!')
# --------------------------------------------------------------------------------------
#function for cross_zapros
def display_menu(conn):
    flag = True
    while flag:  # Printing menu of commands
        vod = input("Select the action: \n1) Show firms \n2) Show sellers \n3) Show provider \n4) Show equipment \n5) Show equipment type \n6) Back\n")
        if vod == '1':
            print(show_firms(conn))
        elif vod == '2':
            print(show_sellers(conn))
        elif vod == '3':
            print(show_provider(conn))
        elif vod == '4':
            print(show_equipment(conn))
        elif vod == '5':
            print(show_equipment_type(conn))
        elif vod == '6':
            flag = False
        else:
            print('Wrong action!')
def sum_price_by_country(conn):
    #Сумма контрактов по странам фирм
    cursor = conn.cursor()
    cursor.execute("SELECT  country, COUNT(equipment_price), SUM(equipment_price) FROM Public.firm, public.equipment\
    WHERE firm_id = id_firm\
    GROUP BY country\
    ORDER BY SUM(equipment_price) DESC")  # Selecting all columns from table seller
    row = cursor.fetchone()
    table = PrettyTable(('Country', 'Amount', 'Summ'))
    while row is not None:  # Fetching row
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table
def sum_price_by_counrty_staj3(conn):
    #Сумма контрактов по странам фирм со стажем  > 3
    cursor = conn.cursor()
    cursor.execute("SELECT  provider_country, COUNT(equipment_price), SUM(equipment_price) FROM public.equipment, public.seller, public.provider\
    WHERE provider_id = id_provider and id_seller=id_sellerss and experience >3\
    GROUP BY provider_country\
    ORDER BY SUM(equipment_price) DESC")  # Selecting all columns from table seller
    row = cursor.fetchone()
    table = PrettyTable(('Country', 'Amount', 'Summ'))
    while row is not None:  # Fetching row
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table
def contract_provider(conn):
    #Контаркты конкретного поставшщка
    cursor = conn.cursor()
    name = input("Введите поставщик: ")
    cursor.execute("SELECT  provider_name, equiment_name, equipment_price,equipment_date FROM public.equipment, public.provider\
    WHERE provider_id = id_provider and provider_name = \'{}\'".format(name))  # Selecting all columns from table seller
    row = cursor.fetchone()
    table = PrettyTable(('Provide name', 'equipment name', 'Price', 'Date'))
    while row is not None:  # Fetching row
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table
def coutry_year(conn):
#Контракты по стране в конкретный год
    cursor = conn.cursor()
    name = input("Введите страну : ")
    year = input("Введите год - ")
    cursor.execute("SELECT  provider_name, equiment_name, equipment_price,equipment_date, provider_country FROM public.equipment, public.provider, public.seller\
    WHERE id_seller = id_sellerss and provider_id = id_provider and provider_country = \'{0}\' ".format(name))  # Selecting all columns from table seller
    row = cursor.fetchone() # YYYY-MM-DD
    table = PrettyTable(('Provide name', "Equipment Name", 'Price', 'Date', 'Coutry'))
    while row is not None:  # Fetching row
        if str(row[3])[:4] == year:
            table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table
def provider_firm_price(conn):
#Поиск поставщиков по фирме изготовителя с ценой > 4000
    cursor = conn.cursor()
    name = input("Введите фирму изготовителя : ")
    cursor.execute("SELECT  provider_name, firm_name, equipment_price  FROM public.firm, public.provider, public.equipment\
    WHERE firm_id = id_firm  and equipment_price > 1000 and id_provider = provider_id and firm_name = \'{}\'".format(name))  # Selecting all columns from table seller
    row = cursor.fetchone()
    table = PrettyTable(('Provider name', 'Firm name', 'Equipment Price' ))
    while row is not None:  # Fetching row
        table.add_row(row)
        row = cursor.fetchone()
    cursor.close()
    return table