#calculator
logo = """ 
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""


def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide,
    
}
def calculator():
  print(logo)
    
  num1 = int(input("Enter the first number:"))
  for symbol in operations:
     print(symbol)
  should_continue = True

  while should_continue:
    operation_symbol = input("Enter the operation symbol:")
    num2 = int(input("Enter the second number:"))
    cal_function = operations[operation_symbol]
    answer = cal_function(num1,num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if (input(f"Type 'y' to continue calculating with: {answer}, or Type 'n' to start new calculation:")) == "y":
      num1 = answer
    else:
      should_continue = False
    calculator()


calculator()
        