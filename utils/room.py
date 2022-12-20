# room number, type, price, and availability
class Room:
    def __init__(self, room_number, room_type, price, availability,client=None):
        self.room_number = room_number
        self.room_type = room_type # 0 = single, 1 = double
        self.price = price
        self.availability = availability # 0 = not available, 1 = available , false = not available, true = available
        self.client = client

    # getter and setter for room class
    def get_room_number(self):
        return self.room_number
        
    def set_room_number(self, room_number):
        self.room_number = room_number

    def get_room_type(self):
        return self.room_type
    
    def set_room_type(self, room_type):
        self.room_type = room_type
    
    def get_price(self):
        return self.price
    
    def set_price(self, price):
        self.price = price

    def get_availability(self):
        return self.availability

    def set_availability(self, availability):
        self.availability = availability

    def get_client(self):
        return self.client
    
    def set_client(self, client):
        self.client = client
    
    def set_room(self, room_number, room_type, price, availability):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.availability = availability

    def __str__(self):

        if self.room_type == 0:
            room_type_str = "Single"
        elif self.room_type == 1:
            room_type_str = "Double"
        else:
            room_type_str = "Undefined"
        
        if self.availability == 0:
            availability_str = "Not available"
        elif self.availability == 1:
            availability_str = "Available"
        else:
            availability_str = "Undefined"

        return "Room number: " + str(self.room_number) + "Room type: " + room_type_str + "Price: " + str(self.price) + "Availability: " + availability_str