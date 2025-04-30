def is_shuffled_enough(arr):
    for i in range(len(arr) - 2):
        if arr[i+1] == arr[i] + 1 and arr[i+2] == arr[i+1] + 1:
            return False
        if arr[i+1] == arr[i] - 1 and arr[i+2] == arr[i+1] - 1:
            return False
    return True

# 🔢 Take input from the user
user_input = input("Enter 10 numbers: ")
numbers = list(map(int, user_input.strip().split(',')))

# ✅ Check if it's shuffled enough
if is_shuffled_enough(numbers):
    print("True")
else:
    print("False")
