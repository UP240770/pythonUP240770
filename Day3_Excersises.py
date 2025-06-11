# 1.- Declare your age as integer variable
age = 18 

# 2.- Declare your height as a float variable
height = 1.75 

# 3.- Declare a variable that store a complex number
complex_number = 2 + 3j

# 4.- Prompt user to enter base and height of triangle, then calculate area
base = float(input("Enter base: "))
triangle_height = float(input("Enter height: "))
area_triangle = 0.5 * base * triangle_height
print("The area of the triangle is", area_triangle)

# 5.- Prompt user to enter sides of triangle and calculate perimeter
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter_triangle = side_a + side_b + side_c
print("The perimeter of the triangle is", perimeter_triangle)

# 6.- Get length and width of rectangle, calculate area and perimeter
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print("Area of the rectangle is", area_rectangle)
print("Perimeter of the rectangle is", perimeter_rectangle)

# 7.- Get radius of a circle, calculate area and circumference
radius = float(input("Enter radius: "))
pi = 3.14
area_circle = pi * radius * radius
circumference = 2 * pi * radius
print("Area of the circle is", area_circle)
print("Circumference of the circle is", circumference)

# 8.- Calculate slope, x-intercept, y-intercept of y = 2x - 2
m = 2  # slope
y_intercept = -2
x_intercept = -y_intercept / m
print("Slope:", m)
print("Y-intercept:", y_intercept)
print("X-intercept:", x_intercept)

# 9.- Calculate slope and distance between points (2, 2) and (6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_2 = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Slope between points:", slope_2)
print("Euclidean distance:", distance)

# 10.- Compare slopes from tasks 8 and 9
print("Are slopes equal?", m == slope_2)

# 11.- Calculate y = x^2 + 6x + 9, try different x values
for x in range(-10, 5):
    y = x**2 + 6*x + 9
    print(f"x: {x}, y: {y}")

# 12.- Length of 'python' and 'dragon', falsy comparison
print("Length of 'python':", len("python"))
print("Length of 'dragon':", len("dragon"))
print("Is length of 'python' not equal to length of 'dragon'?", len("python") != len("dragon"))

# 13.- Use 'and' to check if 'on' is in both 'python' and 'dragon'
print("Is 'on' in both 'python' and 'dragon'?", 'on' in 'python' and 'on' in 'dragon')

# 14.- Use 'in' to check if 'jargon' is in the sentence
sentence = "I hope this course is not full of jargon."
print("Is 'jargon' in the sentence?", 'jargon' in sentence)

# 15.- Negation: there is no 'on' in both python and dragon (should be False)
print("Is 'on' not in both 'python' and 'dragon'?", not ('on' in 'python' and 'on' in 'dragon'))

# 16.- Length of 'python', convert to float and then to string
length_python = len("python")
length_float = float(length_python)
length_str = str(length_float)
print("Length as float:", length_float)
print("Length as string:", length_str)

# 17.- Check if number is even
number = int(input("Enter a number to check if it is even: "))
print("Is the number even?", number % 2 == 0)

# 18.- Check floor division of 7 by 3 == int(2.7)
print("Is 7 // 3 equal to int(2.7)?", 7 // 3 == int(2.7))

# 19.- Check type of '10' == type of 10
print("Is type('10') equal to type(10)?", type('10') == type(10))

# 20.- Check if int('9.8') == 10
try:
    print("Is int('9.8') equal to 10?", int('9.8') == 10)  # This will raise an error
except ValueError:
    print("Cannot convert '9.8' to int directly")

# 21.- Prompt user to enter hours and rate, calculate pay
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
print("Your weekly earning is", weekly_earning)

# 22.- Prompt user to enter number of years lived, calculate seconds lived
years_lived = int(input("Enter number of years you have lived: "))
seconds_lived = years_lived * 365 * 24 * 60 * 60
print("You have lived for", seconds_lived, "seconds.")

# 23.- Display the table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")


#llisto
