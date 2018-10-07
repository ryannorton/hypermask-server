# **Hypermask Server**

Hypermask account and encrypted seed service. Enables wallet usage across devices.

## Requirements

1. python 3.6+

## Quick Start

```
# Copy configuration file
cp sample.env .env

# Create virtual env
virtualenv .env_py3

# Activate virtual env
source .env_py3/bin/activate

# Install requirements
pip install -r requirements.txt

# Initialize database
python manage.py migrate

# Start server
python manage.py runserver
```
