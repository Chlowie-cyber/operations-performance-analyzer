import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------------------------
# Load Dataset
# ---------------------------------
def load_data():
    return pd.read_csv("../data/operations_data.csv")

# ---------------------------------
# Calculate Key KPIS
# ---------------------------------
def calculate_kpis(df):
    total_tasks = df["tasks_completed"].sum()
    avg_productivity = df["productivity_rate"].mean()
    sla_compliance = df["sla_met"].mean() * 100

    print("=== OPERATIONS KPI SUMMARY ===")
    print(f"Total Tasks Completed: {total_tasks}")
    print(f"Average Productivity Rate: {avg_productivity:.2f}")
    print(f"SLA Complaince Rate: {sla_compliance:.2f}%\n")

    return total_tasks, avg_productivity, sla_compliance

# ---------------------------------
# Create Visualizations
# ---------------------------------
def create_visualizations(df):
    # Get absolute project root
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    VISUALS_PATH = os.path.join(BASE_DIR, "visuals")
    os.makedirs(VISUALS_PATH, exist_ok=True)

    # Productivity Trend
    productivity_by_date = df.groupby("data")["productivity_rate"].mean()
    plt.figure()
    productivity_by_date.plot()
    plt.title("Average Productivity Trend")
    plt.xlabel("Date")
    plt.ylabel("Productivity Rate")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(VISUALS_PATH, "productivity_trend.png"))
    plt.close()

    # SLA Compliance Trend
    sla_rate = df.groupby("data")["sla_met"].mean()
    plt.figure()
    sla_rate.plot()
    plt.title("Daily SLA Compliance Rate")
    plt.xlabel("Date")
    plt.ylabel("SLA Compliance")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(VISUALS_PATH, "sla_trend.png"))
    plt.close()

    print("Visualizations saved successfully!")

# ---------------------------------
# Main Execution
# ---------------------------------
if __name__ == "__main__":
    df = load_data()
    calculate_kpis(df)
    create_visualizations(df)