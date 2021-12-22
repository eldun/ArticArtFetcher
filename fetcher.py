import tkinter as tk    # Standard binding to tk
import tkinter.ttk as ttk    # Binding to ttk submodule for new/prettier themed widgets
from tkinter.constants import NSEW, NE, NW, SE, SW, N, S, E, W   # Standard binding to tk
import tkinter.filedialog as filedialog


class FileManagementFrame(ttk.Labelframe):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Populate file management section

        # Directory selection
        output_directory="Placeholder Directory"
        ttk.Label(self, text=f"Artwork Directory: {output_directory}").grid(column=0, row=0, sticky=W, padx=5, pady=5)
        ttk.Button(self, text="Choose Directory", command=filedialog.askdirectory).grid(column=1, row=0, padx=5, pady=5, sticky=E)

        # 'Max size' options
        ttk.Label(self, text="Max Picture Count").grid(column=0, row=1, sticky=W, padx=5, pady=5)
        ttk.Entry(self).grid(column=1, row=1, padx=5, pady=5, sticky=E)

        ttk.Label(self, text="Max Folder Size").grid(column=0, row=2, sticky=W, padx=5, pady=5)
        ttk.Entry(self).grid(column=1, row=2, padx=5, pady=5, sticky=tk.W)
        folder_size_units_combobox = ttk.Combobox(self)
        folder_size_units_combobox['values'] = ('MB', 'GB', 'TB')
        folder_size_units_combobox.state(['readonly'])
        folder_size_units_combobox.grid(column=2, row=2, padx=5, pady=5, sticky=W)

        # Auto Delete option
        ttk.Checkbutton(self, text="Auto-delete old files").grid(column=0, row=3, padx=5, pady=5, sticky=W)

        # Update frequency option
        ttk.Label(self, text="Download new files every: ").grid(column=0, row=4, sticky=W, padx=5, pady=5)
        ttk.Entry(self).grid(column=1, row=4, padx=5, pady=5, sticky=tk.W)
        art_check_frequency_combobox = ttk.Combobox(self)
        art_check_frequency_combobox['values'] = ('Hours', 'Days', 'Weeks', 'Months')
        art_check_frequency_combobox.state(['readonly'])
        art_check_frequency_combobox.grid(column=2, row=4, padx=5, pady=5, sticky=W)

        # Description file option
        ttk.Checkbutton(self, text="Create artwork description file on desktop").grid(column=0, row=5, sticky=W, padx=5, pady=5)







        # Configure resizing for file management columns
        self.columnconfigure(index=0, weight=0)
        self.columnconfigure(index=1, weight=0)

        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1, minsize=30)


        
class ArtworkCriteriaFrame(ttk.Labelframe):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

class LogPaneFrame(ttk.Labelframe):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)   
 
class FetchButtonFrame(ttk.Frame):   
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)    

class MainApplication(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
       
        self.parent = parent
        

        self.file_management_frame = FileManagementFrame(self, text="File Management", borderwidth=5, relief=tk.RIDGE)
        self.artwork_criteria_frame = ArtworkCriteriaFrame(self,  text="Artwork Criteria", borderwidth=5, relief=tk.RIDGE)
        self.log_panel_frame = LogPaneFrame(self,  text="Log", borderwidth=5, relief=tk.RIDGE)
        self.fetch_button_frame = FetchButtonFrame(self, borderwidth=5, relief=tk.RIDGE)

        self.file_management_frame.grid(column=0, row=0, sticky=(NSEW), padx=10, pady=10)
        self.artwork_criteria_frame.grid(column=1, row=0, sticky=(NSEW), padx=10, pady=10)
        self.log_panel_frame.grid(column=0, row=1, sticky=(NSEW), padx=10, pady=10)
        self.fetch_button_frame.grid(column=1, row=2, padx=10, pady=5, sticky=NSEW)

if __name__ == "__main__":
    # Create window
    window = tk.Tk()
    window.title("ArticArtFetcher")
    window.columnconfigure(index=0, weight=1)
    window.rowconfigure(index=0, weight=1)
    window.minsize(200, 200)

    # Create frame for window
    main_application = MainApplication(parent=window)
    main_application.grid(column=0, row=0, sticky=(tk.NSEW))

    # Configure resize
    main_application.columnconfigure(index=0, weight=1)
    main_application.columnconfigure(index=1, weight=1)
    main_application.rowconfigure(index=0, weight=1)
    main_application.rowconfigure(index=1, weight=1)
    main_application.rowconfigure(index=2, weight=1)


    window.mainloop()