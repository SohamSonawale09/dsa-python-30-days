# Problem Statement:
# Given a list of daily temperatures, return a list such that for each day, you tell how many days you would have to wait until a warmer temperature.

# If there is no future day with a warmer temperature, put 0 instead.

def dailyTemperatures(temps):
    stack = []                  # stores day index
    ans = [0] * len(temps)

    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            prev = stack.pop()
            ans[prev] = i - prev
        stack.append(i)

    return ans

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
