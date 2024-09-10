def can_jump(distances):
    max_jump = distances[0]  # maximum jump distance
    can_jump = False
    for i in range(1, len(distances)):
        if distances[i] > max_jump:
            can_jump = False       
            return "NO HE CAN'T"
        else:
            can_jump = True
    
    if (can_jump == True):
        return "YES HE CAN"


distances = list(map(int, input().split(',')))
print(distances)

# Output: Either "YES HE CAN" or "NO HE CAN'T"
print(can_jump(distances))
