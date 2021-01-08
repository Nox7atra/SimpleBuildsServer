Grygory Dyadichenko, [08.01.21 20:49]
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

cd "$parent_path"
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt
python app.py