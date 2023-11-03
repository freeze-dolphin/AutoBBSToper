.PHONY: repl exec unproxy

unproxy:
	unset HTTP_PROXY
	unset HTTPS_PROXY
	unset ALL_PROXY

interactive: unproxy
	python3 -i main.py

exec: unproxy
	BBSTOPER_NOT_USE_X=1 python3 main.py
