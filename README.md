# Pure Python ETL Pipeline & Department Analytics

A zero-dependency Data Pipeline built entirely in pure Python. This project extracts raw CSV employee data, handles malformed records and type-conversion errors gracefully, cleanses data using business logic, and generates department-level Key Performance Indicators (KPIs).

---

## 🌟 Key Features

* **Custom CSV Parser:** Custom line-by-line parsing using standard library functions (`strip()`, `split()`, `zip()`).
* **Robust Error Handling:**
  * Skipping malformed rows with line enumeration for logging.
  * `try-except` fallback handling for failed type conversions (`salary` -> `int`, `rating` -> `float`).
* **Data Cleansing:** Filters active employees meeting key performance thresholds (>= 3.5).
* **Department Analytics:**
  * Calculates headcount, average salary, and average rating.
  * Tracks individual top performers and highest department scores dynamically.
* **Zero External Dependencies:** No Pandas or third-party packages required—runs on native Python 3.x.

---

## 📁 Repository Structure

```text
pure-python-etl-pipeline/
├── main.py          # Complete ETL pipeline script
└── README.md        # Documentation
```

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/HadeeRehman/pure-python-etl-pipeline.git
   cd pure-python-etl-pipeline
