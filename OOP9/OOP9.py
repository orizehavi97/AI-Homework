class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"Point at ({self.x}, {self.y})"

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


p1 = Point(3, 4)
p2 = Point(3, 4)

distance = (p1.x ** 2 + p2.x ** 2) ** 0.5

points_dict = {}

points_dict[p1] = distance
points_dict[p2] = "Point 2"

print("Dictionary:", points_dict)

# 1. One, because p1 and p2 compare equal and have the same hash so the second assignment change the first.

# 2. A hash collision is when two different objects produce the same hash value.
#    Despite being separate instances, p1 and p2 compare equal and share the same hash,
#    so the dictionary treats them as the same key rather than a hash collision.

# 3. Reference count is the number of live references to an object. When it drops to zero, python delete it immediately.
#    The garbage collector supplements this by cleaning up unreachable references.
