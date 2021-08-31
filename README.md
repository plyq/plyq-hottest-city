- [Hottest city](#hottest-city)
  - [How to deploy](#how-to-deploy)
  - [Example](#example)
- [Reasoning](#reasoning)

# Hottest city

Application to find a big city with the highest temperature.

## How to deploy

1. Create `.env` file at the repo dir with following context
  ```
  POSTGRES_USER=test
  POSTGRES_PASSWORD=password
  POSTGRES_HOST=localhost
  POSTGRES_PORT=5432
  POSTGRES_DB=example
  OPENWEATHER_TOKEN=<your open https://openweathermap.org token>
  ```

2. Run the database
  ```
  docker-compose up --build -d
  ```

3. Go to environment
   ```
   pipenv shell
   ```

4. Fill the database
  ```
  PYTHONPATH=$(pwd):$PYTHONPATH python hottest/scripts/fill_cities.py
  ```

5. Run the app
  ```
  FLASK_APP=hottest/app.py flask run
  ```

5. Go to http://127.0.0.1:5000/open_weather

## Example

Ahvaz Iran 46.97

# Reasoning

It is just an example of `asyncio` usage.