# Flask-REST + WebUI
A Flask RESTful template for performing CRUD operations on an SQLAlchemy vehicle database.

### Configuration
* Create and load mariadb/mysql database from /dbinit
* Edit app_settings to point to api.py URL
* Edit api_settings to point to mariadb/mysql database
* Execute app.py and api.py separately 

WebUI --> http://localhost:8080 --> REST <--> http://localhost:8088

### Docker Notes:
```console
docker compose build

# Run APP with environment variables
docker run --env-file app.env -p 8080:8080 fullaware/car-demo:latest

# Run API with environment variables
docker run --env-file api.env -p 8088:8088 fullaware/car-demo-api:latest



# Stop remove all docker containers
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

SQLAlchemy used to execute following queries

Car Count
```sql
SELECT COUNT(*) AS `car_count` ​FROM `car_demo`;
```

Average Horsepower
```sql
SELECT AVG(`car_hp`) AS `AverageHP`​ FROM `car_demo`;
```

Top Colors
```sql
SELECT car_color, COUNT(`car_color`) AS `car_count` ​
FROM `car_demo` ​
GROUP BY `car_color` ​
ORDER BY `car_count` DESC;​
```
