.PHONY: interactive auto auto_headless unproxy

unproxy:
	unset HTTP_PROXY
	unset HTTPS_PROXY
	unset ALL_PROXY

interactive:
	BBSTOPER_HEADLESS=0 python3 -i main.py

auto:
	BBSTOPER_HEADLESS=2 python3 main.py

auto_headless:
	BBSTOPER_HEADLESS=1 python3 main.py
