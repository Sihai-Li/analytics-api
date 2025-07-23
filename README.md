

API microservice while aloow harness time-series data to analyze traffic of any web application. 


## Docker

- `docker build -t analytics-api -f Dockerfile.web .`
- `docker run -it analytics-api'

becomes

- `docker compose up --watch`
- `docker compose down` or 'docker compose down -v' (to remove volumnes)
- `docker compose run app/bin/bash` or `docker compose run app python`