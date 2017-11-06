def edit_distance(str1,str2):
    if len(str1) == 0:
        return len(str2)
    elif len(str2) == 0:
        return len(str1)
    elif str1[-1] == str2[-1]:
        return edit_distance(str1[:len(str1)-1],str2[:len(str2)-1])
    else:
        return 1+min(edit_distance(str1[:len(str1) - 1], str2[:len(str2) - 1]),
                     edit_distance(str1[:len(str1)], str2[:len(str2) - 1]),
                     edit_distance(str1[:len(str1) - 1], str2[:len(str2)]))

print(edit_distance("sunday","saturday"))