install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_heythere.py

format:
	black *.py

lint:
	pylint --disable=R,C heythere.py

all: install lint test
