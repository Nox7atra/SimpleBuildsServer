parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

cd "$parent_path"
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate
py -m pip install -r requirements.txt
py app.py