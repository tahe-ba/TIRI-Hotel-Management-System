# hotel name, capacity, rooms, guests, check in, check out, occupancy

from .room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.capacity = 0
        self.rooms = []
        self.clients = []

    def get_room_by_number(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None

    def get_first_roomnumber(self):
        if len(self.rooms) == 0:
            return 0
        return self.rooms[0].room_number

    def get_last_roomnumber(self):
        if len(self.rooms) == 0:
            return 0
        return self.rooms[-1].room_number

    def add_rooms(self, room_numbers, room_types, prices):
        room_type = "single" if room_types == 0 else "double"
        for i in range(room_numbers):
            room = Room(self.get_last_roomnumber()+1, room_types, prices, 1)
            self.rooms.append(room)
            self.capacity += 1
        print(str(room_numbers)+" Rooms added" + " of type " +
              room_type + " with price " + str(prices)+" TND/night")

    def add_room(self, room_type, price):
        room_type_str = "single" if room_type == 0 else "double"
        room = Room(self.get_last_roomnumber()+1, room_type, price, 1)
        self.rooms.append(room)
        print("Room number "+str(room.room_number)+" added of type " +
              room_type_str + " with price " + str(price))
        self.capacity += 1

    def delete_room(self, room_number):
        if self.get_room_by_number(room_number).client != None:
            print("Some clients are in this room")
            return
        for room in self.rooms:
            if room.room_number == room_number:
                self.rooms.remove(room)
                self.capacity -= 1
                print("Room number "+str(room_number)+" deleted")
                return

    def get_hotel_info(self):
        print("Hotel name: " + self.name)
        print("Hotel capacity: ", str(self.get_occupancy()) +
              "/"+str(self.capacity))

        print("\nHotel clients ("+str(len(self.clients))+") :")
        if len(self.clients) == 0:
            print("No clients")
        print("----------------------------")
        for client in self.clients:
            print("Client name: " + client.name)
            print("Client cin: " + str(client.cin))
            if client.room != None:
                print("Client room: " + str(client.room.room_number))
            print("----------------------------")

        print("\nHotel rooms ("+str(self.capacity)+") : ")
        if len(self.rooms) == 0:
            print("No rooms")
        print("----------------------------")
        for room in self.rooms:
            print("Room number: " + str(room.room_number))
            if room.room_type == 0:
                print("Room type: Single")
            elif room.room_type == 1:
                print("Room type: Double")
            print("Room price: " + str(room.price)+" TND")
            if room.availability == 1:
                print("Room availability: Available")
            else:
                print("Room availability: Not available")

            if room.client != None:
                print("Room client name: " + room.client.name)
            print("----------------------------")

    def check_in(self, room_number, client):
        if client.room != None:
            print("Client " + str(client.cin) +
                  " is already in room " + str(client.room.room_number))
            return
        if self.capacity == 0:
            print("Hotel is full")
            return
        for room in self.rooms:
            if room.availability == 1:
                if room.room_number == room_number:
                    room.availability = 0
                    client.room = room
                    room.client = client
                    if client not in self.clients:
                        self.clients.append(client)
                    print("Checked in " + str(client.cin) +
                          " to room " + str(room.room_number))
                    return
            else:
                if room.room_number == room_number:
                    print("Room " + str(room_number) + " is not available")
                    print("Here are the available rooms :")
                    for room in self.rooms:
                        if room.availability == 1:
                            print(room)
                    return

    def check_out(self, room_number, client):
        if client.room == None:
            print("Client " + str(client.cin) + " is not in a room")
            return
        if client.room.room_number != room_number:
            print("Room " + str(room_number) +
                  " is not assigned to client " + str(client.cin)+"\nThis client is in the room "+str(client.room.room_number))
            return
        for room in self.rooms:
            if room.room_number == room_number:
                self.clients.remove(self.select_client(client.cin))
                room.availability = 1
                room.client = None
                print("check out " + str(client.cin) +
                      " from room " + str(room.room_number))
                return
        print("Room " + str(room_number) + " checkout failed")

    def get_occupancy(self):
        occupancy = 0
        for room in self.rooms:
            if room.availability == 0:
                occupancy += 1
        return occupancy

    def get_room_info(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                print("Room found")
                print("Room number: " + str(room.room_number))
                if room.room_type == 0:
                    print("Room type: Single")
                elif room.room_type == 1:
                    print("Room type: Double")

                print("Room price: " + str(room.price))
                if room.availability == 1:
                    print("Room availability: Available")
                else:
                    print("Room availability: Not available")
                if room.client != None:
                    print("Room client name: " + room.client.name)

    def search_client(self, cin):
        for client in self.clients:
            if client.cin == cin:
                print("Client found")
                print("------------------------")
                print("Client name: " + client.name)
                print("Client cin: " + str(client.cin))
                print("Client address: ", client.address)
                print("Client phone: " + str(client.phone))
                if client.room != None:
                    print("Client room number: " +
                          str(client.room.room_number))
                return
        print("Client not found")

    def select_client(self, cin):
        for client in self.clients:
            if client.cin == cin:
                return client
        return None

    def add_client(self, client):
        if self.select_client(client.cin) != None:
            print("Client already exists")
            return
        print("Client "+str(client.name)+" added but not checked in")
        self.clients.append(client)

    def delete_client(self, cin):
        for client in self.clients:
            if client.cin == cin:
                self.clients.remove(client)
                return
        print("Client not found")

    def print_clients(self):
        if len(self.clients) == 0:
            print("No clients")
            return
        print("----------------------------")
        for client in self.clients:
            print("Client name: " + client.name)
            print("Client cin: " + str(client.cin))
            print("Client address: ", client.address)
            print("Client phone: " + str(client.phone))
            if client.room != None:
                print("Client room: " + str(client.room.room_number))
                print("Check in date: " +
                      str(client.from_date.strftime("%d-%m-%Y")))
                print("Check out date: " +
                      str(client.to_date.strftime("%d-%m-%Y")))
                print(
                    "Duration: " + str(client.get_duration().days) + " days")

            print("----------------------------")

    def check_room_availability(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.availability == 1:
                    print("Room available")
                    print("Room price: " + str(room.price))
                else:
                    print("Room not available but will be available on " +
                          str(room.client.to_date.strftime("%d-%m-%Y")))
                return
        print("Room not found")

    def availability(self):
        if self.capacity == 0:
            return False
        if len(self.rooms) == 0:
            return False
        if self.capacity - self.get_occupancy() == 0:
            return False
        return True

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, capacity):
        self.capacity = capacity

    def get_rooms(self):
        return self.rooms

    def set_rooms(self, rooms):
        self.rooms = rooms

    def get_clients(self):
        return self.clients

    def set_clients(self, clients):
        self.clients = clients

    def bill_amount(self, client):
        return client.room.price * client.get_duration().days
