all: unittest test
	@echo "All done..."

unittest:
	pytest -v test_hvert.py

test:
	@cat 1.in | python hvert.py | diff - 1.ans
	@cat 2.in | python hvert.py | diff - 2.ans
	@echo "All local test passed..."

style-check:
	flake8 .

type-check:
	mypy --strict .

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .hypothesis

kattis-submit:
	@python ../kattis-cli/submit.py -f -p hvertskalmaeta hvert.py