import pandas as pd

# Load benchmark results
bench = pd.read_csv("benchmarking/benchmark_results.csv")

# Load evaluation results
eval_df = pd.read_csv("evaluation/evaluation_results.csv")

# Average response length per model
avg_eval = eval_df.groupby("Model").mean(numeric_only=True).reset_index()

# Merge benchmark and evaluation
comparison = pd.merge(bench, avg_eval, on="Model")

print("\nFinal Model Comparison Table:")
print(comparison)

comparison.to_csv("experiments/results/final_model_comparison.csv", index=False)

print("\nSaved to experiments/results/final_model_comparison.csv")