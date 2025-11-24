Features:

Register Reservations

Book tickets for multiple passengers at once

Update Records: Modify passenger name, boarding station, or destination station

Search Reservations: Find reservation details using PNR number

Delete Reservations: Remove reservation records from the system

Requirements: 

Python

How to Run Ensure you have Python installed on your system

Download or copy the Python script

Run the script using: python station_management.py

Usage:
When you run the program, you'll see a main menu with the following options:

 Register a reservation:

  Enter the number of passengers

  Provide details for each passenger (Name, Boarding Station, Destination Station, PNR)

 Update a record:

  Enter your 10-digit PNR number

  Choose what to update (Name, Boarding Station, or Destination Station)

  Provide the new information

 Search for a reservation:

  Enter your 10-digit PNR number

  View reservation details if found

 Delete a reservation:

  Enter your 10-digit PNR number

  Remove the reservation from the system

Important Notes:

PNR numbers must be exactly 10 digits long

The system stores data in memory during the session (data is not persisted after closing)

All PNR validations require exactly 10 digits

Limitations:
 Data is stored only in memory and will be lost when the program exits

 No input validation for station names or passenger names

 Basic error handling for invalid menu choices

Future Enhancements Potential improvements could include:

 Database integration for data persistence

 Input validation for all fields

 Additional features like fare calculation

 Date and time tracking for reservations

 Export functionality for records
