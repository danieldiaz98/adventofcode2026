data_file = open('elvesDataExample.txt', 'r', encoding="utf-8")

dial = 50
    
def main():
    count_zeros = 0
    for line in data_file:
        if dial == 0:
            count_zeros += 1
        print("DIAL= " + str(dial))
        print("ZEROS= " + str(count_zeros))
        print(line)
        if (line[0] == 'L'):
            number = int(line.replace('L',''))
            rotate_left_dial(number)
            
        elif (line[0] == 'R'):
            number = int(line.replace('R',''))
            rotate_right_dial(number)

    print(dial)
    print("ZEROS= " + str(count_zeros))
    
def rotate_left_dial(rotation):
    global dial
    dial = (dial - rotation) % 100
    return dial

def rotate_right_dial(rotation):
    global dial
    dial = (dial + rotation) % 100

if __name__ == "__main__":
    main()