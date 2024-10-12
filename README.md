# FastAPI Project with Repository Pattern

This project is a FastAPI application implementing the repository pattern for clean and maintainable code architecture.

## Project Structure

The project follows a modular structure:

```
project_root/
├── app/
│   ├── api/
│   ├── db/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   └── main.py
├── alembic/
├── .env
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Copy `.env.example` to `.env` and fill in the necessary details.

### Running the Application

To run the application:

```
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Documentation

Once the application is running, you can access the automatic interactive API documentation:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`


## Database Migrations

This project uses Alembic for database migrations. To create a new migration:

```
alembic revision --autogenerate -m "Description of the change"
```

To apply migrations:

```
alembic upgrade head
```
