black = poetry run black . --exclude={docs/,libOPERA_Py/,".asv/"}  
isort = poetry run isort .   
lint = poetry run pylint $$(find pyopera -name "*.py" | xargs)  
run_tests = poetry run coverage run --source pyopera -m pytest 
test_report = poetry run coverage report --skip-empty --fail-under=85 

# Docker local development commands
build:
	docker compose -f docker-compose.yml build  

run_image_windows:
	docker run -it -v %cd%:/app -p 8080:8080 --rm pyopera_pyopera /bin/bash


# Run various commands inside running docker image
pip_install_packages:
	poetry run python -m pip install -r requirements.txt  

format_all:
	$(black) 
	$(isort)  
	$(lint)  

black:
	$(black)   

isort:
	$(isort)

lint:
	$(lint) 

test:
	$(run_tests)
	$(test_report)

run_benchmarks:
	poetry run asv run --verbose --show-stderr

check_if_builds:
	$(black) --check
	$(isort) --check --diff 
	$(lint)
	$(run_tests)
	$(test_report)

get_benchmark_results: # These are just stored here they don't run in sequence
	poetry run asv show 252454ff
	poetry run asv compare -m 5f48c53c2ea4  252454ff 03ba5808
	poetry run asv publish
	poetry run asv preview
