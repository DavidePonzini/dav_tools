DEV_NAME=utils-DAVIDE-PONZINI
REL_NAME=dav-utils

build:
	python3 -m pip install build
	python3 -m build

upload-test:
	python3 -m pip install --upgrade twine
	python3 -m twine upload --repository testpypi dist/*

install-test:
	python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps $(DEV_NAME)

uninstall:
	python3 -m pip uninstall $(DEV_NAME) $(REL_NAME)
	