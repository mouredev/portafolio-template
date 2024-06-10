python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf backend
reflex init
reflex export --backend-only
unzip backend.zip -d backend
rm -f backend.zip
deactivate