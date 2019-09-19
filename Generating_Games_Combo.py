import itertools
import numpy as np

a = [[[[1,16] ,[8,9]] ,[[5,12] ,[4,13]]] ,[[[6,11],[3,14]],[[7,10],[2,15]]]]
b=[]
def generating_all_games(w,x,y,z):
  for h in range(len(a)):
    for i in range(len(a)):
      for j in range(len(a)):
        for k in range(len(a)):
          if a[h][i][j][k]!=a[w][x][y][z]:
            b.append([a[w][x][y][z],a[h][i][j][k]])         

for w in range(len(a)):
  for x in range(len(a)):
    for y in range(len(a)):
      for z in range(len(a)):
        generating_all_games(w,x,y,z)



def chunks(l,n):
  n = max(1,n)
  return((l[i:i+n] for i in range(0, len(l), n)))

tournament_games = list(chunks(b,15))
tournament_games[2][0], tournament_games[2][2] = tournament_games[2][2], tournament_games[2][0]

print(tournament_games)
'''
tounament_array = np.array_split(b,16)
tounament_array[2][0], tounament_array[2][2] = tounament_array[2][2], tounament_array[2][0]

print(tounament_array)
