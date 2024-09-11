# Webhook Repository

This repository contains a Flask application for handling GitHub webhook events. It receives webhook notifications from GitHub, processes the events, and stores relevant data in MongoDB. This application uses ngrok to expose the local server to the internet.

## Project Structure

- `app/`: Contains the Flask application code.
  - `__init__.py`: Initializes the Flask app.
  - `extensions.py`: Configures extensions like MongoDB.
  - `webhook/`: Contains the webhook blueprint and routes.
    - `__init__.py`: Initializes the webhook blueprint.
    - `routes.py`: Defines routes for handling webhook events.
- `Pipfile` and `Pipfile.lock`: Define the project's Python dependencies.
- `requirements.txt`: Alternative dependency management file.
- `run.py`: Entry point to start the Flask application.

### Prerequisites

- Python 3.7 or later
- [Pipenv](https://pipenv.pypa.io/en/latest/) (or `pip` for managing dependencies)
- [Ngrok](https://ngrok.com/) for exposing the local server
