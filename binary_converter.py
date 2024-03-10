def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return binary

def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal

def main():
    while True:
        print("Choose an option:")
        print("1. Convert decimal to binary")
        print("2. Convert binary to decimal")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            decimal = int(input("Enter a decimal number: "))
            print("Binary representation:", decimal_to_binary(decimal))
        elif choice == '2':
            binary = input("Enter a binary number: ")
            print("Decimal representation:", binary_to_decimal(binary))
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
