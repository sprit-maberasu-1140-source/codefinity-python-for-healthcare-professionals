import pandas as pd
import datetime
from datetime import datetime, timedelta

def get_upcoming_appointments(df):
    df = df.copy()
    df["AppointmentDate"] = pd.to_datetime(df["AppointmentDate"], errors="coerce")
    today = pd.to_datetime(datetime.today().date())
    next_7 = today + pd.Timedelta(days=7)
    upcoming = df[(df["AppointmentDate"] >= today) & (df["AppointmentDate"] <= next_7)]
    for _, row in upcoming.iterrows():
        if pd.isna(row["AppointmentDate"]):
            continue
        print(
            f"Reminder: {row['Patient']}, you have an appointment on "
            f"{row['AppointmentDate'].strftime('%Y-%m-%d')}."
        )

# Set up example data with dynamic dates relative to today
today = datetime.today().date()
data = {
    "Patient": ["John Doe", "Jane Roe", "Sam Green", "Lisa Ray"],
    "AppointmentDate": [
        (today + timedelta(days=7)).strftime("%Y-%m-%d"),   # 7 days from today
        (today + timedelta(days=3)).strftime("%Y-%m-%d"),   # 3 days from today
        (today + timedelta(days=15)).strftime("%Y-%m-%d"),  # 15 days from today
        today.strftime("%Y-%m-%d")                          # today
    ]
}
df = pd.DataFrame(data)

# Example usage:
get_upcoming_appointments(df)