import tkinter as tk    # Standard binding to tk
import tkinter.ttk as ttk    # Binding to ttk submodule for new/prettier themed widgets
from tkinter.constants import NSEW, NE, NW, SE, SW, N, S, E, W   # Standard binding to tk
import tkinter.filedialog as filedialog
import tkinter.colorchooser as colorchooser


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

        configure_frame_row_spacing(self)


        
class ArtworkCriteriaFrame(ttk.Labelframe):

    def on_choose_color(self):
            colorchooser.askcolor()

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Date range
        current_row = 0
        ttk.Label(self, text="Date Range (Inclusive)").grid(column=0, row=current_row)
        ttk.Entry(self).grid(column=1, row=current_row)
        ttk.Label(self, text="-").grid(column=2, row=current_row)
        ttk.Entry(self).grid(column=3, row=current_row)

        # Artist
        current_row += 1
        ttk.Label(self, text="Artist").grid(column=0, row=current_row)
        ttk.Combobox(self).grid(column=1, row=current_row)

        # Art type(e.g. painting, sculpture, etc.)
        current_row += 1
        ttk.Label(self, text="Type").grid(column=0, row=current_row)
        ttk.Combobox(self).grid(column=1, row=current_row)

        # Color
        current_row += 1
        ttk.Label(self, text="Predominant Color").grid(column=0, row=current_row)
        ttk.Entry(self).grid(column=1, row=current_row)
        ttk.Button(self, command=self.on_choose_color).grid(column=2, row=current_row)

        # Rarity
        current_row += 1
        ttk.Checkbutton(self, text="Fetch rarely viewed art").grid(column=0, row=current_row)

        # Style (e.g. impressionist, abstract, etc.)
        current_row += 1
        ttk.Label(self, text="Style").grid(column=0, row=current_row)
        ttk.Combobox(self).grid(column=1, row=current_row)

        configure_frame_row_spacing(self)

        



class LogPaneFrame(ttk.Labelframe):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)   
 
class FetchButtonFrame(ttk.Frame):   
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)    






def configure_frame_row_spacing(frame):
    for row in range(frame.grid_size()[1]):
        frame.rowconfigure(row, weight=1, minsize=30)




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




