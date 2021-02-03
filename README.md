# Gamitude Voice Command Recognition

Recognizing voice commands for [Gamitude](https://gamitude.rocks/ "Gamitude production version").

## Dev

### Install dependencies

`poetry install`

### Run project

#### Windows

`./run_win.sh`

#### Linux

`./run_lin.sh`

### Export to requirements.txt format

`poetry export -f requirements.txt --output requirements.txt`

## Docker
### download other components and build docker
```
./clone.sh 
docker-compose up
```
go to localhost:3000 register, login and have fun  