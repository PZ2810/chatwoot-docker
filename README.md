# Chatwoot Self-Hosted (Docker Compose)

Self-hosted [Chatwoot](https://www.chatwoot.com) deployment using Docker Compose.

## Architecture

| Service    | Image                        | Port (host)    | Purpose                           |
|------------|------------------------------|----------------|-----------------------------------|
| **rails**  | `chatwoot/chatwoot:latest`   | `127.0.0.1:3100` | Main web app & API              |
| **sidekiq**| `chatwoot/chatwoot:latest`   | —              | Background job processor          |
| **postgres** | `pgvector/pgvector:pg16`   | `127.0.0.1:5432` | Primary database               |
| **redis**  | `redis:alpine`               | `127.0.0.1:6379` | Cache & job queue              |

Data is persisted in Docker volumes: `postgres_data`, `redis_data`, `storage_data`.

---

## Prerequisites

- **OS:** Ubuntu 20.04+ (or any Linux with Docker support)
- **Docker:** v20.10+
- **Docker Compose:** v2+

### Install Docker (if not installed)

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
# Log out and log back in for group changes to take effect
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/PZ2810/chatwoot-docker.git
cd chatwoot-docker
```

### 2. Create the `.env` File

Copy the example env file and fill in your values:

```bash
cp .env.example .env
nano .env   # or use any editor
```

**Required changes in `.env`:**

| Variable            | What to set                                       |
|---------------------|---------------------------------------------------|
| `SECRET_KEY_BASE`   | Generate with: `openssl rand -hex 64`             |
| `FRONTEND_URL`      | Your domain, e.g. `https://chat.yourdomain.com`   |
| `POSTGRES_PASSWORD` | Generate with: `openssl rand -hex 32`             |
| `REDIS_PASSWORD`    | Generate with: `openssl rand -hex 32`             |

### 3. Prepare the Database (First Time Only)

```bash
docker compose run --rm rails bundle exec rails db:chatwoot_prepare
```

This creates the database tables and seeds initial data.

### 4. Start All Services

```bash
docker compose up -d
```

Chatwoot will be running at `http://localhost:3100`.

### 5. Set Up Reverse Proxy (Nginx)

Since the app listens on `127.0.0.1:3100`, you need a reverse proxy to serve it on your domain with SSL.

**Install Nginx & Certbot:**

```bash
sudo apt update && sudo apt install -y nginx certbot python3-certbot-nginx
```

**Create Nginx config** at `/etc/nginx/sites-available/chatwoot`:

```nginx
server {
    server_name chat.yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:3100;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

**Enable the site and get SSL:**

```bash
sudo ln -s /etc/nginx/sites-available/chatwoot /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
sudo certbot --nginx -d chat.yourdomain.com --non-interactive --agree-tos -m you@email.com --redirect
```

---

## Common Operations

### View logs

```bash
docker compose logs -f rails
docker compose logs -f sidekiq
```

### Stop all services

```bash
docker compose down
```

### Update Chatwoot to latest version

```bash
docker compose pull
docker compose run --rm rails bundle exec rails db:chatwoot_prepare
docker compose up -d
```

### Access Rails console

```bash
docker compose exec rails bundle exec rails console
```

### Create an admin account

```bash
docker compose exec rails bundle exec rails console
# Inside console:
# SuperAdmin.create!(email: 'admin@yourdomain.com', password: 'securepassword')
```

---

## Backup & Restore

### Backup Postgres

```bash
docker compose exec postgres pg_dump -U postgres chatwoot_production > backup_$(date +%F).sql
```

### Restore Postgres

```bash
cat backup_2026-01-01.sql | docker compose exec -T postgres psql -U postgres chatwoot_production
```

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Rails/Sidekiq crash on first start | Run `docker compose run --rm rails bundle exec rails db:chatwoot_prepare` |
| `PG::ConnectionBad` | Make sure `POSTGRES_HOST=postgres` and `POSTGRES_PASSWORD` matches in both `.env` and `docker-compose.yaml` |
| Redis auth error | Ensure `REDIS_PASSWORD` in `.env` matches across services |
| Port conflict on 3100 | Change the host port in `docker-compose.yaml` under `rails > ports` |

---

## File Structure

```
.
├── docker-compose.yaml   # Service definitions
├── .env                  # Your secrets & config (NOT in git)
├── .env.example          # Template for .env
├── .gitignore            # Excludes .env from git
└── README.md             # This file
```

---

## References

- [Chatwoot Docs](https://www.chatwoot.com/docs/self-hosted)
- [Chatwoot Environment Variables](https://www.chatwoot.com/docs/self-hosted/configuration/environment-variables)
- [Chatwoot GitHub](https://github.com/chatwoot/chatwoot)
