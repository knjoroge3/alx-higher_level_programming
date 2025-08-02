try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError:
            print("age cannot be negative")

