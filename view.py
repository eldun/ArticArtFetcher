from doctest import master
import fractions
from multiprocessing.sharedctypes import Value
from operator import truediv
import tkinter as tk    # Standard binding to tk
import tkinter.ttk as ttk    # Binding to ttk submodule for new/prettier themed widgets
from tkinter.constants import CENTER, EW, NSEW, NE, NW, SE, SW, N, S, E, W   # Standard binding to tk
import tkinter.filedialog as filedialog
import tkinter.colorchooser as colorchooser
import tkinter.scrolledtext as scrolledtext
from turtle import bgcolor, color


class FileManagementFrame(ttk.Labelframe):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Populate file management section

        # Directory selection
        self.output_directory = tk.StringVar()
        self.output_directory.set("No Directory Selected")
        tk.Label(self, text="Artwork Directory: ").grid(column=0, row=0, sticky=W)
        tk.Label(self, textvariable=self.output_directory).grid(column=1, row=0, sticky=W)
        ttk.Button(self, text="Choose Directory", command=self.choose_directory).grid(column=2, row=0)

        # 'Max pic count' options
        ttk.Label(self, text="Max Picture Count:").grid(column=0, row=1, sticky=W)
        self.max_picture_count_entry = ttk.Entry(self, width=7)
        self.max_picture_count_entry.grid(column=2, row=1)

        int_validaiton_command = self.max_picture_count_entry.register(on_int_entry_edited)
        self.max_picture_count_entry.config(validate='all', validatecommand=(int_validaiton_command, '%P'))


        # Max folder size
        ttk.Label(self, text="Max Folder Size:").grid(column=0, row=2, sticky=W)
        max_size_frame = ttk.Frame(self)

        self.max_folder_size_entry = ttk.Entry(max_size_frame, width=4)
        self.max_folder_size_entry.grid(column=0, row=0)
        self.max_folder_size_entry.config(validate='all', validatecommand=(int_validaiton_command, '%P'))


        self.folder_size_units_combobox = ttk.Combobox(max_size_frame, width=2)
        self.folder_size_units_combobox['values'] = ('MB', 'GB', 'TB')
        self.folder_size_units_combobox.state(['readonly'])
        self.folder_size_units_combobox.grid(column=1, row=0)

        max_size_frame.grid(column=2, row=2)

        # Auto Delete option
        ttk.Label(self, text="Auto-delete old files:").grid(column=0, row=3, sticky=W)
        # For whatever reason, I have to create a variable to hold the value of the checkbox instead of just getting the widget itself
        self.auto_delete_checkbutton_var = tk.BooleanVar()
        self.auto_delete_checkbutton = tk.Checkbutton(self, anchor=CENTER, variable=self.auto_delete_checkbutton_var)
        self.auto_delete_checkbutton.grid(column=2, row=3, sticky=EW)

        # Update frequency option
        ttk.Label(self, text="Download new files every:").grid(column=0, row=4, sticky=W)

        update_frequency_frame = ttk.Frame(self)
        self.update_frequency_entry = ttk.Entry(update_frequency_frame, width=3, validate=tk.ALL, validatecommand=(int_validaiton_command, '%P'))
        self.update_frequency_entry.grid(column=0, row=0)
        self.art_check_frequency_combobox = ttk.Combobox(update_frequency_frame, width=5)
        self.art_check_frequency_combobox['values'] = ('Hours', 'Days', 'Weeks', 'Months')
        self.art_check_frequency_combobox.state(['readonly'])
        self.art_check_frequency_combobox.grid(column=1, row=0)
        update_frequency_frame.grid(column=2,row=4)

        # Description file option
        
        ttk.Label(self, text="Create artwork description file on desktop:").grid(column=0, row=5, sticky=W, columnspan=2)
        # For whatever reason, I have to create a variable to hold the value of the checkbox instead of just getting the widget itself
        self.create_description_checkbutton_var = tk.BooleanVar()
        self.create_description_checkbutton = tk.Checkbutton(self, anchor=CENTER, variable=self.create_description_checkbutton_var)
        self.create_description_checkbutton.grid(column=2, row=5, sticky=EW)

        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        self.columnconfigure(index=2, weight=1)

        configure_frame_row_resize(self)
        
        add_widget_padding(self)

    def choose_directory(self):
        dir = filedialog.askdirectory(mustexist=True)

        self.output_directory.set(dir)

        
class ArtworkCriteriaFrame(ttk.Labelframe):

    def on_choose_color(self):
            color = colorchooser.askcolor()
            rgb = color[0]
            hex = color[1]

            self.choose_color_entry_var.set(str(hex))

            if hex == None:
                self.choose_color_button.config(bg='gray')
                return
            
            else:
                self.choose_color_button.config(bg=hex)


    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Date range        
        current_row = 0
        ttk.Label(self, text="Date Range (Inclusive)").grid(column=0, row=current_row, sticky=W)
        date_range = ttk.Frame(master=self)
        self.date_start_entry = ttk.Entry(date_range, width=5)
        int_validation_command = self.date_start_entry.register(on_int_entry_edited)
        self.date_start_entry.config(validate='all', validatecommand=(int_validation_command, '%P'))
        self.date_start_entry.grid(column=0, row=current_row)

        self.date_start_age = ttk.Combobox(date_range, width=3)
        self.date_start_age['values'] = ('BC','AD')
        self.date_start_age.current(0)
        self.date_start_age.grid(column=1, row=current_row)
        ttk.Label(date_range, text="-").grid(column=2, row=current_row)

        self.date_end_entry = ttk.Entry(date_range, width=5, validate='all', validatecommand=(int_validation_command, '%P'))
        self.date_end_entry.grid(column=3, row=current_row)
        self.date_end_age = ttk.Combobox(date_range, width=3)
        self.date_end_age['values'] = ('BC','AD')
        self.date_end_age.current(0)
        self.date_end_age.grid(column=4, row=current_row)
        date_range.grid(column=2, row=current_row)

        # Artist
        current_row += 1
        ttk.Label(self, text="Artist").grid(column=0, row=current_row, sticky=W)
        self.artist_combobox = ttk.Combobox(self, width=12)
        self.artist_combobox.grid(column=2, row=current_row)

        # Art type(e.g. painting, sculpture, etc.)
        current_row += 1
        ttk.Label(self, text="Type").grid(column=0, row=current_row, sticky=W)
        self.art_type_combobox = ttk.Combobox(self, width=12)
        self.art_type_combobox.grid(column=2, row=current_row)

        # Color
        current_row += 1        
        ttk.Label(self, text="Predominant Color").grid(column=0, row=current_row, sticky=W)
        color_frame = tk.Frame(self)
        
        # self.selected_color_styling = ttk.Style()
        # self.selected_color_styling.configure("selected_color.TButton")
        # self.choose_color_button = ttk.Button(color_frame, style="selected_color.TButton", command=self.on_choose_color)
        self.choose_color_button = tk.Button(color_frame, command=self.on_choose_color, width=7, relief=tk.RAISED)

        self.choose_color_entry_var = tk.StringVar()
        self.choose_color_button.config(bg='#0080c0')
        self.choose_color_entry_var.set('#0080c0')

        self.choose_color_button.grid(column=0, row=0, sticky=W)
        self.choose_color_entry = ttk.Entry(color_frame, width=8, state=tk.DISABLED, textvariable=self.choose_color_entry_var)
        self.choose_color_entry.grid(column=1, row=0, sticky=E)
        color_frame.grid(column=2, row=current_row)

        # Rarity
        current_row += 1
        ttk.Label(self, text="Fetch rarely viewed art").grid(column=0, row=current_row, sticky=W)
        self.rarity_checkbutton_var = tk.BooleanVar()
        tk.Checkbutton(self, variable=self.rarity_checkbutton_var).grid(column=2, row=current_row, sticky=EW)

        # Style (e.g. impressionist, abstract, etc.)
        current_row += 1
        ttk.Label(self, text="Style").grid(column=0, row=current_row, sticky=W)
        self.style_combobox = ttk.Combobox(self, width=12)
        self.style_combobox.grid(column=2, row=current_row)



        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=0)
        self.columnconfigure(index=2, weight=1)


        configure_frame_row_resize(self)

        add_widget_padding(self)

       


        



class LogPaneFrame(ttk.Labelframe):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.scrolled_text = scrolledtext.ScrolledText(master=self)
        self.scrolled_text.configure(state=tk.DISABLED, background='light gray')
        self.scrolled_text.tag_config('warning', background='black', foreground='red')
        self.scrolled_text.tag_config('success', background='black', foreground='green')

        self.scrolled_text.grid(column=0, row=0, sticky=NSEW)


        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=1, minsize=10)
        configure_frame_row_resize(self)

    def log_message(self, message, tag=None):
        
        self.scrolled_text.configure(state=tk.NORMAL)
        self.scrolled_text.insert(tk.END,"\n" + message + "\n", tag)
        self.scrolled_text.configure(state=tk.DISABLED)

        



class FetchButtonFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.fetch_button = tk.Button(self, text="Fetch", bg='light green')
        self.fetch_button.grid(column=0, row=0, sticky=NSEW)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


def on_int_entry_edited(text):
    print("in int validation\ntext: " + text)
    if str.isdigit(text) or text == "":
        return True
    else:
        return False



def configure_frame_row_resize(frame):
    for row in range(frame.grid_size()[1]):
        frame.rowconfigure(row, weight=1)

def add_widget_padding(frame):
    for widget in frame.winfo_children():
        widget.grid_configure(padx=5, pady=5)
        add_widget_padding(widget)




class MainApplication(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
       
        self.parent = parent        
        self.controller = None

        self.file_management_frame = FileManagementFrame(self, text="File Management", borderwidth=5, relief=tk.RIDGE)
        self.artwork_criteria_frame = ArtworkCriteriaFrame(self, text="Artwork Criteria", borderwidth=5, relief=tk.RIDGE)
        self.log_panel_frame = LogPaneFrame(self, text="Log", borderwidth=5)
        self.fetch_button_frame = FetchButtonFrame(self, borderwidth=5, relief=tk.RIDGE)


        self.file_management_frame.grid(column=0, row=0, sticky=(NSEW), padx=10, pady=10, ipady=2)
        self.artwork_criteria_frame.grid(column=1, row=0, sticky=(NSEW), padx=10, pady=10)
        self.log_panel_frame.grid(column=0, row=1, columnspan=2, padx=10, pady=10, sticky=NSEW)
        self.fetch_button_frame.grid(column=0, row=2, columnspan=2, padx=10, pady=10, sticky=NSEW)



    def set_controller(self, controller):
        self.controller = controller

    def configure_bindings(self):
        self.fetch_button_frame.fetch_button.bind(sequence="<ButtonPress>", func=self.controller.on_fetch_button_clicked)