s = str(input())

l = len(set(s.lower().replace(' ','')))

boolean = [True for char in s if char.isalpha()]

if all(boolean) and l == 26:
    print("pangram")
else:
    print("not pangram")