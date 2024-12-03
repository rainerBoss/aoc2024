with open("levels.txt") as file:
    data = file.read()

levels = [[int(n) for n in d.split(" ")] for d in data.split("\n")]

unsafe = 0
unsafe_lsit = []
safe = 0
def is_safe(level):
    index = 0
    _safe = True
    increasing = None
    while index != len(level) - 1:
        diff = abs(level[index] - level[index + 1]) 
        if increasing == None: increasing = level[index] < level[index + 1] 
        _increasing = level[index] < level[index + 1] 
        
        if level[index] == level[index + 1]:
            _safe = False
            break

        elif diff < 1 or diff > 3:
            # print(f"Level {level} was unsafe because {level[index]} and {level[index + 1]} is a difference of {diff}")
            _safe = False
            break

        elif increasing != _increasing:
            # print(f"Level {level} was unsafe because first two levels {level[0]} and {level[1]} were {"increasing" if increasing else "decreasing"} but {level[index]} and  {level[index + 1]} were {"increasing" if _increasing else "decreasing"}" )
            _safe = False
            break
        index += 1
    return _safe

for level in levels:
    if is_safe(level):
        safe += 1
    else:
        unsafe_lsit.append(level)
        unsafe += 1


for level in unsafe_lsit:
    index = 0
    while index != len(level):
        test_level = level.copy()
        test_level.pop(index)
        if is_safe(test_level):
            safe += 1 
            break
        index += 1

print(safe)
