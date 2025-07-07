import random, math

#--------------------------------#
def generate_numbers(number_of_pexesos:int):

    if number_of_pexesos % 2 != 0:
        raise ValueError("Počet pexes musí byť párny.")

    half = number_of_pexesos // 2

    generated_num1 =random.sample(range(1,100), half)

    final_numbers = []

    for num in generated_num1:
        final_numbers.extend([num,num])

    random.shuffle(final_numbers)

    return final_numbers
#--------------------------------#
def build_pexeso_matrix(number_of_pexesos:int):

    matrix = []
    numbers = generate_numbers(number_of_pexesos)
    odmocnina = int(math.sqrt(len(numbers)))

    for i in range(0, len(numbers), odmocnina):
        row = []
        for j in range(i, i + odmocnina):
            row.append(numbers[j])
        matrix.append(row)
    
    return matrix
#--------------------------------#
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{num:2}" for num in row))
        #print(" ".join(f"{'#':>2}" for _ in row))
#--------------------------------#

# cisla = [48, 52, 3, 91, 31, 23, 
#          52, 23, 42, 22, 33, 60, 
#          92, 6, 34, 86, 80, 58, 
#          33, 34, 43, 86, 29, 60, 
#          48, 31, 92, 6, 29, 3, 
#          58, 42, 91, 43, 80, 22]

#--------------------------------#
def print_training(matrix):
    for row in matrix:
        #print(" ".join(f"{num:2}" for num in row))
        print(" ".join(f"{'#':>2}" for _ in row))
#--------------------------------#
def print_training(matrix, reveal_coords=[], revealed_positions=[]):
    for i in range(len(matrix)):
        row_display = []
        for j in range(len(matrix[0])): # iteracia cez vsetky stlpce
            if (i, j) in reveal_coords or (i, j) in revealed_positions:
                # zobraz skutočné číslo
                row_display.append(f"{matrix[i][j]:>2}")
            else:
                # zakryté políčko
                row_display.append(" #")
        print(" ".join(row_display))
    print()  # oddelenie výpisov
#--------------------------------#
def reveal_1(matrix, x1, y1, revealed_positions):
    #print("Aktuálny stav:")
    print_training(matrix, reveal_coords=[(x1, y1)], revealed_positions=revealed_positions)
#--------------------------------#
def reveal_2(matrix, x1, y1, x2, y2, revealed_positions):
    #print("Aktuálny stav:")
    print_training(matrix, reveal_coords=[(x1, y1), (x2, y2)], revealed_positions=revealed_positions)

#--------------------------------#
# FUNCTION CALL
#--------------------------------#
size = int(input("Select number of CARDS: "))

maticka = build_pexeso_matrix(size)

revealed_positions = []
print_matrix(maticka)

print()
print("Starting...")
print_training(maticka, revealed_positions=revealed_positions)

# MAIN GAME LOOP
while len(revealed_positions) != size:
    
    x1 = int(input('Suradnica[][y1]: '))
    y1 = int(input('Suradnica[x1][]: '))
    
    while (x1, y1) in revealed_positions:
        print("Táto pozícia je už odhalená. Zadaj inú.")
        x1 = int(input('Suradnica[][y1]: '))
        y1 = int(input('Suradnica[x1][]: '))
    print('*-------------*')
    reveal_1(maticka, x1, y1, revealed_positions)

    x2 = int(input('Suradnica[][y2]: '))
    y2 = int(input('Suradnica[x2][]: '))

    while (x1, y1) == (x2, y2):
        print("Táto pozícia je PRÁVE odhalená. Zadaj inú.")
        x2 = int(input('Suradnica[][y2]: '))
        y2 = int(input('Suradnica[x2][]: '))

    while (x2, y2) in revealed_positions:
        print("Táto pozícia je už odhalená. Zadaj inú.")
        x2 = int(input('Suradnica[][y2]: '))
        y2 = int(input('Suradnica[x2][]: '))
    print('*-------------*')
    reveal_2(maticka, x1, y1, x2, y2, revealed_positions)

    # kontrola páru
    if maticka[x1][y1] == maticka[x2][y2]:
        print("✅ Našiel si pár!")
        revealed_positions.extend([(x1, y1), (x2, y2)])
    else:
        print("❌ Nesprávny pár.")
    print('*-------------*')
    print("Revealed positions:")
    print(revealed_positions)

print('*------------*')
print("KONIEC Hry! 🎉")
print('*------------*')












