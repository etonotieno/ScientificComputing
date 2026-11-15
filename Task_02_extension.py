
import numpy as np

# ==========================================
# PART C: HEAT WAVE ANALYSIS
# ==========================================

t = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])

print("\n========== PART C: HEAT WAVE ==========")

t2 = t + 5

print(f"Original mean: {t.mean():.2f} °C")
print(f"Heat-wave mean: {t2.mean():.2f} °C")

print(f"Original minimum: {t.min():.2f} °C")
print(f"Heat-wave minimum: {t2.min():.2f} °C")

print(f"Original maximum: {t.max():.2f} °C")
print(f"Heat-wave maximum: {t2.max():.2f} °C")

print(f"Original median: {np.median(t):.2f} °C")
print(f"Heat-wave median: {np.median(t2):.2f} °C")

print(f"Original standard deviation: {t.std():.3f}")
print(f"Heat-wave standard deviation: {t2.std():.3f}")

print(f"Original mean in Fahrenheit: {1.8*t.mean()+32:.2f} °F")
print(f"Heat-wave mean in Fahrenheit: {1.8*t2.mean()+32:.2f} °F")

print(f"Highest heat-wave temperature: {t2.max():.2f} °C")
print(f"Temperature increase: {(t2.mean()-t.mean()):.2f} °C")


# ==========================================
# PART E: VACCINE COLD-CHAIN MONITORING
# ==========================================

fridge = np.array([
    4.1, 4.3, 4.0, 4.2, 4.5, 5.0,
    5.8, 6.9, 7.6, 8.4, 8.9, 9.3,
    9.1, 8.2, 7.4, 6.6, 5.9, 5.2,
    4.8, 4.5, 4.4, 4.2, 4.1, 4.0
])

print("\n========== PART E: FRIDGE MONITORING ==========")

# Safe temperature range
bad = (fridge < 2) | (fridge > 8)

# Basic statistics
print(f"Mean: {fridge.mean():.2f} °C")
print(f"Median: {np.median(fridge):.2f} °C")
print(f"Minimum: {fridge.min():.2f} °C")
print(f"Maximum: {fridge.max():.2f} °C")
print(f"Standard deviation: {fridge.std():.3f}")

# Temperature extremes and their hours
print(f"Minimum occurred at hour: {np.argmin(fridge)+1}")
print(f"Maximum occurred at hour: {np.argmax(fridge)+1}")

# Identify unsafe readings
unsafe_hours = np.where(bad)[0] + 1

print(f"Unsafe readings: {bad.sum()}")
print(f"Unsafe hours: {unsafe_hours.tolist()}")

# Percentage outside safe range
print(f"Time outside safe range: {bad.mean():.1%}")

# Fahrenheit conversion
fahrenheit = 1.8 * fridge + 32

print("First 4 readings in Fahrenheit:",
      np.round(fahrenheit[:4], 2))

# Temperature changes between readings
changes = np.diff(fridge)

print(f"Largest temperature increase: {changes.max():.2f} °C")
print(f"Largest temperature decrease: {changes.min():.2f} °C")

# Overall fridge status
if bad.any():
    print("WARNING: Fridge temperature exceeded safe limits!")
else:
    print("Fridge temperature remained within safe limits.")
