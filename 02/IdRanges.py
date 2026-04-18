
def main():
    line = ""
    with open("data.txt") as file:
        line = file.read()

    id_ranges = line.split(",")
    ranges = [process_range(i) for i in id_ranges]
    total = 0
    for r in ranges:
        for i in r:
            if not is_valid(i):
                total += i
    print(ranges)
    print("TOTAL= " + str(total))


def process_range(id_range):
    l,r = id_range.split("-")
    return range(int(l),int(r) + 1)

def is_valid(r):
    s = str(r)
    if len(s) % 2 == 1:
        return True
    middle = len(s) // 2
    return s[:middle] != s[middle:]

if __name__ == "__main__":
    main()