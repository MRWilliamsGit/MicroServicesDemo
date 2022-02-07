install:
	pip install --upgrade pip &&\
		pip3 install -r requirements.txt

#testing not set up
test:
	python -m pytest -vv test.py

format:
	black *.py

lint:
	pylint --disable=R,C heythere.py

all: install lint test
