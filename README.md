# ML Foundations

Foundation notebooks for ML Engineering — NumPy, Pandas, Stats, Linear Algebra.

## Contents

| Week | Topic | Status |
|------|-------|--------|
| 1 | NumPy array thinking and vectorization | ✅ Complete |
| 2 | Pandas data cleaning pipelines | 🔄 Upcoming |

## Week 1 — NumPy Thinking

**Goal:** Demonstrate that vectorized operations outperform Python loops by 10–500x, 
and that broadcasting enables efficient operations on arrays of different shapes.

**Key notebook:** `week1/numpy_thinking.ipynb`

**What I built:**
- 10-problem vectorization benchmark (loop vs vectorized with timing comparisons)
- Broadcasting edge cases and real ML use cases
- Professional data processing class with error handling

**Biggest insight:** Broadcasting compares dimensions RIGHT to LEFT. 
Shape (5, 1) and (3,) are compatible — the (3,) is treated as (1, 3).

## How to Run

\`\`\`bash
git clone https://github.com/YOUR_USERNAME/ml-foundations.git
cd ml-foundations
python -m venv venv && source venv/bin/activate
pip install numpy jupyter
jupyter notebook week1/numpy_thinking.ipynb
\`\`\`