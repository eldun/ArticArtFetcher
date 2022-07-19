class Model():
    def __init__(self):
        self.file_management_model = FileManagementModel()
        self.artwork_criteria_model = ArtworkCriteriaModel()


class FileManagementModel():
    def __init__(self):
        self.output_directory = None
        self.max_picture_count = None
        self.max_folder_size = None
        self.max_folder_size_units = None
        self.auto_delete = None
        self.download_frequency = None
        self.download_frequency_units = None
        self.create_description = None


class ArtworkCriteriaModel():
    def __init__(self):
        self.date_start = None
        self.date_start_age = None
        self.date_end = None
        self.date_end_age = None
        self.artist = None
        self.type = None
        self.predominant_color = None
        self.fetch_rare_art = None
        self.style = None