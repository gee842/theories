.PHONY: research-check research-render research-find research-test research-imports research-links research-secrets
export QUERY

research-check:
	python3 -B tools/research/research.py secrets
	python3 -B tools/research/research.py check

research-render:
	python3 -B tools/research/research.py render

research-find:
	python3 -B tools/research/research.py find

research-test:
	python3 -B -m unittest discover -s tools/research/tests -p 'test_*.py'

research-imports:
	python3 -B tools/research/research.py imports

research-links:
	python3 -B tools/research/research.py links

research-secrets:
	python3 -B tools/research/research.py secrets
