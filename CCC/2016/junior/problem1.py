game = []
for i in range(6):
  game.append(raw_input(""))
won = 0
for i in range(6):
  if game[i-1] == "W":
      won +=1
if won == 0:
    print -1
elif won == 1 or won == 2:
    print 3
elif won == 3 or won == 4:
    print 2
else:
    print 1
