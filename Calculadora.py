class Calculator():
    def multiply(self, x, y):
        return x * y
            
    def add(self, x, y):
        return x + y
            
    def subtract(self, x, y):
        return x - y
            
    def divide(self, x, y):
        return x / y
    
calculator = Calculator()
    
print("Select operation.\n 1. Multiply \n 2. Add\n 3. Subtract\n 4. Divide")

while True:
    choice = input("Enter between 1/2/3/4 or 'Exit': ")
    if choice == 'Exit':
        print("Exiting the program.")
        break
    
    num1 = int(input("First number here: "))
    num2 = int(input("Second number here: "))
    
    if choice == '1':
        print(num1, "*", num2, "=", calculator.multiply(num1, num2))
        
    elif choice == '2':
        print(num1, "+", num2, "=", calculator.add(num1, num2))
        
    elif choice == '3':
        print(num1, "-", num2, "=", calculator.subtract(num1, num2))
        
    elif choice == '4':
        print(num1, "/", num2, "=", calculator.divide(num1, num2))
    
    else:
        print("I do not understand command.")
        

