# Event Management and Ticketing Project

This is an Event Management and Ticketing project built using Django Rest Framework for the backend and React/Next.js for the frontend. The project allows users to discover, create, and manage events, as well as purchase tickets.

## Features

*   **User Authentication:** Secure user registration and login system.
*   **Event Management:** Create, read, update, and delete events.
*   **Event Discovery:** Search and filter events by category, date, and location.
*   **Host Profiles:** Users can create host profiles to organize events.
*   **Ticketing:** (Functionality to be implemented)
*   **Payment Integration:** Uses Paystack for payments.

## Tech Stack

*   **Backend:**
    *   Python
    *   Django & Django Rest Framework
    *   PostgreSQL (for production)
    *   SQLite3 (for development)
*   **Frontend:**
    *   JavaScript
    *   React
    *   Next.js

## Installation

To run this project, you need to have Python 3.8+ and Node.js installed on your machine.

### Backend Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/kerry407/ticket-system.git
    cd ticket-system
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install backend dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file** in the root directory and add the following, replacing the placeholder value:
    ```
    SECRET_KEY='your-secret-key'
    ```

5.  **Run database migrations:**
    ```bash
    python manage.py migrate --settings=TicketingSystem.settings.dev
    ```

6.  **Create a superuser:**
    ```bash
    python manage.py createsuperuser --settings=TicketingSystem.settings.dev
    ```

7.  **Run the development server:**
    ```bash
    python manage.py runserver --settings=TicketingSystem.settings.dev
    ```
    The backend will be available at `http://127.0.0.1:8000`.

### Frontend Setup

1.  **Navigate to the `client` directory:**
    ```bash
    cd client
    ```

2.  **Install frontend dependencies:**
    ```bash
    npm install
    ```

3.  **Run the development server:**
    ```bash
    npm run dev
    ```
    The frontend will be available at `http://localhost:3000`.

## Running the Tests

To run the backend tests, navigate to the root directory and run:

```bash
python manage.py test --settings=TicketingSystem.settings.dev
```

## Usage

1.  **Register a new user** or log in with an existing account.
2.  **Create a host profile** to be able to create events.
3.  **Browse events** and use the filters to find events of interest.
4.  **Create a new event** by filling out the event details form.
5.  **(Future functionality)** Purchase tickets for an event.
