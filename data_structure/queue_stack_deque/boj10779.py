table = list(map(str, input().rstrip()))

stack = []  # 막대기 저장
previous_was_open = False

count = 0
for char in table:
    if char == "(":
        previous_was_open = True
        stack.append(["s", 0])

    if char == ")":
        if previous_was_open: # 레이저라는 뜻
            stack.pop()
            for stick in stack:
                stick[1] += 1
            previous_was_open = False
        else:
            stick, point = stack.pop()
            count += (point + 1)

print(count)
