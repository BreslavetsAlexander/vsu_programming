import random


def bubble_sort(nums):
    s = True
    while s:
        s = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                s = True


nums_list = [random.randint(27, 82) for i in range(10)]
print(nums_list)
bubble_sort(nums_list)
print(nums_list)
