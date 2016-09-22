word = raw_input("")
palin = 0
for i in range(0,len(word)):
    for j in range(0, len(word)):
        if word[i:len(word)-j] == word[i:len(word)-j][::-1]:
            if len(word[i:len(word)-j]) > palin:
                palin = len(word[i:len(word)-j])
print palin
