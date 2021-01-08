from flask import Flask, send_file
import os
from data_structures import FileData, DirectoryData
import json
from jinja2 import FileSystemLoader, Environment

app = Flask(__name__)
default_iconsPath = "/icons/"
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('FileIndexTemplate.html')

def getfiles(dirpath):
    files = [s for s in os.listdir(dirpath)
         if os.path.isfile(os.path.join(dirpath, s))]
    files.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
    return reversed(files)
def getdirs(dirpath):
    dirs = [s for s in os.listdir(dirpath)
         if os.path.isdir(os.path.join(dirpath, s))]
    dirs.sort()
    return dirs

with open('config.json', 'r') as file:
    config = json.loads(file.read())
    filesPath = config["folderToIndex"]

@app.route('/', defaults={'req_path': ''})
@app.route('/<path:req_path>')
def dir_listing(req_path):
    # Joining the base and the requested path
    abs_path = os.path.join(os.path.abspath(config["folderToIndex"]), req_path)
    print(abs_path)
    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_file(abs_path, as_attachment=True)

    # Show directory contents
    files = getfiles(abs_path)
    dirs = getdirs(abs_path)

    dirsData = []
    filesData = []
    for file in files:
        filesData.append(FileData(file, os.path.join(abs_path, file)))
    for dir in dirs:
        if not default_iconsPath.__contains__(dir):
            dirsData.append(DirectoryData(dir))
    return template.render(dirlist=dirsData, filelist=filesData)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
