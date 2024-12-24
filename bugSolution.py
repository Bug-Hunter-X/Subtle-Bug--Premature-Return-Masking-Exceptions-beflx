def improved_function(a, b):
    if a == 0:
        if b == 0:
            return 0 #Handles both a and b being 0
        else:
            return float('inf') #Handle cases where 'a' is 0 and 'b' is non-zero, returning infinity
    else:
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return b / a

result = improved_function(0, 10)
print(result) # Output: inf
result = improved_function(10, 0)
# Output: ZeroDivisionError: Division by zero
result = improved_function(0, 0)
print(result) # Output: 0