
import math 

output, prior = 0, math.inf 

with open(r'input') as input: 
	for line in input: 
		n = int(line.strip())
		if n > prior: 
			output += 1 
		prior = n
		
input.close()

print(output)
