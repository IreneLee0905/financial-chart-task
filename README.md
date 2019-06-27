# financial-chart-task

This is a back-end server for a small project, showing the best profit period in one time transaction of stocks.

## Initial setting
For the first running this server, please change the file name [settings-sample.py](mysite/mysite/settings-sample.py) to **settings.py**.
Setup the Database setting. The default database I used is PostgreSQL.

Stocks data are in the [stocks_fixtures.json](mysite/charts/fixtures/stocks_fixtures.json).
Please use ```python python manage.py loaddata stocks_fixtures.json``` to insert all the data to database.


