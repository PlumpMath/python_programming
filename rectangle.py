#Representation - start
from point import make_point, get_x_coordinate, get_y_coordinate
from segment import get_size
from operator import sub, abs
#Constructor
def make_rectangle(p1, p2, p3, p4):
    if are_opposite_sides_equal(p1, p2, p3, p4):
        return (p1, p2, p3, p4)

#Helper for constructor
def are_opposite_sides_equal(p1, p2, p3, p4):
    if (abs(sub(get_x_coordinate(p1), get_x_coordinate(p2))) == abs(sub(get_x_coordinate(p3), get_x_coordinate(p4)))) and (abs(sub(get_y_coordinate(p2), get_y_coordinate(p3))) == abs(sub(get_y_coordinate(p1), get_y_coordinate(p4)))):
        return True
    else:
        return False

#Selector
def get_length_side_segment(quadruple):
    return (quadruple[0], quadruple[1])

#Selector
def get_breadth_side_segment(quadruple):
    return (quadruple[1], quadruple[2])

#Representation - end


#Use -start
def perimeter(rectangle):
    segment1 = get_length_side_segment(rectangle)
    segment2 = get_breadth_side_segment(rectangle)
    length = get_size(segment1)
    breadth = get_size(segment2)
    return 2 * (length + breadth)

def area(rectangle):
    segment1 = get_length_side_segment(rectangle)
    segment2 = get_breadth_side_segment(rectangle)
    length = get_size(segment1)
    breadth = get_size(segment2)
    return (length * breadth)
#Use - end



#Driver code from user
if __name__ == "__main__":
    p1 = make_point(1, 1)
    p2 = make_point(3, 1)
    p3 = make_point(3, 3)
    p4 = make_point(1, 3)
    rectangle = make_rectangle(p1, p2, p3, p4)
    peri = perimeter(rectangle)
    area_value = area(rectangle)
    print(peri)
    print(area_value)


