import numpy as np

# Create a random vector of size 20 with floats in the range 1-20
ran_vector = np.random.uniform(1, 20, 20)

# Reshape the array to 4 by 5
reshaped_one = ran_vector.reshape(4, 5)

# Replace the max in each row by 0 (axis=1)
reshaped_one[np.arange(len(reshaped_one)), reshaped_one.argmax(axis=1)] = 0

print("Random Vector:")
print(ran_vector)
print("\nReshaped Array:")
print(reshaped_one)