# Server Downtime Monitor

A server downtime montoring webapp that sends notifications to owners when there is downtime

## Useful links



## Requirements

- Python / Django / Django Rest Framework

## Project setup

If not using docker, you can setup a virtual environment using the command below

```sh
python -m venv env
```

then activate it with

```sh
./env/Scripts/activate   # windows or
source env/bin/activate  # linux or mac
```

Once the virtual environment has been activated, install the necessary requirements by using the command below

```sh
python manage.py migrate
```

## Contribution

If you haven't cloned the repository, use the command to clone from the terminal

```sh
git clone https://github.com/dauntless001/sdtmonitor.git
```

When creating a new branch, **ENSURE** that the branch name starts with the format **SDT-&lt;issue-no&gt;-&lt;short-description&gt;** e.g. **SDT-1-project-setup** and the main branch is from develop.

When creating a pull request, please select the target branch as `develop`.

- After writing your code, make sure to run the tests and **ENSURE** it passes before pushing to the git repository. Use the command below to run the test.

```sh
python manage.py test
```

## Pushing to the repository

Run the following command

```sh
 # if pushing for the first time
$ git push -u origin <branchname>

# if pushing normally
$ git push
```
