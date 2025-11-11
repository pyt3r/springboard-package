PACKAGE_NAME=springboard

pep8:
	python -m autopep8 ${PACKAGE_NAME}/ -a -r --in-place

lint:
	python -m flake8 ${PACKAGE_NAME}/ --count --show-source --statistics


git-merge: # if your changes are in develop...
	git checkout develop
	git pull
	git merge origin/master
	git push origin develop

git-amend:
	git commit --amend --no-edit
