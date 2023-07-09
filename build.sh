pip3 install -U pip
pip3 install -U setuptools
pip install -r requirements.txt
python3.9 makemigrations monkeys contacts api
python3.9 manage.py migrate 
python3.9 manage.py collectstatic