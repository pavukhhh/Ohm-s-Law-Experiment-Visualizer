# Ohm's Law Experiment Visualizer
# Class 11 Physics Project
# Formula: V = I * R  →  I = V / R

import matplotlib.pyplot as plt

print("=== Ohm's Law Experiment ===")
print("This program calculates current for given voltage and resistance.")
print()

# Take user input
R = float(input("Enter resistance (in ohms): "))

# Generate voltages from 0 to 10V
voltages = [v for v in range(0, 11)]  # 0, 1, 2, ... 10
currents = [v / R for v in voltages]

# Display results
print("\nVoltage (V)\tCurrent (I)")
for v, i in zip(voltages, currents):
    print(f"{v}\t\t{i:.2f}")

# Plot I vs V graph
plt.plot(voltages, currents, marker='o')
plt.title("Ohm's Law: I vs V (for fixed R)")
plt.xlabel("Voltage (V)")
plt.ylabel("Current (I in Amperes)")
plt.grid(True)
plt.show()
