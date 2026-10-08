.PHONY: research-check research-render research-find research-test research-imports
export QUERY

research-check:
	python3 -B tools/research/research.py check

research-render:
	python3 -B tools/research/research.py render

research-find:
	python3 -B tools/research/research.py find

research-test:
	python3 -B -m unittest discover -s tools/research/tests -p 'test_*.py'

research-imports:
	python3 -B tools/research/research.py imports
