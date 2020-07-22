# create a class for points
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
# assign p to become a point
p = Point(2,8)
#print the values
print(p.x)
print(p.y)
# print the co-ords in formatted string. 
print(f"Co-ordinates of the point are x:{p.x} and y:{p.y}.")

# more classes
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    #methods of the flight class. 
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True    

    def open_seats(self):
        return self.capacity - len(self.passengers)
       

flight = Flight(3)

people = ["Harry", "Peter", "Jillian", "Barry"]
# loop and add these people to the flight
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"no seats for {person}")