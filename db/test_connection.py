import psycopg2
from urllib.parse import urlparse
from core.config import settings


# Get the full URL
db_url = settings.DATABASE_URL

if not db_url:
    raise EnvironmentError("DATABASE_URL not set in environment variables.")
print("DATABASE_URL:", db_url, flush=True)
# Parse URL into components
parsed = urlparse(db_url)

try:
    conn = psycopg2.connect(
        dbname=parsed.path[1:],  # removes leading slash
        user=parsed.username,
        password=parsed.password,
        host=parsed.hostname,
        port=parsed.port
    )
    print("✅ Connected to PostgreSQL successfully.",flush=True)
    conn.close()

except Exception as e:
    print("❌ Failed to connect.",flush=True)
    print(e)


