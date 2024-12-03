class Calculator:
    def Multiply(x, y):
        return x * y
            
    def Add(x, y):
        return x + y
            
    def Subtract(x, y):
        return x - y
            
    def Divide(x, y):
        return x / y
    
print("Select operation.\n 1. Multiply \n 2. Add\n 3. Subtract\n 4. Divide")

while True:
    choice = input("Enter between 1/2/3/4 or 'Exit': ")
    if choice == 'Exit':
        print("Exiting the program.")
        break
    
    num1 = int(input("First number here: "))
    num2 = int(input("Second number here: "))
    
    if choice == '1':
        print(num1, "*", num2, "=", Calculator.Multiply(num1, num2))
        
    elif choice == '2':
        print(num1, "+", num2, "=", Calculator.Add(num1, num2))
        
    elif choice == '3':
        print(num1, "-", num2, "=", Calculator.Subtract(num1, num2))
        
    elif choice == '4':
        print(num1, "/", num2, "=", Calculator.Divide(num1, num2))
    
    else:
        print("I do not understand command.")
        

