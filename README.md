# 📈 Predicting Price Movements from News Sentiment — Week 1

A structured weekly project exploring how financial news headlines influence asset price movements.  
Week 1 focuses on **environment setup**, **data loading**, and **Exploratory Data Analysis (EDA)**.

---

## 🎯 Objectives (Week 1)

- Set up a reproducible Python environment  
- Prepare Git branching structure  
- Perform EDA on news headlines dataset:
  - Descriptive statistics (headline lengths, nulls)
  - Publisher activity distribution
  - Time-series trends (daily/hourly frequency)
  - Text analysis (keywords, bigrams, basic topic clustering)
- Save plots + processed data for next tasks

---

## 🚀 How to Run This Project

1. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Start Jupyter Lab**

   ```bash
   jupyter lab
   ```

4. **Run the Analysis**
   Open `notebooks/01_data_overview.ipynb` to see the interactive analysis.
   
   Alternatively, you can use the modular scripts in `src/`:
   ```python
   from src.data_loader import load_csv_memory_friendly
   from src.eda_helpers import plot_top_publishers
   
   df = load_csv_memory_friendly("data/raw/raw_analyst_ratings.csv")
   plot_top_publishers(df)
   ```

---

## 🗂 Project Structure

```
.
├── data/
│   ├── raw/
│   │   └── raw_analyst_ratings.csv
│   └── processed/
│       └── eda_outputs/
├── notebooks/
│   └── 01_data_overview.ipynb
├── src/
│   ├── data_loader.py
│   ├── text_cleaning.py
│   └── eda_helpers.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Key Insights (Week 1)

### Top Publishers
The dataset is dominated by a few key publishers, indicating a concentration of financial news sources.
- **Paul Quintaro**
- **Lisa Levin**
- **Benzinga Newsdesk**

### Headline Analysis
- **Headline Length**: The distribution of headline lengths is approximately normal with a mean around 73 characters.
- **Common Keywords**: Frequent terms include "stocks", "hit", "highs", reflecting the market-focused nature of the dataset.

### Publication Trends
- **Time of Day**: Publication activity peaks during market hours.
- **Weekly Pattern**: Activity is significantly higher on weekdays compared to weekends.

---

## 🔀 Branching Strategy

| Branch   | Purpose                              |
| -------- | ------------------------------------ |
| `main`   | Stable, reviewed code                |
| `task-1` | Environment setup + EDA              |
| `task-2` | Technical indicators, price pipeline |
| `task-3` | Sentiment analysis + correlation     |





