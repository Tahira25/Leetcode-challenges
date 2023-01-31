
import itertools


def challenge_1(nums, target):
    # target_list = [[nums[i]+nums[j]] = target for i,j in range(len(nums))] 
    # is this not possible in a list comprehension?
    for number in itertools.combinations(nums, 2) == target:
        print(for number in numbers [nums.index[number]])

    

print(challenge_1([1,2,3], 6))

# x=[1,2,3]
# print(list(itertools.combinations(x, 2)))