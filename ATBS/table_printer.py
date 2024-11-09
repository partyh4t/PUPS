
# table printer

tableData = [['apples', 'oranges', 'grapes', 'bananas'],
             ['Alice', 'Bob', 'Jim', 'Moe'],
             ['dogs', 'cats', 'moose', 'goose']]

col_width = []


def columnWidth(data, width):
    # calculates the width of each column
    for j in range(0, len(data)):
        counter = 0
        for i in range(0, len(data[0])):
            if len(data[j][i]) > counter:
                counter = len(data[j][i])
        width.append(counter)


columnWidth(tableData, col_width)

#prints out the data into a table format using the returned column width from columnWidth()
for i in range(0, len(tableData) + 1):
    for j in range(0, len(tableData)):
        print(tableData[j][i].rjust(col_width[j]), end=' ')
    print()


