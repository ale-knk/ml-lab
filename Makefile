PROJECT_NAME=ml-lab
include .env
export $(shell sed 's/=.*//' .env)

up:
	set -a; . .env; set +a;
	docker compose -f infrastructure/docker-compose.yml -p $(PROJECT_NAME) up --build -d

down:
	set -a; . .env; set +a; \
	docker compose -f infrastructure/docker-compose.yml --project-name $(PROJECT_NAME) down -v
