up:
	docker compose up -d --build

down:
	docker compose down

logs:
	docker compose logs -f web

migrate:
	docker compose exec web python src/manage.py migrate

createsuperuser:
	docker compose exec web python src/manage.py createsuperuser

shell:
	docker compose exec web python src/manage.py shell

collectstatic:
	docker compose exec web python src/manage.py collectstatic --noinput
