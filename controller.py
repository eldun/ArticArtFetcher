import pprint


class Controller():
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def on_fetch_button_clicked(self, event):
        self.log_message("fetch clicked")

        self.update_file_management_model()
        self.update_file_artwork_criteria_model()
        

    def update_file_management_model(self):
        model = self.model.file_management_model
        view = self.view.file_management_frame


        try:

            model.output_directory = view.output_directory
            model.max_picture_count = view.max_picture_count_entry.get()
            model.max_folder_size = view.max_folder_size_entry.get()
            model.max_folder_size_units = view.folder_size_units_combobox.get()
            model.auto_delete = view.auto_delete_checkbutton_var.get()
            model.download_frequency = view.update_frequency_entry.get()
            model.download_frequency_units = view.art_check_frequency_combobox.get()
            model.create_description = view.create_description_checkbutton_var.get()
        
        except Exception as e:
            self.log_message("Error updating File Management Model:\n" + str(e), 'warning')

        else:
            self.log_model_fields(model)            

    def update_file_artwork_criteria_model(self):

        model = self.model.artwork_criteria_model
        view = self.view.artwork_criteria_frame

        try:

            model.date_start = view.date_start_entry.get()
            model.date_start_age = view.date_start_age.get()
            model.date_end = view.date_end_entry.get()
            model.date_end_age = view.date_end_age.get()
            model.artist = view.artist_combobox.get()
            model.type = view.art_type_combobox.get()
            model.predominant_color = view.choose_color_entry.get()
            model.fetch_rare_art = view.rarity_checkbutton_var.get()
            model.style = view.style_combobox.get()

        except Exception as e:
            self.log_message("Error updating File Management Model:\n" + str(e), 'warning')

        else:
            self.log_model_fields(model)       

    def log_message(self, message, tag=''):
        self.view.log_panel_frame.log_message(message, tag)

    def log_model_fields(self, model):
        self.log_message(
            "Updated " + str(model.__class__.__name__) + "\n" +
            pprint.pformat(vars(model), indent=2) 
            + "\n")