# Docker local development commands
build:
	docker compose -f docker-compose.yml build  

run_image_windows:
	docker run -it -v %cd%:/app -p 8080:8080 --rm pyopera_pyopera /bin/bash


# Run various commands inside running docker image
pip_install_packages:
	poetry run python -m pip install -r requirements.txt  

format_all:
	poetry run black . --exclude={docs/,libOPERA_Py/,".asv/"}    
	poetry run isort .   
	poetry run pylint $(find pyopera -name "*.py" | xargs)    

black:
	poetry run black . --exclude={docs/,libOPERA_Py/,".asv/"}   

isort:
	poetry run isort .  

lint: # Run directly doesnt work with makefile
	poetry run pylint $(find pyopera -name "*.py" | xargs)  

test:
	poetry run coverage run --source pyopera -m pytest  
	poetry run coverage report --skip-empty --fail-under=85

run_benchmarks:
	poetry run asv run --python=same

get_benchmark_results:
	poetry run asv publish
	poetry run asv preview

check_if_builds:
	poetry run black . --check --exclude={docs/,libOPERA_Py/}
	poetry run isort --check --diff .  
	poetry run pylint $(find pyopera -name "*.py" | xargs)
	poetry run coverage run --source pyopera -m pytest
	poetry run coverage report --skip-empty --fail-under=85
