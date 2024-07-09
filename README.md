## Doodlify
### installation progress
```bash
git clone https://github.com/mihf05/Doodlify.git
cd Doodlify
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
py manage.py runserver
```
### create admin
```bash
py manage.py createsuperuser
```
### migrate
```bash
py manage.py migrate
```  
