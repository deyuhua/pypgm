PY_TEST=python3 -m unittest -v

all: install test

### install pgm module into system
install:
	python3 setup.py install

### unit test case
test:
	cd ./tests && \
	$(PY_TEST) potential_test.py &&\
	$(PY_TEST) graph_test.py

clean:
	rm -rf build/ dist/ pypgm.egg-info/
