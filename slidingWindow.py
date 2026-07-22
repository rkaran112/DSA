# create the window then slide it towards the right. Then remove the
# first element and add the new element - (old_sum-first_num)+new_num
# cannot imagine how to max profit works

class SlidingWindow:
    def maxSum(self, nums, k):
        # fixed-size window: slide by dropping the leftmost and adding the new element
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        return max_sum

    def maxProfit(self, prices):
        # variable window: track the lowest price seen so far as the left edge
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

sw = SlidingWindow()
print(sw.maxSum([2,1,5,1,3,2], 3))
print(sw.maxProfit([7,1,5,3,6,4]))
