def classify_triangle(a, b, c):
    if min(a, b, c) <= 0: # Check if any side length is less than or equal to zero
        return "Invalid Triangle"
    
    sides = sorted([a, b, c])
    right_triangle = sides[0]**2 + sides[1]**2 == sides[2]**2 # Check if it is a right triangle
    
    if a == b == c:
        return "Equilateral and Right Triangle" if right_triangle else "Equilateral Triangle" #Check equilateral triangle
    elif a == b or b == c or a == c:
        return "Isosceles and Right Triangle" if right_triangle else "Isosceles Triangle" #Check Isosceles triangle
    else:
        return "Scalene and Right Triangle" if right_triangle else "Scalene Triangle" #Check scalene triangle

if __name__ == "__main__":
    try:
        a, b, c = map(float, input("Enter the lengths of sides a, b, and c separated by spaces: ").split())
        print(f"The triangle is: {classify_triangle(a, b, c)}")
    except ValueError:
        print("Please enter valid numbers.")  #Error Handling
