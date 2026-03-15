print(0.1+0.2==0.3)
print (1+0.1111111111111111111111111==1)
print(1+0.111111111111111111111111111111)
epsilon = 1.0

while (1.0 + epsilon / 2.0) != 1.0:
    epsilon = epsilon / 2.0

print(f"Machine epsilon: {epsilon}")
print(0.1+0.2)
