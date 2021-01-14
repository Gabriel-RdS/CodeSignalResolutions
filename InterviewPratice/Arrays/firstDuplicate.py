"""
Google Challange: https://app.codesignal.com/interview-practice/task/pMvymcahZ8dY4g75q/description
"""

a = [2, 1, 3, 5, 3, 2]


def firstDuplicate(nums):
    num_set = set()
    no_duplicate = -1

    for i in range(len(nums)):

        if nums[i] in num_set:
            return nums[i]
        else:
            num_set.add(nums[i])

    return no_duplicate


print(firstDuplicate(a))
