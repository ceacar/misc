SHELL := /bin/bash
tester_version = 1.0.0

run:
	(source setenv;\
	python ./run.py)
install:
	(ls ./venv_py3 >/dev/null 2>&1|| virtualenv -p $$(which python3) venv_py3;\
	  source setenv;\
	  cat ./misc/requirement.txt | awk '{print "pip install",$$0}' | bash)
utest:
	(source setenv;\
	pytest -vv ./loan_processor/tests/utests/;\
	py.test --cov-report term-missing --cov=loan_processor ./loan_processor/;)
itest:
	(source setenv;\
	python ./loan_processor/tests/itests/itest.py && echo "itest passed")

run_large:
	(source setenv;\
	./misc/random_data.py |python ./misc/run_stdin.py)
