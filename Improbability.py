def improbability(s,n):
    if n >= len(s):
        return "0"

    if n == 0:
        return s

    final_length = len(s) - n
    retain = final_length
    final_string = ""

    while len(final_string) != final_length:
        mini = s[0]
        for i in range(len(s)-retain+1):
            if s[i]<mini:
                mini = s[i]
        final_string += mini
        index = s.index(mini)
        s = s[index+1:]
        n = n-index
        retain = len(s) - n
        if n == 0:
            final_string += s

#    print(final_string)
    return final_string

#improbability("746209249",6)