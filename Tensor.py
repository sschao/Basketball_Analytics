import numpy as np 

np.set_printoptions(threshold=np.inf)
#np.set_printoptions(suppress = True)

number_teams = 64
number_rounds = 6

T = np.zeros((number_teams,number_teams,number_rounds))
for r in range(number_rounds):
	for i in range(number_teams):
		for j in range(number_teams):
			bin_i = bin(i)[2:].zfill(7)
			bin_j = bin(j)[2:].zfill(7)
			if (bin_i[-r-1] != bin_j[-r-1]):
				if bin_i[:-r-1] == bin_j[:-r-1]:
					T[i,j,r] = 1 
			#a is zeros anyway

for x in range(number_rounds):
	np.savetxt("Tensor_round_" + str(x+1) +".csv", T[:,:,x], delimiter = ",", fmt ="%f")


#str(x+1) because Python indices start at 0 not 1. First round is 1