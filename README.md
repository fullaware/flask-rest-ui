# Flask-REST + WebUI
A Flask RESTful template for performing CRUD operations on an SQLAlchemy vehicle database.
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