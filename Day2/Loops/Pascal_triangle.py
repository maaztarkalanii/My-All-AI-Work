rows = 10
row = [1]

# width of the biggest number, so every cell can be the same size
biggest = 252                      # largest value in row 10
cell = len(str(biggest)) + 1       # digits + 1 gap space

for i in range(rows):
    # 1. Turn the row into text, each number in a fixed-width cell
    line = ""
    for number in row:
        line = line + str(number).center(cell)

    # 2. Indent: each row shifts by half a cell
    print(" " * ((rows - i) * cell // 2) + line)

    # 3. Build the next row
    next_row = [1]
    for j in range(len(row) - 1):
        next_row.append(row[j] + row[j + 1])
    next_row.append(1)

    # 4. Move to the next row
    row = next_row