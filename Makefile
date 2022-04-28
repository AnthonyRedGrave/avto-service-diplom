migrate:
	docker-compose run --rm web python manage.py migrate

migrations:
	docker-compose run --rm web python manage.py makemigrations 

admin:
	docker-compose run --rm web python manage.py createsuperuser 

csv_import:
	docker-compose run --rm web python manage.py csv_import

csv_export:
	docker-compose run --rm web python manage.py csv_export