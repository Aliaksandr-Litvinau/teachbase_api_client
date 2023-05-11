postgres: ## Run postgres
	@docker run -d -p 5432:5432 \
                  -e POSTGRES_PASSWORD=postgres \
                  -e POSTGRES_USER=postgres \
                  -e POSTGRES_DB=teachbase_db \
                  --name teachbase_db \
                  --restart always \
                  postgres:13;

redis:
	@docker run --name teachbase_redis \
                -p 6379:6379 \
                -d redis;


