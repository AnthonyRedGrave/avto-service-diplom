migrate:
	docker-compose run --rm web python manage.py migrate

migrations:
	docker-compose run --rm web python manage.py makemigrations 

admin:
	docker-compose run --rm web python manage.py createsuperuser 