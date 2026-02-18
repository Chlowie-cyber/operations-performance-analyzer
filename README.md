# Operations Performance Analyzer

**Operations Performance Analyzer** is a Python project that generates synthetic operations data, calculates key performance indicators (KPIs), and visualizes team productivity and SLA compliance trends. This project demonstrates data analysis, visualization, and Python scripting skills, suitable for AI, ML, and data-driven roles.

---

## 🚀 Features

- Generates a synthetic operations dataset with employees, tasks completed, hours worked, and SLA compliance.
- Calculates key KPIs:
  - Total tasks completed
  - Average productivity rate
  - SLA compliance rate
- Visualizes trends with charts:
  - Average productivity trend over time
  - Daily SLA compliance trend
- Structured project with `data`, `src`, and `visuals` folders.

---

## 📁 Folder Structure

operations-performance-analyzer/
│
├── data/ # Generated dataset (operations_data.csv)
├── src/ # Python scripts
│ ├── generate_data.py # Script to generate synthetic dataset
│ └── analyze_operations.py # Script to calculate KPIs and create visualizations
├── visuals/ # Saved charts (productivity and SLA trends)
├── .gitignore # Git ignore file
└── README.md # Project documentation


---

## 💻 How to Run

1. **Clone the repository:**
    git clone https://github.com/<your-username>/operations-performance-analyzer.git
    cd operations-performance-analyzer


2. **Create a virtual environment:**
    python -m venv .venv
  # Windows
    .venv\Scripts\activate
  # macOS/Linux
    source .venv/bin/activate


3. **Install dependencies:**
    pip install -r requirements.txt


4. **Generate synthetic dataset:**
    python src/generate_data.py


5. **Run analysis and create visualizations:**
    python src/analyze_operations.py

Charts will be saved in the visuals/ folder.

## KPI Summary:

Total Tasks Completed: 11937
Average Productivity Rate: 1.53
SLA Compliance Rate: 81.00%


Visualizations:

visuals/productivity_trend.png → Average productivity trend

visuals/sla_trend.png → Daily SLA compliance trend


## 🛠 Tech Stack

Python 3
Pandas (data manipulation)
NumPy (data generation)
Matplotlib (visualization)

## 📌 Author

Lehlogonolo Mpye
GitHub: https://github.com/<Chlowie-cyber>

