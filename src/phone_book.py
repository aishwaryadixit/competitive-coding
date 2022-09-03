n = input()
n = int(n)
thisdict = {}
name = "an"
number = 12345

for i in range(n):
    try:
        name, number = input().split()
        thisdict[name] = number
    except (EOFError):
        break


na = "sample"
while na != "":
    try:
        na = str(input())
        if na in thisdict:
            for name in thisdict:
                if name == na and thisdict[name] != "":
                    print(name + "=" + thisdict[name])

                elif thisdict[name] == "":
                    print("Not Found")

                else:
                    continue
        else:
            print("Not found")

    except (EOFError):
        break
