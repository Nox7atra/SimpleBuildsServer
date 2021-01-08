parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

cd "$parent_path"
virtualenv --no-site-packages env
source env/bin/activate
pip install -r requirements.txt
python app.py