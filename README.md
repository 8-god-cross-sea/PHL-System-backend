# PHL-System-backend
[![Build Status](https://travis-ci.org/8-god-cross-sea/PHL-System-backend.svg?branch=master)](https://travis-ci.org/8-god-cross-sea/PHL-System-backend)
[![Coverage Status](https://coveralls.io/repos/github/8-god-cross-sea/PHL-System-backend/badge.svg?branch=master)](https://coveralls.io/github/8-god-cross-sea/PHL-System-backend?branch=master?maxAge=0)

# Setup
Trough pipenv:
```bash
pipenv install
pipenv run gunicorn app:app
```

On Windows:
```bash
pipenv install
pipenv run waitress-serve --port=xxxx app:app
```

Trough Docker:
```bash
docker-compose up # use production config by default
```