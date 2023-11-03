.PHONY: repl exec unproxy

unproxy:
	unset HTTP_PROXY
	unset HTTPS_PROXY
	unset ALL_PROXY

interactive: unproxy
	BBSTOPER_NOT_LOADIMAGE=0 python3 -i main.py

exec: unproxy
	BBSTOPER_NOT_LOADIMAGE=1 python3 main.py
