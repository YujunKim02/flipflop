import numpy as np
import matplotlib.pyplot as plt

def f(x, a, b, c):
    return b * np.exp(c * x) - a * x

def calculate_parameters(mu, L):
    kappa = L / mu
    c = 0.5 * np.log(kappa)
    b = np.sqrt(mu * L) / c**2
    a = b * c
    return a, b, c

# Given values of mu and L
mu = 1
L = 100

# Calculate parameters a, b, and c based on the given conditions
a, b, c = calculate_parameters(mu, L)
print(a, b, c)
print(b*c**3*np.exp(c))
# Create x values in the domain [-3, 3]
x_values = np.linspace(-1.5, 1.5, 1000)

# Calculate corresponding y values using the function f(x)
y_values = f(x_values, a, b, c)

# Calculate the value of f(0)
f_at_0 = f(0, a, b, c)

# Plot the function
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='f(x)')
plt.axhline(y=f_at_0, color='red', linestyle='--', label='f(0)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x) on the domain [-1.5, -1.5]')
plt.legend()
plt.grid(True)
plt.show()