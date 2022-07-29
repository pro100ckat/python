import psycopg2  # Import library postgres
import Commands  # Import file with sql commands
from prettytable import PrettyTable
if __name__ == '__main__':

    flag = True
    try:
        print("Connecting to database..")
        conn = psycopg2.connect("host=" + "localhost" + " port=" + "5432" + " dbname=" + "NDB" + " user=" + "postgres" + " password=" + "10217200")
        print("Connected!\n")
    except psycopg2.ProgrammingError:
        print("Connection error.")
        flag = False
    while flag:  # Printing menu of commands
        vod = input("Select the action: \n1) Show table \n2) Add record \n3) Update record \n4) Delete record\n5) Cross\n6) Exit\n ")
        if vod == '1':
            Commands.display_menu(conn)
        elif vod == '2':
            Commands.adding_menu(conn)
        elif vod == '3':
            Commands.Update_menu(conn)
        elif vod == '4':
            Commands.delete_menu(conn)
        elif vod == '5':
            Commands.cross_menu(conn)
        elif vod == '6':
            flag = False
        else:
            print('Wrong action!')
    conn.close()
