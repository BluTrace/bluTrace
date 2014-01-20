import math

def find_distance_with_angle(x1, y1, x2, y2, north):
  x_diff = x2 - x1
  y_diff = y2 - y1
  sum_of_squares = x_diff**2 + y_diff**2
  distance = math.sqrt(sum_of_squares)
  theta_rad = math.asin(y_diff/distance)
  theta_degree = (180/math.pi) * theta_rad
  print "Distance: ", distance
  print "Angle in degrees: ", theta_degree
  print "Angle from north axis: ", math.ceil((theta_degree - north)*100)/100

print "Assuming all coordinates lie in 1st quadrant"
north = input("Enter the angle for north with respect to x-axis: ")
x1 = input("Enter the x-coordinate for first point: ")
y1 = input("Enter the y-coordinate for first point: ") 
x2 = input("Enter the x-coordinate for second point: ")
y2 = input("Enter the y-coordinate for second point: ") 
find_distance_with_angle(x1, y1, x2, y2, north)
