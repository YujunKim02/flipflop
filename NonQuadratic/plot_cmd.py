import matplotlib.pyplot as plt
import numpy as np

# Read the data from the .txt file
data_file = './plotdatanew/cmd.txt'

# Initialize empty lists to store the data
epochs = []
data1 = []
data2 = []

# Read the data from the file
with open(data_file, 'r') as file:
    lines = file.readlines()

# Extract the data from the lines
for i in range(0, len(lines), 2):
    epochs.append(int(lines[i].strip()))
    d1, d2 = map(float, lines[i+1].split())
    data1.append(d1)
    data2.append(d2)

# Divide data by their first elements to normalize
data1_normalized = [val / data1[0] for val in data1]
data2_normalized = [val / data2[0] for val in data2]

# Calculate the normalized functions 1/k and 1/k^2
k = epochs
function1 = [1/k_val for k_val in k]
function1_normalized = [val / function1[0] for val in function1]

function2 = [1/(k_val**2) for k_val in k]
function2_normalized = [val / function2[0] for val in function2]

# Plot the data in log-log scale
plt.figure(figsize=(10, 6))
plt.loglog(epochs, data1_normalized, label='RR (Normalized)')
plt.loglog(epochs, data2_normalized, label='Flipflop (Normalized)')

# Plot the normalized function 1/k as a dotted line
plt.loglog(k, function1_normalized, '--', label='1/k (Normalized)')

# Plot the normalized function 1/k^2 as a dotted line
plt.loglog(k, function2_normalized, '--', label='1/k^2 (Normalized)')

plt.xlabel('Epochs')
plt.ylabel('Normalized Values')
plt.title('Data and Functions in Log-Log Scale with Normalization')
plt.legend()
plt.grid(True)
plt.show()