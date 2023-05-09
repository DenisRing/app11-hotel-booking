import pandas
from abc import ABC, abstractmethod

df = pandas.read_csv("hotels.csv", dtype={"id": str})

"""
Instance variables are coded within the method of the class, like name and hotel_id
Class variable are coded outside, like watermark. These are shared amongst all instances

Instance Method. If it has self, its an instance method. The method can be applied to an instance
Class Method uses cls instead of self (along with other variables) and @classmethod just above function
This CAN be self, but cls is convention. Related to the Class, but not the Instance.

A property uses a @property decorator. It isnt called and behaves like a variable?
You keep that code enclosed inside a method

Static methods are created using the @staticmethod decorator. They dont take self or cls arguements. Like a function
doesnt reference class or instance. Use them for utilities, like conversions. Blurred with class methods, but
has no related to its class. Rare-ish

Magic Methods. Overrides built in methods found with dir(Hotel). Write at end of class. Check the purple __eq__
Needs to be self and other because esotericism 

Abstract Classes the OG parent, like grandparent. Inheirts from ABC which is imported. Abstract Base Class. You
CANT instnatiate these. Not supposed to create instances, its abstract, it defines a structure. Helps with clear code
In this case, because it has a generate method, it means every child must have its own generate method
Abstract Methods also needs to be imported as abstractmethod and decorated accordingly. 

"""

class Hotel:
    watermark = "The Real Estate Company"
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False


class Ticket(ABC):

    @abstractmethod
    def generate(self):
        pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here is your booking data:
        Name: {self.the_customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name


    @staticmethod
    def convert(amount):
        return amount * 1.2

class DigitalTicket(Ticket):
    def generate(self):
        pass


"""
hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="134")

print(hotel1.name)
print(hotel2.name)
print(hotel1.watermark)
print(hotel2.watermark)
print(Hotel.watermark)

print(hotel1.available())

print(Hotel.get_hotel_count(data=df)) #class methods
print(hotel1.get_hotel_count(data=df))

ticket = ReservationTicket(customer_name="john smith ", hotel_object=hotel1) # properties
print(ticket.the_customer_name)
print(ticket.generate())

converted = ReservationTicket.convert(10)
print(converted)"""

