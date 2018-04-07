def findMaxConsecutiveOnes(nums):
        maxnumcons = 0
        count = 0
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == 1:
                count = count + 1
            else:
                if count > maxnumcons:
                    maxnumcons = count
                count = 0
            i += 1
        if count > maxnumcons:
            return count
        return maxnumcons

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))  #3
