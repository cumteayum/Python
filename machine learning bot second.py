w1 = 21
w2 = 21

def correctOp(ip1, ip2):
	return 2 * ip1 + ip2

inputs = [[2,2], [5,3], [6,7]]

learningRate = 0.01

for i in range(10000):
	for ip in inputs:
		predictedOP = w1 *ip[0] + w2 * ip[1]
		correctOput = correctOp(ip[0], ip[1])

		cost = correctOput - predictedOP

		w1 += learningRate * ip[0] * cost
		w2 += learningRate * ip[1] * cost

print(w1)
print(w2)