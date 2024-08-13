def print_pyramid(n):
    # Loop through each level of the pyramid
    for i in range(1, n + 1):
        # Print spaces for alignment
        print(' ' * (n - i), end='')
        # Print stars
        print('*' * (2 * i - 1))

def main():
    # Get user input
    while True:
        try:
            n = int(input("Enter the number of levels for the pyramid: "))
            if n > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    # Print the pyramid pattern
    print_pyramid(n)

if __name__ == '__main__':
    main()
