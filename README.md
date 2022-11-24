# pyOPERA
Full python implementation of the NIH OPERA suite of models  
docker run -it --rm pyopera_pyopera /bin/bash  
docker compose -f docker-compose.yml build  

```
poetry run python -m pip install -r requirements.txt  
poetry run black .  
poetry run isort .  
poetry run pylint $(find . -name "*.py" | xargs)  
poetry run pytest tests  
poetry run coverage run -m pytest tests    
```

~~TODO: Create a python package around the Matlab package (the base files) using Poetry~~  
TODO: Create CI/CD for package in TestPypi and the prod Pypi (CircleCI maybe?)  
~~TODO: Auto semantic versioning with poetry too~~  
TIDO: Documentation using Sphinx (make sure original repo/builders are credited)  
TODO: Start adding the wrapper code and files  
TODO: Benchmarking with airspeed velocity  
~~TODO: Formatting/Linting/Coverage~~
~~TODO: Choose between Pytest an Unittest~~ 




