import os
from datetime import datetime

time_pattern = "%H:%M:%S %d/%m/%Y"
default_iconsPath = "/icons/"
def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0 : 'B', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
    while size > power:
        size /= power
        n += 1
    return "%.0f" % size, power_labels[n]

def isImage(extension):
    return extension == ".png" or extension == ".jpg" or extension == ".svg"

class FileData:
    def __init__(self, filename, abs_path):
        self.href = filename
        self.creationTime = datetime.fromtimestamp(os.path.getctime(abs_path)).strftime(time_pattern)
        self.modificationTime = datetime.fromtimestamp(os.path.getmtime(abs_path)).strftime(time_pattern)
        size = format_bytes(os.path.getsize(abs_path))
        self.fileSize = size[0] + " " + size[1]
        self.caption = os.path.basename(filename)
        extension = os.path.splitext(filename)[1]
        if extension == ".apk":
            self.iconPath = os.path.join(default_iconsPath, "apk.png")
        else:
            if isImage(extension):
                self.iconPath = filename
            else:
                self.iconPath = os.path.join(default_iconsPath, "file.png")

class DirectoryData:
    def __init__(self, path):
        self.href = path
        self.caption = os.path.basename(path)