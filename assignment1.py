#def add_numbers(x, y):
   # return x + y

#result = add_numbers(10, 5)
#print(result)  # Outputs: 15

#marks = int(input("Enter the student's marks (0-100): "))

# Grading system based on the marks
#if marks > 70:
   # print("Grade: Distinction 🏆")
#elif marks >= 60:
 #   print("Grade: Credit 🎖️")
#elif marks >= 50:
  #  print("Grade: Pass 👍")
#else:
#   print("Grade: Fail ❌")

def input_numbers():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    Equation = input("Enter the equation: ")
    if Equation == "+":
        return x + y
    elif Equation == "-":
        return x - y
    elif Equation == "*":
        return x * y
    elif Equation == "/":
        return x / y
    elif Equation == "%":
        return x % y
    elif Equation == "**":
        return x ** y
    else:
        return "Invalid equation"
print(input_numbers())
