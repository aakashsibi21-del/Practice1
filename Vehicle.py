# Develop a simple Vehicle Rental Management System using Python OOP concepts. 
# 1. Create an abstract class named Vehicle. 
# ○ Include an abstract method named calculate_rent(days). 
# ○ Include a method named display_vehicle_details(). 
# 2. Encapsulate the rental price per day using a private attribute. 
# ○ Provide a method to retrieve the rental price. 
# 3. Create two child classes: 
# ○ Car 
# ○ Bike 
# 4. Implement calculate_rent(days) differently: 
# ○ Car: Rental price per day × number of days + ₹500 service charge. 
# ○ Bike: Rental price per day × number of days + ₹100 service charge. 
# 5. Create objects of both vehicle types and demonstrate: 
# ○ Displaying vehicle details. 
# ○ Calculating rental charges for 3 days. 
# ○ Displaying the final rental amount.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, Vehicle_Name, Vehicle_no, Rent_price ):
        self.Vehicle_Name = Vehicle_Name
        self.Vehicle_no = Vehicle_no
        self.__Rental_Price = Rent_price

    @abstractmethod
    def calculate_rent(self):
        pass

    @property
    def Rental_price(self):
        return self.__Rental_Price

    @Rental_price.setter
    def Rental_price(self,update):
        if update <=0:
            raise 'The Rental price Cannot be Zero or Positive.'
        self.__Rental_Price = update

    def Display_details(self):
        print('\nVehicle Name : ',self.Vehicle_Name,'\nVehichle No : ', self.Vehicle_no,
              '\nRental Price : ',self.__Rental_Price)

class Car(Vehicle):
    def __init__(self, Vehicle_Name, Vehicle_no, Rent_price, days):
        super().__init__(Vehicle_Name, Vehicle_no, Rent_price)
        self.days = days

    def calculate_rent(self):
        print('Total rental price', ((self.Rental_price * self.days) + 500),'\n')

class Bike(Vehicle):
    def __init__(self, Vehicle_Name, Vehicle_no, Rent_price, days):
        super().__init__(Vehicle_Name, Vehicle_no, Rent_price)
        self.days = days

    def calculate_rent(self):
        print('Total rental price : ',((self.Rental_price * self.days) + 100),'\n')


car = Car('BMW', 'KL 38 A 7724', 5000, 3)
car.Display_details()
car.calculate_rent()

bike = Bike('Royal Enfield', 'KL 38 C 6645', 2000, 3)
bike.Display_details()
bike.calculate_rent()

