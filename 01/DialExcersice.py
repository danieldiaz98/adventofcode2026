data_file = open('elvesDataExample.txt', 'r', encoding="utf-8")

dial = 50
count_zeros = 0

def main():
    global count_zeros
    for line in data_file:
        line = line.strip()
        if not line:
            continue
            
        if line[0] == 'L':
            number = int(line[1:])
            rotate_left_dial(number)
            
        elif line[0] == 'R':
            number = int(line[1:])
            rotate_right_dial(number)

    print("DIAL FINAL = " + str(dial))
    print("ZEROS TOTALES = " + str(count_zeros))
    
def rotate_left_dial(rotation):
    global dial, count_zeros
    tmp_dial = dial
    dial = (dial - rotation) % 100
    if tmp_dial > 0:
        if rotation >= tmp_dial:
            count_zeros += 1 + ((rotation - tmp_dial) // 100)
    else:
        count_zeros += rotation // 100

def rotate_right_dial(rotation):
    global dial, count_zeros
    tmp_dial = dial
    dial = (dial + rotation) % 100
    count_zeros += (tmp_dial + rotation) // 100

if __name__ == "__main__":
    main()