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

        #Perform the operatio
