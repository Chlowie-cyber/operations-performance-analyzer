import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_operations_data(num_records=1000):
    """
    Generate synthetic operations performance dataset.
    """
    np.random.seed(42)
    start_date = datetime(2025, 1, 1)

    data = {
        "data": [start_date + timedelta(days=i % 30) for i in range(num_records)],
        "employee_id": np.random.randint(1000, 1100, num_records),
        "tasks_completed": np.random.randint(5, 20, num_records),
        "hours_worked": np.random.uniform(6, 10, num_records).round(2),
        "sla_met": np.random.choice([0, 1], num_records, p=[0.2, 0.8])
    }

    df = pd.DataFrame(data)

    df["productivity_rate"] = (df["tasks_completed"] / df["hours_worked"]).round(2)

    return df

if __name__ == "__main__":
    df = generate_operations_data()

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(BASE_DIR, "data")

    os.makedirs(DATA_PATH, exist_ok=True)

    # <-- SAVE THE FILE
    file_path = os.path.join(DATA_PATH, "operations_data.csv")
    df.to_csv(file_path, index=False)

    print("Dataset genenrated successfully!")