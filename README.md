# Sample HTTP Check

This sample shows how to turn any shell script into a Service Check
that Datadog can consume and monitor. The aim is simplicity and
time-to-value.

Fork from https://github.com/DataDog/sample-http-check
Thanks @alq666

## Python implementation

This python implementation uses CURL under the covers for maximum
flexibility.

It is packaged with `make` as an example.

To install dependencies:

    make build

To run it:

    MY_URL=... DATADOG_API_KEY=... DATADOG_APP_KEY=... venv/bin/python sample.py
