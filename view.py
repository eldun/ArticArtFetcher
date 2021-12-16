import tkinter as tk
import tkinter.filedialog as filedialog
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


# Set up Labelframes
file_management_frame = ttk.Labelframe(master=mainframe, text="File Management", borderwidth=5, relief=tk.RIDGE)
file_management_frame.grid(column=0, row=0, sticky=(tk.NSEW), padx=10, pady=10)

artwork_criteria_frame = ttk.Labelframe(master=mainframe, text="Artwork Criteria")
artwork_criteria_frame.grid(column=1, row=0, sticky=(tk.NSEW), padx=10, pady=10)

log_frame = ttk.Labelframe(master=mainframe, text="Log", borderwidth=5, relief=tk.RIDGE)
log_frame.grid(column=0, columnspan=2, row=1, sticky=(tk.NSEW), padx=10, pady=10)

button_frame = ttk.Frame(master=mainframe)
button_frame.grid(column=1, row=2, padx=10, pady=5, sticky=tk.SE)


# Populate file management section
label_column = 0
entry_column = 1


ttk.Label(master=file_management_frame, text="Artwork Directory:").grid(column=label_column, row=0, sticky=tk.W, padx=5, pady=5)
ttk.Button(master=file_management_frame, text="Choose Directory", command=filedialog.askdirectory).grid(column=entry_column, row=0, sticky=tk.E)
ttk.Label(master=file_management_frame, text="Max Picture Count").grid(column=label_column, row=1, sticky=tk.W, padx=5, pady=5)
ttk.Label(master=file_management_frame, text="Max Folder Size").grid(column=label_column, row=2, sticky=tk.W, padx=5, pady=5)
ttk.Label(master=file_management_frame, text="Auto-delete Old Files").grid(column=label_column, row=3, sticky=tk.W, padx=5, pady=5)
ttk.Label(master=file_management_frame, text="Download New Files Every:").grid(column=label_column, row=4, sticky=tk.W, padx=5, pady=5)
ttk.Label(master=file_management_frame, text="Create Description File on Desktop").grid(column=label_column, row=5, sticky=tk.W, padx=5, pady=5)

# Configure resizing for file management columns
file_management_frame.columnconfigure(index=0, weight=1)
file_management_frame.columnconfigure(index=1, weight=1)

for row in range(file_management_frame.grid_size()[1]):
    file_management_frame.rowconfigure(row, weight=1, minsize=30)




ttk.Button(master=button_frame, text="Fetch Art").grid()



window.mainloop()
