data_file = open('elvesDataExample.txt', 'r', encoding="utf-8")

dial = 50

''' //TODO: Improve code so that it can take higher values
Allowing the dial to complete more than one full rotation
Examples: L150 R250 '''
    
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
    difference = 0
    if (rotation == dial):
        dial = 0
        return dial
    if (rotation > dial):
        difference = (rotation - dial)
        dial = 100 - difference
        return dial
    if (rotation < dial):
        dial = dial - rotation
        return dial

def rotate_right_dial(rotation):
    global dial
    temp_dial = dial + rotation
    difference = 0
    if (temp_dial > 99):
        difference = temp_dial - 100
        dial = 0 + difference
    else :
        dial = temp_dial    
    return dial

if __name__ == "__main__":
    main()