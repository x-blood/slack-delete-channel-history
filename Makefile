deploy:
	sls deploy --aws-profile $(PROFILE)

pip_install:
	pip install -r requirements.txt

pip_freeze:
	pip freeze > requirements.txt

venv_activate:
	source ./myvenv/bin/activate