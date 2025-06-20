def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    pivot = int(len(nums) / 2)
    left_list = merge_sort(nums[0:pivot])
    right_list = merge_sort(nums[pivot:])
    return merge(left_list, right_list)

def merge(left_list, right_list):
    left_cursor = right_cursor = 0
    ret = []

    while left_cursor < len(left_list) and right_cursor < len(right_list):
        if left_list[left_cursor] < right_list[right_cursor]:
            ret.append(left_list[left_cursor])
            left_cursor += 1
        else:
            ret.append(right_list[right_cursor])
            right_cursor += 1

    ret.extend(left_list[left_cursor:])
    ret.extend(right_list[right_cursor:])

    return ret


print(merge_sort([1,5,3,2,8,7,6,4]))