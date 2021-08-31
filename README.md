- [Hottest city.](#hottest-city)
  - [How to deploy](#how-to-deploy)
  - [Example](#example)
  - [Reasoning](#reasoning)

# Hottest city.

Application to find a big city with the highest temperature.

## How to deploy

1. Create `.env` file at the repo dir with following context
  ```
  POSTGRES_USER=test
  POSTGRES_PASSWORD=password
  POSTGRES_HOST=localhost
  POSTGRES_PORT=5432
  POSTGRES_DB=example
  OPENWEATHER_TOKEN=67b5b992f75ad1be9b2becb87ca0f49f
  ```

2. Run the database
  ```
  docker-compose up --build -d
  ```

3. Fill the database
  ```
  pipenv shell
  PYTHONPATH=$(pwd):$PYTHONPATH python hottest/scripts/fill_cities.py
  exit
  ```

4. Run the app
  ```
  pipenv shell
  FLASK_APP=hottest/app.py flask run
  ```

5. Go to http://127.0.0.1:5000/open_weather

## Example

Ahvaz Iran 46.97

## Reasoning

It is just an example of `asyncio` usage.