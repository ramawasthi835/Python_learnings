# PROGRAM TO CHECK WHETHER A NUMBER IS PRIME

# Take input from the user
a = int(input("Enter a number to check if it's prime: "))

# Handle edge cases
if a <= 1:
    print("Not prime")
else:
    # Assume number is prime unless a divisor is found
    is_prime = True
    for i in range(2, a):
        if a % i == 0:
            is_prime = False
            break
    
    # Display result
    if is_prime:
        print("Prime")
    else:
        print("Not prime")
