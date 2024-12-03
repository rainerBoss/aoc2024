with open("levels.txt") as file:
    data = file.read()
    levels = [[int(n) for n in d.split(" ")] for d in data.split("\n")]
    
    unsafe = 0
    safe = 0
    for level in levels:
        index = 0
        _safe = True
        increasing = None 
        while index != len(level) - 1:
            if level[index] == level[index + 1]:
                unsafe += 1
                _safe = False
                break
            diff = abs(level[index] - level[index + 1]) 
            if diff < 1 or diff > 3:
                # print(f"Level {level} was unsafe because {level[index]} and {level[index + 1]} is a difference of {diff}")
                unsafe += 1
                _safe = False
                break
            if increasing == None:
                increasing = level[index] < level[index + 1] 
            else:
                _increasing = level[index] < level[index + 1] 
                if increasing != _increasing:
                    # print(f"Level {level} was unsafe because first two levels {level[0]} and {level[1]} were {"increasing" if increasing else "decreasing"} but {level[index]} and  {level[index + 1]} were {"increasing" if _increasing else "decreasing"}" )
                    unsafe += 1
                    _safe = False
                    break
            index += 1
        if _safe:
            # print(f"Level {level} was safe")
            safe += 1

    print(unsafe) 
    print(safe) 
