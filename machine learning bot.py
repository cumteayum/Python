weight = 5

def getcorrect(input):
	return 10 *input

inputs = [5, 8, 10, 0]

for i in range(10000):
	for ip in inputs:
		predictedOutput = weight * ip
		correctOutput = getcorrect(ip)

		cost = correctOutput - predictedOutput
		weight += 0.01*cost 

print(weight)