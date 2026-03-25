# Temperature Experiment Analysis

## Objective
The objective of this experiment is to analyze how temperature affects
response length, speed, and latency of the language model.

## Temperature Results

| Temperature | Tokens/sec | Latency | Response Length |
|-------------|------------|---------|----------------|
| 0.0 | 4.22 | 55.99 | 1522 |
| 0.2 | 5.31 | 47.29 | 1612 |
| 0.5 | 5.01 | 52.47 | 1675 |
| 0.7 | 4.84 | 51.07 | 1673 |
| 1.0 | 4.87 | 54.56 | 1808 |

## Analysis
- Temperature affects response length and generation speed.
- Temperature 0.2 produced the fastest response.
- Higher temperature produced longer responses.
- Temperature 0 produced more deterministic responses.
- Temperature 1 produced longer and more varied responses.

## Conclusion
- Temperature 0 is best for structured outputs.
- Temperature 0.2–0.5 provides balanced performance.
- Temperature 1 is best for creative text generation.