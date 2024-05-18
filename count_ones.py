#Kenneth Smith 
#11.2
#5-18-2024
# This program uses a recursive function that accepts an integer argument, n, and prints the number of 1 up to and including n.
#It also writes a non-recursive method that takes an integer argument, n, and prints the number of 1 up to and including n.

def count_ones(n):
    #Recursive function to count the number of 1s from 1 up to 'n'.
    # 1. Base case: If n is less than or equal to 0, return 0.
    # 2. Otherwise, recursively count the number of 1s in n // 10 (i.e., excluding the last digit).
    # 3. Increment the count by 1 if the last digit of n is 1.
    #4. Return the count.
    
    if n <= 0:
        return 0
    return count_ones(n // 10) + (n % 10 == 1)

def count_ones_non_recursive(n):
    #Non-recursive function to count the number of 1s from 1 up to 'n'. 
    #Method
    #1. Initialize count to 0.
    #2. Iterate from 1 to n (inclusive).
    #3. For each number, convert it to string and count the occurrences of '1'.
    #4. Add the count to the total count.
    #5. Return the total count.
    
    if n <= 0:
        return 0
    count = 0
    for i in range(1, n+1):
        count += str(i).count('1')
    return count

def test_count_ones_functions(n):
   #Testing the function
    if n <= 0:
        print("Invalid input! Input value must be greater than 0.")
        return
    print("Recursive function invoked:")
    recursive_count = count_ones(n)
    print(f"Total number of '1's from 1 to {n}: {recursive_count}\n")
    
    print("Non-recursive function invoked:")
    non_recursive_count = count_ones_non_recursive(n)
    print(f"Total number of '1's from 1 to {n}: {non_recursive_count}\n")

# Test examples
test_count_ones_functions(50)
test_count_ones_functions(500)
test_count_ones_functions(6000)
test_count_ones_functions(0)  # Should print an error message
test_count_ones_functions(-28)  # Should print an error message
