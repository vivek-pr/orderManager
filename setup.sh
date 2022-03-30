pip3 install -r req.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py test
python3 manage.py shell < setup.py