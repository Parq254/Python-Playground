
import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime, timedelta


class PeriodTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple GUI Period Tracker")
        self.period_dates = []

        self.label = tk.Label(master, text="Hello Genevieve : ) \n When was your last period (YYYY-MM-DD):")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Next Period", command=self.predict_next_period)
        self.button.pack()

        self.view_button = tk.Button(master, text="Last Period Dates", command=self.view_past_dates,bg='gray')
        self.view_button.pack()

    def predict_next_period(self):
        last_period_date = self.entry.get()
        last_period_date = datetime.strptime(last_period_date, '%Y-%m-%d')
        self.period_dates.append(last_period_date)
        cycle_length = 28  # average cycle length
        next_period_date = last_period_date + timedelta(days=cycle_length)
        messagebox.showinfo("Next Period Date", f"The next period is expected on {next_period_date.date()}")

    def view_past_dates(self):
        past_dates = "\n".join([date.strftime('%Y-%m-%d') for date in self.period_dates])
        messagebox.showinfo("Past Period Dates", past_dates)
    
    

root = tk.Tk()
root.geometry('500x500')
tracker = PeriodTracker(root)
root.mainloop()
