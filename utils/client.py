# name cin,address,phone,from_date,to_date,room_number

class Client:
    def __init__(self, name, cin, address, phone, from_date, to_date, room=None):
        self.name = name
        self.cin = cin
        self.address = address
        self.phone = phone
        self.from_date = from_date
        self.to_date = to_date
        self.room = room

    # getter and setter for client class
    def get_duration(self):
        return self.to_date - self.from_date

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cin(self):
        return self.cin

    def set_cin(self, cin):
        self.cin = cin

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_from_date(self):
        return self.from_date

    def set_from_date(self, from_date):
        self.from_date = from_date

    def get_to_date(self):
        return self.to_date

    def set_to_date(self, to_date):
        self.to_date = to_date

    def get_room(self):
        return self.room

    def set_room(self, room):
        self.room = room

    def set_client(self, name, cin, address, phone, from_date, to_date):
        self.name = name
        self.cin = cin
        self.address = address
        self.phone = phone
        self.from_date = from_date
        self.to_date = to_date

    def get_client(self):
        return self.name, self.cin, self.address, self.phone, self.from_date, self.to_date

    def __str__(self):
        return "Name: " + self.name + " CIN: " + self.cin + " Address: " + self.address + " Phone: " + str(self.phone) + " From date: " + str(self.from_date) + " To date: " + str(self.to_date)

        