.PHONY: build run clean

build:
	virtualenv venv
	venv/bin/pip install -e .

clean:
	@rm -rf venv
