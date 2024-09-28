import math

x = input("Hello There!, type (start) to start uning our online calculator: ")

while True:
    
    print("-" * 30)
    n1 = int(input("First digit: "))
    print("-" * 30)
    n2 = int(input("Second digit: "))

    a = n1 * n2
    b = n1 + n2
    c = n1 - n2
    d = n1 / n2

    l = ["a. multiply", "b. add", "c. subtract", "d. devide"]
    print(l)

    choice = input("Choose a, b, c, d, or exit: ")

    if choice == "a":
        print("The answer is: ", a)
    elif choice == "b":
        print("The answer is: ", b)
    elif choice == "c":
        print("The answer is: ", c)
    elif choice == "d":
        print("The answer is: ", d)
    elif choice == "exit":
        print("have a nice time")
        break
    else:
        print("Invalid input. Please choose a, b, c, d, or exit.")
