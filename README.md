# Car Rental App — PythonAnywhere Deployment Experiment

**Flask · MySQL · PythonAnywhere · REST API**

Deployment-oriented copy of my [Car Rental Web Application](https://github.com/benjanning/data-representation-project), created while exploring hosting a Python/Flask project with a MySQL database.

## What is here?

- [CarServer.py](./CarServer.py) — Flask endpoints.
- [CarDao.py](./CarDao.py) and [CustomerDao.py](./CustomerDao.py) — database access.
- [static/CarServer.html](./static/CarServer.html) — client-side interface.
- [dbconfig.py](./dbconfig.py) — environment-based database configuration.
- [requirements.txt](./requirements.txt) — Python dependencies.

## Configuration

This repository **does not include live database credentials**. Supply these environment variables in the hosting environment:

| Environment variable | Purpose |
| --- | --- |
| `DB_HOST` | Database hostname |
| `DB_USER` | MySQL user |
| `DB_PASSWORD` | MySQL password |
| `DB_NAME` | Database name |
| `DEMO_USERNAME` | Demonstration login name |
| `DEMO_PASSWORD` | Demonstration login password |

The database and Flask app require additional setup on PythonAnywhere or another suitable host. An old class demonstration URL is not guaranteed to remain online.

**Project maturity:** This is an educational deployment experiment, **not a production-ready authentication or booking service**. Demo passwords and endpoints need hardening before public deployment.

[See the main case study](https://github.com/benjanning/data-representation-project) · [Explore my portfolio](https://github.com/benjanning/programming2022)
