SHELL := /bin/bash
tester_version = 1.0.0
project_name = least_common_string
main_script_file = least_common_string.py
venv_path = venv_py3/bin

run:
	(source setenv;\
	python ./$(project_name)/$(main_script_file))
install:
	(ls ./venv_py3 >/dev/null 2>&1|| virtualenv -p $$(which python3) venv_py3;\
	  source setenv;\
	  cat ./misc/requirement.txt | awk '{print "pip install",$$0}' | bash)
utest:
	(source setenv;\
	./$(venv_path)/pytest -vv ./$(project_name)/tests/utests/test*.py;\
	./$(venv_path)/py.test --cov-report term-missing --cov=$(project_name) ./$(project_name)/;)

