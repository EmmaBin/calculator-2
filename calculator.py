"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    user_choice= input("Type your math problem using operator, num1, num2 >>")
    tokens= user_choice.split(" ")
    if tokens[0] == "q":
        break
    else: 
        if tokens[0] == "+":
            print(add(int(tokens[1]), int(tokens[2])))


