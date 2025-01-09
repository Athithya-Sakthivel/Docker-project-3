DOCKER_COMPOSE = docker-compose
GIT_REPO = https://github.com/Athithya-Sakthivel/Docker-project-3

# Install Python dependencies
requirements:
	pip install -r requirements.txt

# Build Docker images
docker-build:
	$(DOCKER_COMPOSE) build

# Run the full pipeline
run:
	$(DOCKER_COMPOSE) up --build

# Push changes to GitHub
push:
	git add .
	git commit -m "Automated pipeline updates"
	git push origin main

# Clean Docker containers, images, and networks
clean:
	$(DOCKER_COMPOSE) down
	docker system prune -f

# Run everything in order
all: requirements docker-build run push
