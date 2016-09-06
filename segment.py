# Representation - start

from point import distance_between_points, make_point, get_x_coordinate, get_y_coordinate
#Constructor
def make_segment(point1, point2):
    return (point1, point2)

#Selector
def start_segment(lineSegment):
    return lineSegment[0]

#Selector
def end_segment(lineSegment):
    return lineSegment[1]

#Representation - end

#Use -start
def midpoint_segment(lineSegment):
    return make_point((get_x_coordinate(start_segment(lineSegment)) + get_x_coordinate(end_segment(lineSegment)))/2, (get_y_coordinate(start_segment(lineSegment)) + get_y_coordinate(end_segment(lineSegment)))/2)

def get_size(lineSegment):
    return distance_between_points(start_segment(lineSegment), end_segment(lineSegment))

#Use - end


#Driver code from user
if __name__ == "__main__":
    p1 = make_point(1,2)
    p2 = make_point(3, 4)
    line = make_segment(p1, p2)
    midpoint = midpoint_segment(line)
    print(midpoint)




