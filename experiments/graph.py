import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("experiments/results/temperature_results.csv")

plt.figure()
plt.plot(df["Temperature"], df["Tokens/sec"], marker='o')
plt.title("Temperature vs Tokens/sec")
plt.xlabel("Temperature")
plt.ylabel("Tokens/sec")
plt.savefig("experiments/results/temp_speed.png")

plt.figure()
plt.plot(df["Temperature"], df["Response Length"], marker='o')
plt.title("Temperature vs Response Length")
plt.xlabel("Temperature")
plt.ylabel("Response Length")
plt.savefig("experiments/results/temp_length.png")

print("Temperature plots saved.")