#  SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  Super happy about having figured out this problem with very little help.
#  the key for this is to understand len(nums)-1 and adding the +1 to the num iteration.

def spy_game(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
        else:
            nums[i+1]
    else:
        return False



print(spy_game([1,2,4,0,0,7,5]))  # --> True
print(spy_game([1,0,2,4,0,5,7]))  # --> True
print(spy_game([1,7,2,0,4,5,0]))  # --> False
print(spy_game([0,0,7,9]))
