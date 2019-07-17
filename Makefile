.PHONY: build run clean

build:
	python3 -m venv ./venv/
	venv/bin/pip3 install -e .

clean:
	@rm -rf venv
