#Simple Calculator using Python
print("Welcome to the Simple Calculator!")

ch = "yes"

while ch.lower() != "no":
    try:
        #Input two numbers
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        #Menu for operations
        print("Choose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        operation = input("Enter your choice (1,2, 3, 4 or +, -, *, /)")

        #Perform the operation 
        if operation == '1' or operation == '+':
            print(f"{a} + {b} = {a + b}")
        elif operation == '2' or operation == '-':
            print(f"{a} - {b} = {a - b}")
        elif operation == '3' or operation == '*':
            print(f"{a} * {b} = {a * b}")
        elif operation == '4' or operation == '/':
            if b != 0:
                print(f"{a} / {b} = {a / b}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid choice. Please try again")
            
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    
    #Check if user wants to continue
    ch = input("\nDo you want to continue? (yes/no): ")
    print()

print("Thank you for using the Calculator!")
