all: build install

.PHONY: build install test docs distclean dist upload

build:
	python3 setup.py build

install:
	python3 setup.py install

test:
	python3 -m pytest -v --cov=pytaxa test/

docs:
	cd docs;\
	make html

distclean:
	rm dist/*

dist:
	python3 setup.py sdist
	python3 setup.py bdist_wheel --universal

uptest:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload:
	twine upload dist/*
