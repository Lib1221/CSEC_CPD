size = int(input())
line = list(map(int,input().split()))
for _ in range(int(input())):
    x,y = map(int,input().split())
    left_fly_bird = y-1
    right_fly_bird = line[x-1]-y
    if x > 1:
        line[x-2]+=left_fly_bird
    if x<size:
        line[x]+=right_fly_bird
    line[x-1]=0
for l in line:
    print(l)
