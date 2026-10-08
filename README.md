# 🧹 Pandas Data Cleaning & EDA

A **foundation-level** data science project: take a messy sales dataset, clean it step by step with Pandas, then explore it with visualizations.

> 💡 **Learning goal:** Real-world data is always messy. Before any analysis or ML model, you must clean it. This project teaches you exactly that.

## 📌 Concepts covered
- Loading CSV data and first inspection (`head`, `info`, `describe`)
- Finding & handling **missing values** (when to fill vs when to drop)
- Removing **duplicate rows**
- Fixing **inconsistent text** ("Lahore" vs "lahore " vs "LAHORE")
- Converting **wrong data types** (price stored as text → number)
- **EDA**: `groupby`, `value_counts`, aggregations
- **Visualizations** with Matplotlib & Seaborn

## 📁 Files
| File | What it is |
|---|---|
| `data/sales_data.csv` | Messy sample dataset — missing values, duplicates and inconsistent entries **on purpose** |
| `data_cleaning_eda.ipynb` | Full cleaning + EDA notebook with outputs — read it top to bottom |
| `requirements.txt` | Needed Python packages |

## 🚀 How to run
```bash
pip install -r requirements.txt
jupyter notebook data_cleaning_eda.ipynb
```

## 🧠 After studying this, you should be able to explain
1. Why do we check `df.info()` first?
2. When should you fill missing values vs drop the row?
3. Why do text inconsistencies break `groupby` results?
4. What story does the "sales by city" chart tell?
