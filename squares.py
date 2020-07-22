#from my script named square use the function squares
from square import squares

#call the function squares and pass in value 4
print(squares(4))

#display a loop of squared numbers
for i in range(10):
    print(f"The square number of {i} is {squares(i)}.")