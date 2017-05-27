from pprint import pprint


with open("gardenbot.log") as f:
    lines = f.readlines()
    lines = reversed(lines)
    for line in lines:
        log = list(line.split(";"))
        print(log)

