parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

cd "$parent_path"
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt
python3 app.py