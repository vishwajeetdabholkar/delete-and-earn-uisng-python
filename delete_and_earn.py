def maxPoints(elements):
    # Write your code here
    count = {}
    length = 0
    for num in elements:
        count.setdefault(num, 0)
        count[num] += num
        length = max(num, length)
    points = [0] * (length + 1)
    dp = [0] * (length + 2)
    for k, v in count.items():
        points[k] = v
    result = 0
    for i in range(len(points)):
        if i == 0:
            dp[i+1] = points[i]
        else:
            dp[i+1] = max(dp[i], dp[i-1] + points[i])
        result = max(dp[i+1], result)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    elements_count = int(input().strip())

    elements = []

    for _ in range(elements_count):
        elements_item = int(input().strip())
        elements.append(elements_item)

    result = maxPoints(elements)

    fptr.write(str(result) + '\n')

    fptr.close()
