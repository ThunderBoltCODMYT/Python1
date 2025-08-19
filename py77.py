import tkinter as tk
# Cerate  Window
root = tk.Tk()
root.title('Number Pad')
root.geometry('250x300')

# Create the Number Grid
nums = [[9.8,7],[6,5,4],[3,2,1],['#',0,'*']]

#Configure rows and columns to resize the window
for i in range(4):
    root.columnconfigure(i, weight = 1, minsize = 75)
    root.rowconfigure(i, weight = 1, minsize = 50)

#Create and Place Labels in the Grid
for i in range(4):
    for j in range(3):
        frame = tk.Frame(master = root, relief = tk.RAISED, borderwidth = 5, bg = "#d0efff")
        frame.grid(row = i, column = j, sticky = 'nsew')

        label = tk.Label(master = frame, text = nums[i][j], bg = "#d0efff", font = ("Arial", 18))
        label.pack(expand = True, fill = "both", padx = 10, pady = 10)

root.mainloop()