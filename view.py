import tkinter as tk
from tkinter.constants import ANCHOR    # Standard binding to tk
import tkinter.ttk as ttk   # Binding to ttk submodule for new/prettier themed widgets

# Create window 
window = tk.Tk()
window.title("ArticArtFetcher")

# Create Main Content Frame
mainframe = ttk.Frame(master=window)
mainframe.grid(column=0, row=0, sticky=(tk.NSEW))

# Handle resize proportions
mainframe.columnconfigure(index=0, weight=1)
mainframe.columnconfigure(index=1, weight=1)
mainframe.rowconfigure(index=0, weight=3)
mainframe.rowconfigure(index=1, weight=1)

window.columnconfigure(index=0, weight=1)
window.rowconfigure(index=0, weight=1)


# Set up Frames
file_management_frame = ttk.Frame(master=mainframe, borderwidth=5, relief=tk.RIDGE)
file_management_frame.grid(column=0, row=0, sticky=(tk.NSEW))

artwork_criteria_frame = ttk.Frame(master=mainframe, borderwidth=5, relief=tk.RIDGE)
artwork_criteria_frame.grid(column=1, row=0, sticky=(tk.NSEW))

log_frame = ttk.Frame(master=mainframe, borderwidth=5, relief=tk.RIDGE)
log_frame.grid(column=0, row=1, sticky=(tk.NSEW))

button_frame = ttk.Frame(master=mainframe)
button_frame.grid(column=1, row=1)



# Populate frames with labels
ttk.Label(master=file_management_frame, text="File Management").grid()
ttk.Label(master=artwork_criteria_frame, text="Artwork Criteria").grid()
ttk.Label(master=log_frame, text="Log").grid()
ttk.Button(master=button_frame, text="Fetch Art").grid()



window.mainloop()
