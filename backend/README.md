# Flash Decks Backend

FastAPI backend for the Flash Decks flashcard application.

## Prerequisites

- Python 3.9+
- PostgreSQL 15+
- pip or conda for package management

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Copy the example environment file and update it with your settings:

```bash
cp .env.example .env
```

Edit `.env` and configure:
- `DATABASE_URL`: PostgreSQL connection string
- `JWT_SECRET_KEY`: Secret key for JWT tokens (change in production!)
- `JWT_REFRESH_SECRET_KEY`: Secret key for refresh tokens (change in production!)

### 3. Set Up PostgreSQL

#### Option A: Using Docker (Recommended for Development)

```bash
docker run -d \
  --name flashdecks-postgres \
  -e POSTGRES_USER=flashdecks \
  -e POSTGRES_PASSWORD=flashdecks \
  -e POSTGRES_DB=flashdecks \
  -p 5432:5432 \
  postgres:15-alpine
```

#### Option B: Local PostgreSQL Installation

Install PostgreSQL and create the database:

```bash
# macOS with Homebrew
brew install postgresql@15
brew services start postgresql@15

# Create database and user
createdb flashdecks
psql flashdecks -c "CREATE USER flashdecks WITH PASSWORD 'flashdecks';"
psql flashdecks -c "GRANT ALL PRIVILEGES ON DATABASE flashdecks TO flashdecks;"
```

### 4. Run Database Migrations

```bash
alembic upgrade head
```

### 5. Start the Development Server

```bash
uvicorn app.main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

## API Documentation

Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Testing

```bash
pytest
```

## Project Structure

```
backend/
├── app/
│   ├── api/          # API routes
│   ├── core/         # Core configuration
│   ├── db/           # Database session and initialization
│   ├── models/       # SQLModel models
│   ├── schemas/      # Pydantic schemas
│   └── main.py       # FastAPI application entry point
├── alembic/          # Database migrations
├── tests/            # Test files
└── requirements.txt  # Python dependencies
```
