n = int(input())
events = list(map(int, input().split()))

officers = 0
untreated = 0

for event in events:
    if event == -1:
        if officers > 0:
            officers -= 1
        else:
            untreated += 1
    else:
        officers += event

print(untreated)
