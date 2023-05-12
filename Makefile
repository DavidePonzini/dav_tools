NAME=utils-DAVIDE-PONZINI

build:
	rm -rf dist/
	python3 -m pip install build
	python3 -m build

upload-test: build
	python3 -m pip install --upgrade twine
	python3 -m twine upload --repository testpypi dist/*

install-local: uninstall build
	python3 -m pip install ./dist/*.whl

download-test: uninstall
	python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps $(NAME)

uninstall:
	python3 -m pip uninstall $(NAME)
	