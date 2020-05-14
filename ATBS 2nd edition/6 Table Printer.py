# Practice project from Automate the Boring Stuff - Chapter 6
# Done


def print_table(list_of_strings):

    # get longest word first and use that to adjust the column width to
    col_widths = [0] * len(list_of_strings)  # create list of zeros that's as long as there is lists in list_of_strings
    for i in range(len(list_of_strings)):
        col_widths[i] = len(max(list_of_strings[i], key=len))  # create list of longest words per sublist
    col_widths = max(col_widths)  # set col_widths to be the highest number in the list

    # printing out the well-organized table
    for i in range(len(list_of_strings)):
        print(f"{list_of_strings[i][0].rjust(col_widths)}", end="")  # print first row
    print()
    for i in range(len(list_of_strings)):
        print(f"{list_of_strings[i][1].rjust(col_widths)}", end="")  # print second row
    print()
    for i in range(len(list_of_strings)):
        print(f"{list_of_strings[i][2].rjust(col_widths)}", end="")  # print third row
    print()
    for i in range(len(list_of_strings)):
        print(f"{list_of_strings[i][3].rjust(col_widths)}", end="")  # print fourth row


# input for print_table
table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)
