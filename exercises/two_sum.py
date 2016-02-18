def two_sum(nums, target):
    index_list = range(len(nums))
    for idx in index_list:
        first_num = nums[idx]
        for idx_j in range(idx+1,len(nums)):
            sec_num = nums[idx_j]
            num_sum = first_num + sec_num
            if target == num_sum:
                return [idx,idx_j]


