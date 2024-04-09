#!/usr/bin/env python3

def admin_login(username, password):
    if username.upper() == "ADMIN" and password == "12345":
        return "Access granted"
    return "Access denied"

def hows_the_weather(temperature):
    if temperature < 49:
        return "It's brisk out there!"
    elif temperature > 40 and temperature < 64:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"


def fizzbuzz(num):
    if not num % 15:
        return "FizzBuzz"
    elif not num % 5:
        return "Buzz"
    elif not num % 3:
        return "Fizz"
    
    return num
    
    


def calculator(operation, num1, num2):
    if operation == "+" or operation == "-" or operation == "*" or operation == "/":
        sum = str(num1) + operation + str(num2)
        return eval(sum)
    else:
        print("Invalid operation!")
        return None
