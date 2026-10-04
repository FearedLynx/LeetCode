class Solution(object):
    def maxProfit(self, prices):
        # prices - array
        # prices[i] - stock on day i
        # choose a single day to buy and a different day in the future to sell
        # return maximum profit you can achive from this transaction
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if i<j:
                    currentProfit = prices[j]-prices[i]
                    if currentProfit>maxProfit:
                        maxProfit = currentProfit
        if maxProfit>0:
            return maxProfit
        else:
            return 0

# TIME LIMIT EXCEEDED. 198 / 213 testcases passed

# second try

def profits(prices):
    # If I sold today, what's the most I could make?
    passed = []
    maks = 0
    for i in range(1, len(prices)):
        passed.append(prices[i-1])
        current = prices[i] - min(passed)
        if current>maks:
            maks = current
    return maks
arr = [7,1,5,3,6,4]
print(profits(arr))

# TIME LIMIT EXCEEDED. 199 / 213 testcases passed - min(passed) scans the list every day, so O(n^2)

# third try - O(n) time, O(1) memory

def profits3(prices):
    # If I sold today, what's the most I could make?
    passedMin = prices[0]
    maks = 0
    for i in range(1, len(prices)):
        if prices[i-1] < passedMin:
            passedMin = prices[i-1]
        current = prices[i] - passedMin
        if current>maks:
            maks = current
    return maks
arr = [7,1,5,3,6,4]
print(profits3(arr))