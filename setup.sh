pip3 install -r requirement.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py test
python3 manage.py shell < setup.py
