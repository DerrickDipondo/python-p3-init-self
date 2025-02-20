# Create a logic to find if the string has the required letters
# Iterate through the strings to rearrage the letters
# Display the outcome


# Create an empty array to store the string
from collections import deque

def swap(s):
    # Coun the number of "a's" and "b's"
    count_a = s.count("a")
    count_b = s.count("b")

    # If there are fewer than "a's" or "b's", it's impossible
    if count_a < 3 or count_b < 3:
        return -1 # Impossible case
    
    n = len(s)

    # Convert string to list for easy swapping
    s = list(s)

    def  swap_count(target):
        """ Helper function to count swaps needed to form a target pattern"""
        positions = deque([i for i in range(n) if s[1] == target])
        swaps = 0
        i = 0
        while positions:
            target_index = positions.popleft()
            swaps += abs(target_index -1)
        return swaps
    
    # Find swaps needed to group "aaa" and "bbb"
    swap_count("a")
    swap_count("b")

    # Example usage
print(swap("ababab"))
print(swap("aaa"))
print(swap("abababababaaa"))