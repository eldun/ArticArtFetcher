import tkinter as tk    # Standard binding to tk
import tkinter.ttk as ttk   # Binding to ttk submodule for new/prettier themed widgets

# Create window 
window = tk.Tk()
window.title("ArticArtFetcher")

mainframe = ttk.Frame(master=window)
mainframe.grid(column=0, row=0, ipadx=200, ipady=200, sticky=(tk.N, tk.E, tk.S, tk.W))
window.columnconfigure(index=0, weight=1)
window.rowconfigure(index=0, weight=1)

file_management_frame = ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=200, height=100)
file_management_frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(tk.N,tk.W))

artwork_criteria_frame = ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=200, height=100)
artwork_criteria_frame.grid(column=1, row=0, columnspan=3, rowspan=2, sticky=(tk.N,tk.E))


window.mainloop()
