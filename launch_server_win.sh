Grygory Dyadichenko, [08.01.21 20:49]
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

cd "$parent_path"
py -m pip install --user virtualenv
py -m venv env
.\_env\Scripts\activate
python3 -m pip install -r requirements.txt
python app.py