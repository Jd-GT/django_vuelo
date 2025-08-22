# Rionegro Flights Management

This Django web application is designed to manage flight information for the city of Rionegro. It allows users to register flights, list existing flights, and view flight statistics.

## Project Structure

```
rionegro_flights
├── manage.py
├── requirements.txt
├── README.md
└── flights
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── migrations
    │   └── __init__.py
    └── templates
        └── flights
            ├── base.html
            ├── flight_list.html
            ├── flight_form.html
            └── flight_stats.html
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd rionegro_flights
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run migrations:**
   ```
   python manage.py migrate
   ```

4. **Start the development server:**
   ```
   python manage.py runserver
   ```

5. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Features

- Register new flights
- List all registered flights
- View flight statistics

## License

This project is licensed under the MIT License.