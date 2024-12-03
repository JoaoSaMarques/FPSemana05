def Calculator():
    
    def Multiply(x, y):
        return x * y
        
    def Add(x, y):
        return x + y
        
    def Subtract(x, y):
        return x - y
        
    def Divide(x, y):
        if y == 0:
            return "Error: Division by zero is not allowed."
        return x / y

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num ⬤