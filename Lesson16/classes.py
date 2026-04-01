class Vehicle:
    def __init__(self, make, model): # Constructor: This runs automatically when object is created.
        self.make = make #self is how object methods know WHICH object called them
        self.model = model

    def moves(self):
        print(f"\nstarting the engine of your {self.make} {self.model}...\n")

    def stop(self):
        print(f'stopping the engine...\n')
    
    def desc(self):
        print(f'This is a {self.make} {self.model}.')

my_car = Vehicle("Toyota", "Corolla")
my_car.moves()
my_car.stop()
my_car.desc()

your_car = Vehicle("Honda", "Civic")
your_car.moves()    
your_car.stop()


###################### INHERITANCE ######################

class Airplane(Vehicle): # Airplane is a child class of Vehicle, it inherits all the properties and methods of Vehicle
    # def __init__(self, make, model, num_engines):
    #     super().__init__(make, model) # super() is a built-in function that allows us to call methods from the parent class, in this case it calls the __init__ method of Vehicle to initialize make and model
    #     self.num_engines = num_engines

    def moves(self):
        print('\nstarting the engine of airplane tighten your seatbelts...\n')

    # def desc(self):
    #     print(f'This is a {self.make} {self.model} with {self.num_engines} engines.')


class Bike(Vehicle):
    def moves(self):
        print(f'\nstarting your {self.make} {self.model}\'s engine...\n')


class Van(Vehicle):
    pass # pass is a placeholder that does nothing, it allows us to create a class without defining any methods or properties, 
         # it will still inherit all the properties and methods of Vehicle




my_plane = Airplane("Boeing", "747")
my_bike = Bike("Honda", "CB300R")
my_van = Van("Omni", "Transit")

my_plane.moves()
my_plane.desc()

my_bike.moves()
my_bike.stop()

my_van.desc()
my_van.moves()