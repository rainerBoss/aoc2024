numbers = []
good_strings = []

with open("data.txt", "r") as file:
    data = file.read()
    strings = data.split("mul(")
    for string in strings:
        # print("STR: ", string)
        mul = ["", ""]
        index = 0
        if not string[index].isnumeric():
            # print("First is not nummeric, contunue the loop")
            continue
        while string[index] != ",":
            # print("While loop 1: ", string[index])
            if string[index].isnumeric():
                # print("Char is nummeric, adding to mul 0")
                mul[0] += string[index]
                index += 1
            else: break
        if string[index] != ",": continue
        # print("MUL 0: ", mul)
        index += 1
        while string[index] != ")":
            # print("While loop 2: ", string[index])
            if string[index].isnumeric():
                # print("Char is nummeric, adding to mul 1")
                mul[1] += string[index]
                index += 1
            else: break
        if string[index] != ")": continue
        # print("MUL 1: ", mul)
        # good_strings.append(f"mul({string[0:index+1]}")
        mul_them = int(mul[0]) * int(mul[1])
        # print(mul_them)
        numbers.append(mul_them)


print("SUM: ", sum(numbers))