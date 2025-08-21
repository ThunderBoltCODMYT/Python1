import tkinter as tk

# Initialize main window
window = tk.Tk()
window.title("Simple Interest Calculator")
window.geometry("400x400")

# Create a frame for better layout
frame = tk.Frame(master=window, height=400, width=400, bg="#d0efff", relief=tk.GROOVE, borderwidth=5)
frame.pack(padx=10, pady=10)

# Input fields and labels
tk.Label(frame, text="Principal Amount:", bg="#d0efff").pack(pady=5)
entry_PrincipalAmount = tk.Entry(frame, bg="#0044FF", fg="black", width=20)
entry_PrincipalAmount.pack(pady=5)

tk.Label(frame, text="Rate of Interest (%):", bg="#d0efff").pack(pady=5)
entry_RateOfInterest = tk.Entry(frame, bg="#0044FF", fg="black", width=20)
entry_RateOfInterest.pack(pady=5)

tk.Label(frame, text="Time (Years):", bg="#d0efff").pack(pady=5)
entry_PeriodOfTimeInYears = tk.Entry(frame, bg="#0044FF", fg="black", width=20)
entry_PeriodOfTimeInYears.pack(pady=5)

# Result label
result_label = tk.Label(frame, text="", bg="#d0efff", fg='black', width=25)
result_label.pack(pady=10)

# Function to calculate Simple Interest
def SimpleInterestCalculatorMainFunction():
    try:
        P = float(entry_PrincipalAmount.get())
        R = float(entry_RateOfInterest.get())
        T = float(entry_PeriodOfTimeInYears.get())
        SI = (P * R * T) / 100
        result_label.config(text=f"Simple Interest is: {SI:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Button to trigger calculation
tk.Button(frame, text="Calculate", command=SimpleInterestCalculatorMainFunction).pack(pady=10)

# Start the GUI loop
window.mainloop()