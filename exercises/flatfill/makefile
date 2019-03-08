SHELL := /bin/bash
tester_version = 1.0.0
project_name = blazing_potato
service_port = 35555
server_ip = localhost

run:
	(source setenv;\
	cd ./src/main/java/;\
	javac ./Main.java;\
	java Main;)
install:
	(ls ./venv_py3 >/dev/null 2>&1|| virtualenv -p $$(which python3) venv_py3;\
	  source setenv;\
	  cat ./misc/requirement.txt | awk '{print "pip install",$$0}' | bash)
utest:
	(source setenv;\
	javac ./src/test/java/FailingTest.java;\
	java org.junit.runner.JUnitCore FailingTest)
	#javac -cp /usr/share/java/junit-4.10.jar ./test/java/FailingTest.java)
itest:
	(source setenv;\
	pytest -vv ./$(project_name)/tests/itests/itest.py)

locust:
	(source setenv;\
	cd $(project_name)/tests/loadtests;\
	locust --host=$(service_ip):$(service_port))

benchmark:
	(source setenv;\
	./example_cmd_for_sanity_test.py;\
	ab -c 500 -n 5000 -s 90 localhost:35555/get/b7d1c31f1654ddf1043260b571e9d8ba)
