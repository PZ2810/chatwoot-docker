#!/usr/bin/env bash
set -e

ENV_FILE=".env"
EXAMPLE_FILE=".env.example"

if [ ! -f "$EXAMPLE_FILE" ]; then
  echo "Error: $EXAMPLE_FILE not found!"
  exit 1
fi

echo "Generating $ENV_FILE from $EXAMPLE_FILE..."
cp -f "$EXAMPLE_FILE" "$ENV_FILE"

SECRET_KEY=$(openssl rand -hex 64)
POSTGRES_PW=$(openssl rand -hex 32)
REDIS_PW=$(openssl rand -hex 32)

sed -i "s/replace_with_a_64_char_hex_string/$SECRET_KEY/" "$ENV_FILE"
sed -i "s/replace_with_a_secure_postgres_password/$POSTGRES_PW/" "$ENV_FILE"
sed -i "s/replace_with_a_secure_redis_password/$REDIS_PW/" "$ENV_FILE"

echo ""
echo "Successfully generated .env with secure random keys:"
grep -E "SECRET_KEY_BASE|POSTGRES_PASSWORD|REDIS_PASSWORD" "$ENV_FILE"
echo ""
echo "Next: Run 'nano .env' to update your FRONTEND_URL."
