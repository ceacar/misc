import excalibur

@excalibur.debug
def least_operation_to_edit(str1, str2, str1_length, str2_length):
    """
    Insert
    Remove
    Replace


    Input:   str1 = "geek", str2 = "gesek"
    Output:  1
    We can convert str1 into str2 by inserting a 's'.

    Input:   str1 = "cat", str2 = "cut"
    Output:  1
    We can convert str1 into str2 by replacing 'a' with 'u'.

    Input:   str1 = "sunday", str2 = "saturday"
    Output:  3
    Last three and first characters are same.  We basically
    need to convert "un" to "atur".  This can be done using
    below three operations.
    Replace 'n' with 'r', insert t, insert a

    """
    if str1_length == 0:
        return str2_length
    elif str2_length == 0:
        return str1_length

    to_add = 1

    if str1[-1] == str2[-1]:
        to_add = 0


    #insert:str1 need to insert 1 char to match to str2
    insert_operation = least_operation_to_edit(str1, str2[:-1], str1_length, str2_length - 1)
    #remove: str1 need to remove 1 char to match to str2
    remove_operation = least_operation_to_edit(str1[:-1], str2, str1_length - 1, str2_length)
    #replace
    replace_operation = least_operation_to_edit(str1[:-1], str2[:-1], str1_length - 1, str2_length - 1)

    total_edit = to_add + min(insert_operation, remove_operation, replace_operation)

    return total_edit

if __name__ == "__main__":
    print(least_operation_to_edit("geek", "gesek", 4, 5))
    print(least_operation_to_edit("sunday", "saturday", 6, 8))
