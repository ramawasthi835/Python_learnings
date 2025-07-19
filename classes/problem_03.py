import random

# TRAIN BOOKING SYSTEM USING OOP
class Train:

    # Method to book a train ticket
    def book(self, fro, to):
        self.fro = fro  # Origin
        self.to = to    # Destination

        # Generate a random PNR number
        PNR = random.randint(111111, 999999)

        # Print booking confirmation
        print(f"Train successfully booked from {fro} to {to}.")
        print(f"Your PNR Number is {PNR}")

        return PNR

    # Method to get fare details for a given PNR
    def get_fare(self, PNR):
        fare = random.randint(100, 999)  # Generate random fare
        print(f"Fare for PNR number {PNR} is ₹{fare}")

    # Method to get status of a train (dummy implementation)
    def get_status(self, PNR):
        print(f"Train status for PNR {PNR}: On Time!!")

# Create an instance of the Train class
a = Train()

# Book a ticket and get the generated PNR
pnr = a.book("Delhi", "Kanpur")

# Get fare for the booked PNR
a.get_fare(pnr)

# (Optional) Get train status
# a.get_status(pnr)

    