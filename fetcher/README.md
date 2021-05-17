# Query Xiaomi Flora devices & store data to designated services

## Installation

```
sudo apt-get install -y bluez build-essential cargo libffi-dev libglib2.0-dev libssl-dev python3-dev

# see https://cryptography.io/en/latest/installation/ and https://github.com/IanHarvey/bluepy for other distro

$ pip install -r requirements.txt

$ pip install setup.py
```

## Development

This project includes a number of helpers in the `Makefile` to streamline common development tasks.

### Environment Setup

The following demonstrates setting up and working with a development environment:

```
### create a virtualenv for development

$ make virtualenv

$ source env/bin/activate


### run myflora-fetcher cli application

$ myflora-fetcher --help


### run pytest / coverage

$ make test
```


### Releasing to PyPi

Before releasing to PyPi, you must configure your login credentials:

**~/.pypirc**:

```
[pypi]
username = YOUR_USERNAME
password = YOUR_PASSWORD
```

Then use the included helper function via the `Makefile`:

```
$ make dist

$ make dist-upload
```

## Deployments

### Docker

Included is a basic `Dockerfile` for building and distributing `My Flora Fetch Tool`,
and can be built with the included `make` helper:

```
$ make docker

$ docker run -it myflora-fetcher --help
```
