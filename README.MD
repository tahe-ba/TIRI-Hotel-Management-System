# TIRI Management System

A command line interface (CLI) for managing a hotel.

## Features

* Manage various aspects of the hotel, such as setting room rates or viewing the occupancy status of rooms
* View and modify rooms in the hotel, such as adding or removing rooms or changing their type or price
* View and manage guests staying at the hotel, such as adding or removing guests or making reservations

## Usage

To run the program, open a terminal window and navigate to the directory where the program is located. Then, enter the following command:

> python main.py

The main menu will be displayed, with the following options:

1. Hotel management
2. Room management
3. Client management
4. Exit

Select an option by entering the corresponding number.

### Hotel management

The hotel management menu allows you to manage various aspects of the hotel. The following options are available:

1. **Add room**
2. **Remove room**
3. **Get hotel info**
4. **Back**

*Add room:* add a new room to the hotel (room type, room price)

*Remove room:* remove a room from the hotel (room number)

*Get hotel info:* return information about the hotel (hotel name,capacity, list of clients, list of rooms)

*Back:* return to the main menu

### Room management

The room management menu allows you to view and modify the rooms in the hotel. The following options are available:

1. **Check availability**
2. **Check in**
3. **Check out**
4. **Search room**
5. **Back**

*Check availability:* check if a room is available (room number)

*Check in:* check in a guest (cin,name,phone,address,checkin date,checkout date,room number)

*Check out:* check out a guest (room number)

*Search room:* search for a room (room number)

*Back:* return to the main menu

### Client management

The client management menu allows you to view and manage the guests staying at the hotel. The following options are available:

1. **Search client**
2. **Add client**
3. **Print all clients**
4. **Pay bill**
5. **Back**

*Search client:* search for a client (cin)

*Add client:* add a new client (cin,name,phone,address,checkin date,checkout date) and gives the chance to choose a room now or later

*Print all clients:* print all clients

*Pay bill:* pay the bill for a client (cin) and check out the client

*Back:* return to the main menu

## Installation

Before running the program, make sure you have the following dependencies installed:

* Python 3.x

## Examples

Here are some examples of how to use the program:

* To add a new room, select "Hotel management" from the main menu, then select "Add room" and enter the type and price of the room.
* To check in a guest, select "Room management" from the main menu, then select "Check in" and enter the guest's details and select a room.

## Troubleshooting

If you encounter any issues while using the program, try the following:

* Make sure you have the latest version of the program and all dependencies installed.
* If you are having trouble with a specific feature, try restarting the program and trying again.

## Contributing

If you would like to contribute to the development of this project, please contact the project maintainer.

I hope this helps! Let me know if you have any questions or need further assistance.