table = [
    [" ", 1, 2, 3],
    [1, "-", "-", "-"],
    [2, "-", "-", "-"],
    [3, "-", "-", "-"]
]

[print(*i) for i in table]

sign = "X"

def check_victory_condition(table):
    victory_condition = any({
        table[1][1] == "0" and table[1][2] == "0" and table[1][3] == "0",
        table[1][1] == "X" and table[1][2] == "X" and table[1][3] == "X",
        table[2][1] == "0" and table[2][2] == "0" and table[2][3] == "0",
        table[2][1] == "X" and table[2][2] == "X" and table[2][3] == "X",
        table[3][1] == "0" and table[3][2] == "0" and table[3][3] == "0",
        table[3][1] == "X" and table[3][2] == "X" and table[3][3] == "X",
        table[1][1] == "0" and table[2][1] == "0" and table[3][1] == "0",
        table[1][1] == "X" and table[2][1] == "X" and table[3][1] == "X",
        table[1][2] == "0" and table[2][2] == "0" and table[3][2] == "0",
        table[1][2] == "X" and table[2][2] == "X" and table[3][2] == "X",
        table[1][3] == "0" and table[2][3] == "0" and table[3][3] == "0",
        table[1][3] == "X" and table[2][3] == "X" and table[3][3] == "X",
        table[1][1] == "0" and table[2][2] == "0" and table[3][3] == "0",
        table[1][1] == "X" and table[2][2] == "X" and table[3][3] == "X",
        table[3][1] == "0" and table[2][2] == "0" and table[1][3] == "0",
        table[3][1] == "X" and table[2][2] == "X" and table[1][3] == "X",
    })
    return victory_condition

def move(sign):
    row, column = 0, 0
    while row not in (1, 2, 3):
        row = int(input("Введите номер строки: "))
        if row not in (1, 2, 3):
            print("Возможные значения номера строки: 1, 2, 3")
    while column not in (1, 2, 3):
        column = int(input("Введите номер столбца: "))
        if column not in (1, 2, 3):
            print("Возможные значения номера столбца: 1, 2, 3")
    if table[row][column] == "-":
        table[row][column] = sign
        [print(*i) for i in table]
        return table
    else:
        print("Ячейка была выбрана ранее. Выберите другую ячейку.")
        move(sign)

count = 0
while not check_victory_condition(table) and count < 9:
    move(sign)
    sign = "0" if sign == "X" else "X"
    # if sign == "X":
    #     sign = "0"
    # else:
    #     sign = "X"
    count += 1
sign = "0" if sign == "X" else "X"
if count < 9:
    print(f"Победил игрок {sign}")
else:
    print("Ничья!")

input("Понравилась игра? ")