# **Hypermask Server**

Hypermask account and encrypted seed service. Enables wallet usage across devices.

## Requirements

- python 3.6+

## Quick Start

```bash
# Copy configuration file
$ cp sample.env .env

# Create virtual env
$ virtualenv .env_py3

# Activate virtual env
$ source .env_py3/bin/activate

# Install requirements
$ pip install -r requirements.txt

# Initialize database
$ python manage.py migrate

# Start server
$ python manage.py runserver
```

## REST API Endpoints

### Register New User

[POST] [localhost:8000/api/v1/register](http://localhost:8000/api/v1/register)

Example Request Body:

```json
{
    "username": "satoshi",
    "password_hash": "pwhash",
    "encrypted_key": "x9Dk3LkjD... (optional)"
}
```

Example Response:

```json
{
    "created": true
}
```

### Set Encrypted Key

[POST] [localhost:8000/api/v1/key?username=satoshi&password_hash=pwhash&encrypted_key=x9Dk3LkjD...](http://localhost:8000/api/v1/key?username=satoshi&password_hash=pwhash&encrypted_key=x9Dk3LkjD...)

Example Response:

```json
{
    "success": true
}
```

### Get Encrypted Key

[GET] [localhost:8000/api/v1/key?username=satoshi&password_hash=pwhash](http://localhost:8000/api/v1/key?username=satoshi&password_hash=pwhash)

Example Response:

```json
{
    "encrypted_key": "x9Dk3LkjD..."
}

```
