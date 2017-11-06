m,n = map(int,input().split())

magazine = input()
note = input()

mag_words = [str(word) for word in magazine.split()]
note_words = [str(word) for word in note.split()]
flag = 0
for word in note_words:
    if word in mag_words:
        mag_words.remove(word)
    else:
        print("No")
        flag = 1
        break

if not flag:
    print("Yes")
