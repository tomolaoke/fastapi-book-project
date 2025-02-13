# FastAPI Book Management Task

This project is a FastAPI application for managing a collection of books. The application provides endpoints to retrieve, create, update, and delete book entries. The application is served using Nginx as a reverse proxy and includes Continuous Integration (CI) and Continuous Deployment (CD) pipelines.

## Table of Contents
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [CI/CD Pipeline](#cicd-pipeline)
- [Nginx Configuration](#nginx-configuration)
- [Contributing](#contributing)

## Installation

### Prerequisites
- Python 3.12
- Docker (if using Docker)
- Nginx (if deploying manually)

### Clone the Repository
```bash
git clone https://github.com/tomolaoke/fastapi-book-project.git
cd fastapi-book-project
```

### Set Up Virtual Enviroment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Running the Application
### Running Locally
```bash
uvicorn main:app --reload
```

Visit http://127.0.0.1:8000 to access the application.

### Running with Docker
## Build and run Docker containers:
```bash
docker-compose up --build
```

Access the application at [http://localhost.](http://127.0.0.1:8000/api/v1/books/17)

### API Endpoints
GET /api/v1/books/: Retrieve all books.

GET /api/v1/books/{book_id}: Retrieve a book by its ID.

POST /api/v1/books/: Create a new book.

PUT /api/v1/books/{book_id}: Update a book by its ID.

DELETE /api/v1/books/{book_id}: Delete a book by its ID.

### CI/CD Pipeline

## CI Pipeline

Trigger: Pull requests to the main branch.

Actions:

Install dependencies.

Run tests.

## CD Pipeline

Trigger: Merging a pull request to the main branch.

Actions:

Deploy the application with the latest changes.

### GitHub Actions Configuration
## CI Workflow File (.github/workflows/ci.yml):
```yaml
name: CI Pipeline

on:
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Check out code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        python -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt

    - name: Run tests
      run: |
        source venv/bin/activate
        pytest
```

## Deployment Workflow File (.github/workflows/deploy.yml):
```yaml
name: Deployment Pipeline

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Check out code
      uses: actions/checkout@v2

    - name: Deploy application
      run: |
        echo "Deploying application..."
        # Add your deployment commands here
```

### Nginx Configuration
## Install Nginx
```bash
sudo apt update
sudo apt install nginx
```

### Configure Nginx as a Reverse Proxy
## Create a configuration file:
```bash
sudo nano /etc/nginx/sites-available/fastapi
```

## Add the following configuration:
```Nginx
server {
    listen 80;

    server_name your_domain_or_IP;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## Enable the configuration:
```bash
sudo ln -s /etc/nginx/sites-available/fastapi /etc/nginx/sites-enabled/
sudo systemctl restart nginx
```

### Contributing
Fork the repository.

Create a new branch.

Make your changes.

Open a pull request.

### License

MIT License

### Task Worked On by:

Tomola Oke (TM)

[Linkedin.](https://www.linkedin.com/in/tomolaoke)
