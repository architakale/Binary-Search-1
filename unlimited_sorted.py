# Time Complexity : O(logn)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode: yes 
class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        low = 0
        high = 1
        
        while reader.get(high) < target:
            low = high
            high *= 2
        
        while low <= high:
            mid = (low + high)/2
            
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1