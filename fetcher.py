from os import initgroups
import tkinter as tk    # Standard binding to tk
import tkinter.ttk as ttk    # Binding to ttk submodule for new/prettier themed widgets
from tkinter.constants import CENTER, EW, NSEW, NE, NW, SE, SW, N, S, E, W   # Standard binding to tk
import tkinter.filedialog as filedialog
import tkinter.colorchooser as colorchooser
import tkinter.scrolledtext as scrolledtext
from typing import Sized

class FileManagementFrame(ttk.Labelframe):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Populate file management section

        # Directory selection
        output_directory="Placeholder Directory"
        ttk.Label(self, text=f"Artwork Directory: {output_directory}").grid(column=0, row=0, sticky=W, columnspan=2)
        ttk.Button(self, text="Choose Directory", command=filedialog.askdirectory).grid(column=2, row=0)

        # 'Max pic count' options
        ttk.Label(self, text="Max Picture Count:").grid(column=0, row=1, sticky=W)
        ttk.Entry(self, width=7).grid(column=2, row=1)

        # Max folder size
        ttk.Label(self, text="Max Folder Size:").grid(column=0, row=2, sticky=W)
        max_size_frame = ttk.Frame(self)
        ttk.Entry(max_size_frame, width=4).grid(column=0, row=0)
        folder_size_units_combobox = ttk.Combobox(max_size_frame, width=2)
        folder_size_units_combobox['values'] = ('MB', 'GB', 'TB')
        folder_size_units_combobox.state(['readonly'])
        folder_size_units_combobox.grid(column=1, row=0)
        max_size_frame.grid(column=2, row=2)

        # Auto Delete option
        ttk.Label(self, text="Auto-delete old files:").grid(column=0, row=3, sticky=W)
        tk.Checkbutton(self, anchor=CENTER).grid(column=2, row=3, sticky=EW)

        # Update frequency option
        ttk.Label(self, text="Download new files every:").grid(column=0, row=4, sticky=W)

        update_frequency_frame = ttk.Frame(self)
        ttk.Entry(update_frequency_frame, width=3).grid(column=0, row=0)
        art_check_frequency_combobox = ttk.Combobox(update_frequency_frame, width=5)
        art_check_frequency_combobox['values'] = ('Hours', 'Days', 'Weeks', 'Months')
        art_check_frequency_combobox.state(['readonly'])
        art_check_frequency_combobox.grid(column=1, row=0)
        update_frequency_frame.grid(column=2,row=4)

        # Description file option
        ttk.Label(self, text="Create artwork description file on desktop:").grid(column=0, row=5, sticky=W, columnspan=2)
        tk.Checkbutton(self, anchor=CENTER).grid(column=2, row=5, sticky=EW)

        self.columnconfigure(index=0, weight=2, minsize=200)
        self.columnconfigure(index=1, weight=1, minsize=50)
        self.columnconfigure(index=2, weight=2, minsize=150)
        configure_frame_row_resize(self)
        add_widget_padding(self)


        
class ArtworkCriteriaFrame(ttk.Labelframe):

    def on_choose_color(self):
            colorchooser.askcolor()

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Date range        
        current_row = 0
        ttk.Label(self, text="Date Range (Inclusive)").grid(column=0, row=current_row, sticky=W)
        date_range = ttk.Frame(master=self)
        ttk.Entry(date_range, width=5).grid(column=0, row=current_row)
        ttk.Combobox(date_range, width=2).grid(column=1, row=current_row)
        ttk.Label(date_range, text="-").grid(column=2, row=current_row)
        ttk.Entry(date_range, width=5).grid(column=3, row=current_row)
        ttk.Combobox(date_range, width=2).grid(column=4, row=current_row)
        date_range.grid(column=2, row=current_row)

        # Artist
        current_row += 1
        ttk.Label(self, text="Artist").grid(column=0, row=current_row, sticky=W)
        ttk.Combobox(self, width=12).grid(column=2, row=current_row)

        # Art type(e.g. painting, sculpture, etc.)
        current_row += 1
        ttk.Label(self, text="Type").grid(column=0, row=current_row, sticky=W)
        ttk.Combobox(self, width=12).grid(column=2, row=current_row)

        # Color
        current_row += 1        
        ttk.Label(self, text="Predominant Color").grid(column=0, row=current_row, sticky=W)
        color_frame = ttk.Frame(self)
        ttk.Button(color_frame, command=self.on_choose_color).grid(column=0, row=0, sticky=EW)
        ttk.Entry(color_frame, width=7).grid(column=1, row=0, sticky=E)
        color_frame.grid(column=2, row=current_row)

        # Rarity
        current_row += 1
        ttk.Label(self, text="Fetch rarely viewed art").grid(column=0, row=current_row, sticky=W)
        tk.Checkbutton(self).grid(column=2, row=current_row, sticky=EW)

        # Style (e.g. impressionist, abstract, etc.)
        current_row += 1
        ttk.Label(self, text="Style").grid(column=0, row=current_row, sticky=W)
        ttk.Combobox(self, width=12).grid(column=2, row=current_row)

        # configure_frame_column_resize(self)


        self.columnconfigure(index=0, weight=2, minsize=200)
        self.columnconfigure(index=1, weight=1, minsize=50)
        self.columnconfigure(index=2, weight=2, minsize=150)

        configure_frame_row_resize(self)
        add_widget_padding(self)

        



class LogPaneFrame(ttk.Labelframe):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.scrolled_text = scrolledtext.ScrolledText(master=self)
        self.scrolled_text.configure(state=tk.DISABLED, background='light gray')
        self.scrolled_text.grid(column=0, row=0, sticky=NSEW)


        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=1)

    def log_message(self, message):
        self.scrolled_text.configure(state=tk.NORMAL)
        self.scrolled_text.insert(tk.END, 'hey')
        self.scrolled_text.configure(state=tk.DISABLED)


        



class FetchButtonFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        ttk.Button(self, text="Fetch", ).grid(column=0, row=0, sticky=NSEW)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)





def configure_frame_row_resize(frame):
    for row in range(frame.grid_size()[1]):
        frame.rowconfigure(row, weight=1, minsize=30)

def add_widget_padding(frame):
    for widget in frame.winfo_children():
        widget.grid_configure(padx=5, pady=5)
        add_widget_padding(widget)


class MainApplication(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
       
        self.parent = parent
        

        self.file_management_frame = FileManagementFrame(self, text="File Management", borderwidth=5, relief=tk.RIDGE)
        self.artwork_criteria_frame = ArtworkCriteriaFrame(self, text="Artwork Criteria", borderwidth=5, relief=tk.RIDGE)
        self.log_panel_frame = LogPaneFrame(self, text="Log", borderwidth=5, relief=tk.RIDGE)
        self.fetch_button_frame = FetchButtonFrame(self, borderwidth=5, relief=tk.RIDGE)


        self.file_management_frame.grid(column=0, row=0, sticky=(NSEW), padx=10, pady=10)
        self.artwork_criteria_frame.grid(column=1, row=0, sticky=(NSEW), padx=10, pady=10)
        self.log_panel_frame.grid(column=0, row=1, columnspan=2, padx=10, pady=10, sticky=NSEW)
        self.fetch_button_frame.grid(column=1, row=2, padx=10, pady=10, sticky=NSEW)

if __name__ == "__main__":
    # Create window
    window = tk.Tk()
    window.title("ArticArtFetcher")
    window.columnconfigure(index=0, weight=1)
    window.rowconfigure(index=0, weight=1)
    window.minsize(200,200)

    # Create frame for window
    main_application = MainApplication(parent=window)
    main_application.grid(column=0, row=0, sticky=(tk.NSEW))

    # Configure resize
    main_application.columnconfigure(index=0, weight=1, minsize= 300)
    main_application.columnconfigure(index=1, weight=1, minsize=300)
    main_application.rowconfigure(index=0, weight=1, minsize=300)
    main_application.rowconfigure(index=1, weight=1, minsize=150)
    main_application.rowconfigure(index=2, weight=1, minsize=100)


    window.mainloop()




