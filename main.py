# main menu for hotel management system
from datetime import datetime, timedelta
import os

from utils.hotel import Hotel
from utils.client import Client

hotel_name = "TIRI"


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print("Welcome to " + hotel_name + " Management System")


clear_screen()
hotel = Hotel(hotel_name)
print("Hotel created")

# hardcode rooms and client for testing
print ("Initializing rooms...")
hotel.add_rooms(2, 0, 1500)
hotel.add_rooms(2, 1, 500)
# hotel.add_rooms(2, 1, 3000)
# hotel.delete_room(0)
# hotel.get_room_info(1)
# today = datetime.today()
# tomorrow = today + timedelta(days=2)
# c1 = Client("tester", "07242209", "tunis", "24367878",
#             today, tomorrow, hotel.rooms[0])
# print("Adding test client...")
# hotel.check_in(0, c1)


def check_availability():
    clear_screen()
    print("Check availability")
    print("Occupancy: " + str(hotel.get_occupancy()) + "/" + str(hotel.capacity))


def check_in():
    clear_screen()
    print("Check in")
    if hotel.availability() == False:
        print("No available rooms")
        return
    while True:
        try:
            cin = input("Enter client cin: ")
            if cin.isdigit() == False or len(cin) != 8:
                raise ValueError
            else:

                break
        except ValueError:
            print("Invalid cin. Please enter a valid cin.")
    client = hotel.select_client(cin)
    if client != None:
        if client.room != None:
            print("Client already checked in")
            return
        else:
            print("Client already exists")
            while True:
                try:
                    choice = input(
                        "Do you want to check in this client? (Y/N): ")
                    if choice != "Y" and choice != "N" and choice != "y" and choice != "n":
                        raise ValueError
                    else:
                        if choice == "Y" or choice == "y":
                            while True:
                                try:
                                    room_number = input("Enter room number: ")
                                    if room_number.isdigit() == False:
                                        raise ValueError
                                    else:
                                        room_number = int(room_number)
                                        if (room_number > hotel.get_last_roomnumber() or room_number < hotel.get_first_roomnumber()):
                                            raise ValueError
                                        if hotel.rooms[room_number].availability == False:
                                            raise ValueError
                                        break
                                except ValueError:
                                    print(
                                        "Invalid room number. Please enter a valid room number.")
                            hotel.check_in(room_number, client)
                            break
                        elif choice == "N" or choice == "n":
                            print("Check in cancelled")
                            break
                except ValueError:
                    print("Invalid choice. Please enter Y or N.")
            return
    else:
        name = input("Enter client name: ")
        while True:
            try:
                phone = input("Enter client Phone: ")
                if phone.isdigit() == False or len(phone) != 8:
                    raise ValueError
                else:
                    phone = int(phone)
                    break
            except ValueError:
                print("Invalid phone. Please enter a valid phone.")

        address = input("Enter client address: ")

        while True:
            try:
                check_in = input("Enter check-in date (DD-MM-YYYY): ")
                check_in_date = datetime.strptime(check_in, "%d-%m-%Y")
                break
            except ValueError:
                print(
                    "Invalid date format. Please enter the date in a recognized format.")

        while True:
            try:
                check_out = input("Enter check-out date (DD-MM-YYYY): ")
                check_out_date = datetime.strptime(check_out, "%d-%m-%Y")
                if check_out_date <= check_in_date:
                    raise ValueError
                break
            except ValueError:
                print(
                    "Invalid date format. Please enter the date in a recognized format.")

        client = Client(name, cin, phone, address,
                        check_in_date, check_out_date)
        while True:
            try:
                room_number = input("Enter room number: ")
                if room_number.isdigit() == False:
                    raise ValueError
                else:
                    room_number = int(room_number)
                    if (room_number > hotel.get_last_roomnumber() or room_number < hotel.get_first_roomnumber()):
                        raise ValueError
                    if hotel.rooms[room_number].availability == False:
                        raise ValueError
                    break
            except ValueError:
                print("Invalid room number. Please enter a valid room number.")
        hotel.check_in(room_number, client)


def check_out():
    clear_screen()
    print("Check out")
    if hotel.get_occupancy() == 0:
        print("No clients checked in")
        return
    while True:
        try:
            cin = input("Enter client cin: ")
            if cin.isdigit() == False or len(cin) != 8:
                raise ValueError
            else:
                break
        except ValueError:
            print("Invalid cin. Please enter a valid cin.")
    c1 = hotel.select_client(cin)
    if c1 == None:
        print("Client not found.")
        return
    else:
        while True:
            try:
                room_number = input("Enter room number: ")
                if room_number.isdigit() == False:
                    raise ValueError
                else:
                    room_number = int(room_number)
                    if (room_number > hotel.capacity-1 or room_number < 0):
                        raise ValueError
                    break
            except ValueError:
                print("Invalid room number. Please enter a valid room number.")
        print("bill amount is:", hotel.bill_amount(c1),
              "TND", "(", c1.room.price, "TND/day )")
        input("Press enter to pay bill...")
        print("Bill paid")
        hotel.check_out(room_number, c1)


def search_client():
    clear_screen()
    print("Search client")
    if (len(hotel.clients) == 0):
        print("No clients")
        return
    while True:
        try:
            cin = input("Enter client cin: ")
            if cin.isdigit() == False or len(cin) != 8:
                raise ValueError
            else:
                hotel.search_client(cin)
                break
        except ValueError:
            print("Invalid cin. Please enter a valid cin.")


def print_all_clients():
    clear_screen()
    print("All clients")
    hotel.print_clients()


def search_room():
    clear_screen()
    print("Search room")
    if hotel.capacity == 0:
        print("No rooms available")
        return

    while True:
        try:
            room_number = input("Enter room number: ")
            if room_number.isdigit() == False:
                raise ValueError
            else:
                room_number = int(room_number)
                if (room_number > hotel.get_last_roomnumber() or room_number < hotel.get_first_roomnumber()):
                    raise ValueError
                hotel.get_room_info(room_number)
                break
        except ValueError:
            print("Invalid room number. Please enter a valid room number.")



def hotel_info():
    clear_screen()
    print("Hotel info")
    hotel.get_hotel_info()


def exit():
    print("Exiting...")


def main_menu():
    print("\t1. Hotel management")
    print("\t2. Room management")
    print("\t3. Client management")
    print("\t4. Exit")
    choice = input("Enter your choice: ")
    return choice


def menu_hotel():
    print("\t1. Add room")
    print("\t2. Remove room")
    print("\t3. Get hotel info")
    print("\t4. Back")
    choice = input("Enter your choice: ")
    return choice


def menu_room():
    print("\t1. Check availability")
    print("\t2. Check in")
    print("\t3. Check out")
    print("\t4. Search room")
    print("\t5. Back")
    choice = input("Enter your choice: ")
    return choice


def menu_client():
    print("\t1. Search client")
    print("\t2. Add client")
    print("\t3. Print all clients")
    print("\t4. Pay bill")
    print("\t5. Back")
    choice = input("Enter your choice: ")
    return choice


def add_room():
    print("Add new room")
    while True:
        try:
            room_type = input("Enter room type (0: Single, 1: Double): ")
            if room_type.isdigit() == False:
                raise ValueError
            else:
                if room_type != "0" and room_type != "1":
                    raise ValueError
                room_type = int(room_type)
                break
        except ValueError:
            print("Invalid room type. Please enter a valid room type.")

    while True:
        try:
            price = input("Enter room price: ")
            if price.isdigit() == False:
                raise ValueError
            else:
                price = int(price)
                break
        except ValueError:
            print("Invalid price. Please enter a valid price.")
    hotel.add_room(room_type, price)


def remove_room():
    print("Remove room")
    if hotel.capacity == 0:
        print("No rooms available")
        return
    if hotel.get_occupancy() == hotel.capacity:
        print("All rooms are occupied")
        return
    while True:
        try:
            room_number = input("Enter room number: ")
            if room_number.isdigit() == False:
                raise ValueError
            else:
                room_number = int(room_number)

                if (room_number > hotel.get_last_roomnumber() or room_number < hotel.get_first_roomnumber()):
                    raise ValueError
                break
        except ValueError:
            print("Invalid room number. Please enter a valid room number.")

    hotel.delete_room(room_number)


def hotel_management():
    clear_screen()
    while True:
        print("Hotel management")
        choice = menu_hotel()
        if choice == "1":
            add_room()
        elif choice == "2":
            remove_room()
        elif choice == "3":
            hotel_info()
        elif choice == "4":
            break
        else:
            print("Invalid choice")
        input("Press enter to continue...")
        clear_screen()


def room_management():
    clear_screen()
    while True:
        print("Room management")
        choice = menu_room()
        if choice == "1":
            check_availability()
        elif choice == "2":
            check_in()
        elif choice == "3":
            check_out()
        elif choice == "4":
            search_room()
        elif choice == "5":
            break
        else:
            print("Invalid choice")
        input("Press enter to continue...")
        clear_screen()


def pay_bill():
    if (len(hotel.clients) == 0):
        print("No clients")
        return
    while True:
        print("Paying bill")
        try:
            cin = input("Enter client cin: ")
            if cin.isdigit() == False or len(cin) != 8:
                raise ValueError
            else:
                break
        except ValueError:
            print("Invalid cin. Please enter a valid cin.")

    c1 = hotel.select_client(cin)
    if c1 == None:
        print("Client not found.")
        return
    elif (c1.room == None):
        print("Client ", c1.name, "is not checked in yet.")
        print("Bill amount is: 0 TND")
        print("Do you want to delete client?")
        choice = input("Enter your choice (y/n): ")
        if choice == "y":
            hotel.delete_client(c1.cin)
            print("Client deleted")
        else:
            print("Client not deleted")
        return
    else:
        print("Client", c1.name, "satyed",
              str(c1.get_duration().days), "days", "in room", c1.room.room_number)
        print("bill amount is:", hotel.bill_amount(c1),
              "TND", "(", c1.room.price, "TND/day )")
        input("Press enter to pay bill...")
        print("Bill paid")
        hotel.check_out(c1.room.room_number, c1)


def add_client():
    print("Add client")
    while True:
        try:
            cin = input("Enter client cin: ")
            if cin.isdigit() == False or len(cin) != 8:
                raise ValueError
            else:
                break
        except ValueError:
            print("Invalid cin. Please enter a valid cin.")
    if hotel.select_client(cin) != None:
        print("Client already exists")
        return
    name = input("Enter client name: ")

    while True:
        try:
            phone = input("Enter client phone: ")
            if phone.isdigit() == False or len(phone) != 8:
                raise ValueError
            else:
                break
        except ValueError:
            print("Invalid phone. Please enter a valid phone.")

    address = input("Enter client address: ")

    while True:
        try:
            check_in = input("Enter check-in date (DD-MM-YYYY): ")
            check_in_date = datetime.strptime(check_in, "%d-%m-%Y")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in a recognized format.")

    while True:
        try:
            check_out = input("Enter check-out date (DD-MM-YYYY): ")
            check_out_date = datetime.strptime(check_out, "%d-%m-%Y")
            if check_out_date <= check_in_date:
                raise ValueError
            break
        except ValueError:
            print("Invalid date format. Please enter the date in a recognized format.")

    print("Do you want to book a room? (y/n)")

    choice = input("Enter your choice: ")
    if choice == "y" or choice == "Y":
        while True:
            if hotel.availability() == False:
                print("No available rooms")
                c1 = Client(name, cin, address, phone,
                            check_in_date, check_out_date)
                hotel.add_client(c1)
                return
            try:
                room_number = input("Enter room number: ")
                if room_number.isdigit() == False:
                    raise ValueError
                else:
                    room_number = int(room_number)
                    if (room_number > hotel.get_last_roomnumber() or room_number < hotel.get_first_roomnumber()):
                        raise ValueError
                    if hotel.rooms[room_number].availability == False:
                        raise ValueError
                    hotel.check_in(room_number, Client(
                        name, cin, address, phone, check_in_date, check_out_date))
                    break
            except ValueError:
                print("Invalid room number. Please enter a valid room number.")
    elif choice == "n" or choice == "N":
        c1 = Client(name, cin, address, phone, check_in_date, check_out_date)
        hotel.add_client(c1)


def client_management():
    clear_screen()
    while True:
        print("Client management")
        choice = menu_client()
        if choice == "1":
            search_client()
        elif choice == "2":
            add_client()
        elif choice == "3":
            print_all_clients()
        elif choice == "4":
            pay_bill()
        elif choice == "5":
            break
        else:
            print("Invalid choice")
        input("Press enter to continue...")
        clear_screen()


def main():
    while True:
        choice = main_menu()
        if choice == "1":
            hotel_management()
        elif choice == "2":
            room_management()
        elif choice == "3":
            client_management()
        elif choice == "4":
            exit()
            break
        else:
            print("Invalid choice")
        input("Press enter to continue...")
        clear_screen()


main()
