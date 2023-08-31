.PHONY: repl exec

repl:
	python3 -i main.py

exec:
	BBSTOPER_NOT_USE_X=1 python3 main.py
