import matplotlib.pyplot as plt
import numpy as np

# Given data
phat = 0.687
lower = 0.61
upper = 0.76

# Create the plot
fig, ax = plt.subplots(figsize=(8, 3))
ax.errorbar(phat, 0, xerr=[[phat - lower], [upper - phat]], fmt='o', color='blue', capsize=10, label='95% CI')
ax.scatter(phat, 0, color='red', zorder=5)
ax.text(phat, 0.05, f"p̂ = {phat:.3f}", ha='center', color='red', fontsize=10)

# Decorations
ax.set_xlim(0.5, 0.85)
ax.set_ylim(-0.5, 0.5)
ax.set_yticks([])
ax.set_title("95% Confidence Interval for AI Support Proportion", fontsize=12)
ax.set_xlabel("Proportion")
ax.axvline(lower, color='gray', linestyle='--', alpha=0.7)
ax.axvline(upper, color='gray', linestyle='--', alpha=0.7)
ax.text(lower, -0.1, f"{lower:.2f}", ha='center', fontsize=9)
ax.text(upper, -0.1, f"{upper:.2f}", ha='center', fontsize=9)
ax.legend()

# Save as PNG
plt.tight_layout()
plt.savefig("CI.png", dpi=300)
plt.close()
