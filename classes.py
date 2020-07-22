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