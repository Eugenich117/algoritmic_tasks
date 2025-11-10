s = input().strip()
n = len(s)
LEFT = 0
RIGHT = 1

left_cost = 0
right_cost = 10**9

for char in s:
    if char == 'L':
        new_left = min(left_cost + 1, right_cost + 2)
        new_right = min(left_cost + 1, right_cost)
    elif char == 'R':
        new_left = min(left_cost, right_cost + 1)
        new_right = min(left_cost + 1, right_cost + 1)
    else:  # 'B'
        new_left = min(left_cost + 1, right_cost + 2)
        new_right = min(left_cost + 2, right_cost + 1)
    left_cost, right_cost = new_left, new_right

answer = min(left_cost + 1, right_cost)
print(answer)