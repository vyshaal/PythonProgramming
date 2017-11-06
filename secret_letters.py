def reverse(str):
    words = str.split(" ")
    words = [word[::-1] for word in words]
    str = " ".join(words)
    #print(str)
    return str

#reverse("Let's meet in the owlery    today ")
# reverse("Dumbledore army meeting at five")