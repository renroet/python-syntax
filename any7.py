def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    answer = False
    # YOUR CODE HERE 
    for num in nums:
        if num == 7:
            answer = True
    return answer

# print("should be true", any7([1, 2, 7, 4, 5]))
# print("should be false", any7([1, 2, 4, 5]))

