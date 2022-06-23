prompt = """
What topping would you like on your pizza?
Enter 'quit' when you are finished: """

stop_looping = False
while not stop_looping:
    topping = input(prompt)
    if topping != 'quit':
        print(f"  I'll add {topping} to your pizza.")
    else:
        stop_looping = True


active = True
while active:
    topping = input(prompt)
    if topping != 'quit':
        print(f"  I'll add {topping} to your pizza.")
    else:
        active = False


while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"  I'll add {topping} to your pizza.")
    else:
        break
