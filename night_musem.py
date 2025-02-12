def min_rotations(s):
    current = 'a'
    total_moves = 0

    for char in s:
        clockwise_dist = abs(ord(char) - ord(current))
        counterclockwise_dist = 26 - clockwise_dist
        total_moves += min(clockwise_dist, counterclockwise_dist)
        current = char
    print(total_moves)
s = input().strip()
min_rotations(s)
