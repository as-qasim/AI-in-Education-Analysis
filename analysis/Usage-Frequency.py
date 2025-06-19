import matplotlib.pyplot as plt

# Data
labels = ["Never", "Rarely", "Occasionally", "Frequently"]
counts = [6, 9, 33, 110]
percentages = [c / 150 * 100 for c in counts]

# Plot
plt.figure(figsize=(8, 5))
bars = plt.bar(labels, percentages, color=['gray', 'silver', 'skyblue', 'green'])

# Add percentage labels on top of each bar
for bar, pct in zip(bars, percentages):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, f"{pct:.1f}%", 
             ha='center', va='bottom', fontsize=10)

plt.title("AI Tool Usage Frequency (n = 150)")
plt.ylabel("Percentage (%)")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("CI.png", dpi=300)
plt.show()
