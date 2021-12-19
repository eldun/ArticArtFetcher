import tkinter as tk
import tkinter.filedialog as filedialog
from tkinter.constants import NSEW, NE, NW, SE, SW, N, S, E, W   # Standard binding to tk
import tkinter.ttk as ttk   # Binding to ttk submodule for new/prettier themed widgets


def set_up_frames():

    # Set up Labelframes
    file_management_frame = ttk.Labelframe(master=mainframe, text="File Management", borderwidth=5, relief=tk.RIDGE)
    file_management_frame.grid(column=0, row=0, sticky=(NSEW), padx=10, pady=10)

    artwork_criteria_frame = ttk.Labelframe(master=mainframe, text="Artwork Criteria")
    artwork_criteria_frame.grid(column=1, row=0, sticky=(NSEW), padx=10, pady=10)

    log_frame = ttk.Labelframe(master=mainframe, text="Log", borderwidth=5, relief=tk.RIDGE)
    log_frame.grid(column=0, columnspan=2, row=1, sticky=(NSEW), padx=10, pady=10)

    button_frame = ttk.Frame(master=mainframe)
    button_frame.grid(column=1, row=2, padx=10, pady=5, sticky=tk.SE)

def set_up_file_management_section():

    # Directory selection
    output_directory="Placeholder Directory"
    ttk.Label(master=file_management_frame, text=f"Artwork Directory: {output_directory}").grid(column=0, row=0, sticky=W, padx=5, pady=5)
    ttk.Button(master=file_management_frame, text="Choose Directory", command=filedialog.askdirectory).grid(column=1, row=0, padx=5, pady=5, sticky=E)

    # 'Max size' options
    ttk.Label(master=file_management_frame, text="Max Picture Count").grid(column=0, row=1, sticky=W, padx=5, pady=5)
    ttk.Entry(master=file_management_frame).grid(column=1, row=1, padx=5, pady=5, sticky=E)

    ttk.Label(master=file_management_frame, text="Max Folder Size").grid(column=0, row=2, sticky=W, padx=5, pady=5)
    ttk.Entry(master=file_management_frame).grid(column=1, row=2, padx=5, pady=5, sticky=tk.W)
    folder_size_units_combobox = ttk.Combobox(master=file_management_frame)
    folder_size_units_combobox['values'] = ('MB', 'GB', 'TB')
    folder_size_units_combobox.state(['readonly'])
    folder_size_units_combobox.grid(column=2, row=2, padx=5, pady=5, sticky=W)

    # Auto Delete option
    ttk.Checkbutton(master=file_management_frame, text="Auto-delete old files").grid(column=0, row=3, padx=5, pady=5, sticky=W)

    # Update frequency option
    ttk.Label(master=file_management_frame, text="Download new files every: ").grid(column=0, row=4, sticky=W, padx=5, pady=5)
    ttk.Entry(master=file_management_frame).grid(column=1, row=4, padx=5, pady=5, sticky=tk.W)
    art_check_frequency_combobox = ttk.Combobox(master=file_management_frame)
    art_check_frequency_combobox['values'] = ('Hours', 'Days', 'Weeks', 'Months')
    art_check_frequency_combobox.state(['readonly'])
    art_check_frequency_combobox.grid(column=2, row=4, padx=5, pady=5, sticky=W)

    # Description file option
    ttk.Checkbutton(master=file_management_frame, text="Create artwork description file on desktop").grid(column=0, row=5, sticky=W, padx=5, pady=5)


    # Configure resizing for file management columns
    file_management_frame.columnconfigure(index=0, weight=0)
    file_management_frame.columnconfigure(index=1, weight=0)

    for row in range(file_management_frame.grid_size()[1]):
        file_management_frame.rowconfigure(row, weight=1, minsize=30)

def set_up_criteria_section():


    # has not been viewed much
    # date start
    # date end

    # Directory selection
    ttk.Label(master=file_management_frame, text=f"Artwork Directory: {output_directory}").grid(column=0, row=0, sticky=W, padx=5, pady=5)
    ttk.Button(master=file_management_frame, text="Choose Directory", command=filedialog.askdirectory).grid(column=1, row=0, padx=5, pady=5, sticky=E)

    # 'Max size' options
    ttk.Label(master=file_management_frame, text="Max Picture Count").grid(column=0, row=1, sticky=W, padx=5, pady=5)
    ttk.Entry(master=file_management_frame).grid(column=1, row=1, padx=5, pady=5, sticky=E)

    ttk.Label(master=file_management_frame, text="Max Folder Size").grid(column=0, row=2, sticky=W, padx=5, pady=5)
    ttk.Entry(master=file_management_frame).grid(column=1, row=2, padx=5, pady=5, sticky=tk.W)
    folder_size_units_combobox = ttk.Combobox(master=file_management_frame)
    folder_size_units_combobox['values'] = ('MB', 'GB', 'TB')
    folder_size_units_combobox.state(['readonly'])
    folder_size_units_combobox.grid(column=2, row=2, padx=5, pady=5, sticky=W)

    # Auto Delete option
    ttk.Checkbutton(master=file_management_frame, text="Auto-delete old files").grid(column=0, row=3, padx=5, pady=5, sticky=W)

    # Update frequency option
    ttk.Label(master=file_management_frame, text="Download new files every: ").grid(column=0, row=4, sticky=W, padx=5, pady=5)
    ttk.Entry(master=file_management_frame).grid(column=1, row=4, padx=5, pady=5, sticky=tk.W)
    art_check_frequency_combobox = ttk.Combobox(master=file_management_frame)
    art_check_frequency_combobox['values'] = ('Hours', 'Days', 'Weeks', 'Months')
    art_check_frequency_combobox.state(['readonly'])
    art_check_frequency_combobox.grid(column=2, row=4, padx=5, pady=5, sticky=W)

    # Description file option
    ttk.Checkbutton(master=file_management_frame, text="Create artwork description file on desktop").grid(column=0, row=5, sticky=W, padx=5, pady=5)


    # Configure resizing for file management columns
    file_management_frame.columnconfigure(index=0, weight=0)
    file_management_frame.columnconfigure(index=1, weight=0)

    for row in range(file_management_frame.grid_size()[1]):
        file_management_frame.rowconfigure(row, weight=1, minsize=30)



# Create window 
window = tk.Tk()
window.title("ArticArtFetcher")

# Create Main Content Frame
mainframe = ttk.Frame(master=window)
mainframe.grid(column=0, row=0, sticky=(tk.NSEW))

# Handle resize proportions
mainframe.columnconfigure(index=0, weight=0)
mainframe.columnconfigure(index=1, weight=1)
mainframe.rowconfigure(index=0, weight=3)
mainframe.rowconfigure(index=1, weight=1)

window.columnconfigure(index=0, weight=1)
window.rowconfigure(index=0, weight=1)

set_up_frames()
set_up_file_management_section()














# Artwork criteria section



ttk.Button(master=button_frame, text="Fetch Art").grid()



window.mainloop()
