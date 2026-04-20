
def main():
    total_joltage = 0
    with open("data.txt") as file:
        for line in file:
            total_joltage += int(process_bank(line.strip()))
            print(total_joltage)

def process_bank(bank):
    mayor1 = max(bank)
    mayor2 = 0
    result = ""
    posicion_mayor = bank.index(mayor1)
    if (posicion_mayor != len(bank) - 1):
        x = bank[posicion_mayor + 1 :]
        mayor2 = max(x)
        result = str(mayor1) + str(mayor2)
        print("Joltage: " + result)
        return result
    else:
        x = bank[:posicion_mayor]
        mayor2 = max(x)
        result = str(mayor2) + str(mayor1)
        print("Joltage: " + result)
        return result

    return 0

if __name__ == "__main__":
    main()