#Calculator
from art import logo
print(logo)

#Add
def add(n1,n2):
  return n1+n2
#Subtract
def subtract(n1,n2):
  return n1-n2
#Multiply
def multiply(n1,n2):
  return n1*n2
#divide
def divide(n1,n2):
  return n1/n2

operations = {
        "+":add,
        "-":subtract,
        "*":multiply,
        "/":divide
          }
def calculator():
  num1 = int(input("What's the first Number?:"))
  for symbol in operations:
    print(symbol )

  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation: ") 
    num2 = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol] 
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    result = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or type 'q' to quit.")
    if result == "y":
        num1 = answer
    elif result == "q":
      should_continue =False
    else:
      should_continue =False
      calculator()

calculator()