class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        
        if valueDiff < 0:
            return False

        window = {}
        l = 0
        width = valueDiff + 1

        for r in range(len(nums)):

            bucket = nums[r] // width

            if bucket in window:
                return True

            if (
                bucket - 1 in window and
                abs(nums[r] - window[bucket - 1]) <= valueDiff
            ):
                return True

            if (
                bucket + 1 in window and
                abs(nums[r] - window[bucket + 1]) <= valueDiff
            ):
                return True

            window[bucket] = nums[r]

            # maintain sliding window
            if r - l >= indexDiff:
                old_bucket = nums[l] // width
                del window[old_bucket]
                l += 1

        return False

        