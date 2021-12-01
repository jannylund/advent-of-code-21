.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: format
format:
	autoflake --recursive --in-place --remove-unused-variables --remove-all-unused-imports . && \
	black . && \
	isort .

.PHONY: test
test:
	python -m pytest tests
