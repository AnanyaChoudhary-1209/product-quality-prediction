
# Import libraries for data analysis and visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load our dataset
df = pd.read_csv("data/product_quality_synthetic_dataset.csv")

# Set a consistent style for the graphs
sns.set_theme(style="whitegrid")


# --------------------------------------------------
# 1. HISTOGRAMS: Understand target distributions
# --------------------------------------------------

# These are the three quality measurements we want to predict
targets = ["viscosity_cP", "density_g_cm3", "purity_pct"]

# Create one histogram for each target
for column in targets:
    plt.figure(figsize=(7, 4))
    sns.histplot(data=df, x=column, kde=True)

    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Number of samples")
    plt.tight_layout()

    # Display the graph
    plt.show()


# --------------------------------------------------
# 2. SCATTER PLOTS: Explore input-output relationships
# --------------------------------------------------

# Process parameters that may affect product quality
inputs = [
    "temperature_C",
    "pressure_bar",
    "reaction_time_min",
    "mixing_speed_rpm",
    "concentration_pct",
    "pH"
]

# Compare each input with each quality measurement
for feature in inputs:
    for target in targets:
        plt.figure(figsize=(6, 4))

        sns.scatterplot(data=df, x=feature, y=target, alpha=0.5)

        plt.title(f"{feature} vs {target}")
        plt.tight_layout()
        plt.show()


# --------------------------------------------------
# 3. CORRELATION HEATMAP: Examine linear relationships
# --------------------------------------------------

# Exclude the sample ID because it is only an identifier
numeric_df = df.drop(columns=["sample_id"])

# Calculate correlations between numerical columns
correlation_matrix = numeric_df.corr()

# Display the correlation matrix as a heatmap
plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,       # Display correlation values
    cmap="coolwarm",  # Color scale
    fmt=".2f",        # Show two decimal places
    vmin=-1,
    vmax=1
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
