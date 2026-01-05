from core.file_handler import FileHandler

class VersionControl:

    @staticmethod
    def save_version():
        data = FileHandler.load_map()
        return FileHandler.backup_map(data)
