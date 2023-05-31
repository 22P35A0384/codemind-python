# Function to reverse the prefix of a string
def reverse_prefix(string, length):
    return string[:length][::-1] + string[length:]

# Number of test cases
T = int(input())

# Iterate over test cases
for _ in range(T):
    # Read input for current test case
    N, K = map(int, input().split())
    S_prime = input().strip()

    # Initialize original string
    S = ""

    # Reverse the prefix in each step
    for i in range(K, 0, -1):
        S_prime = reverse_prefix(S_prime, i)

    # Output the original string
    print(S_prime)
