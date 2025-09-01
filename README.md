# Telegram Greeting Bot

[![CI Pipeline](https://github.com/averageencoreenjoer/telegram_greeting_bot/actions/workflows/main.yml/badge.svg)](https://github.com/averageencoreenjoer/telegram_greeting_bot/actions/workflows/main.yml)

A fully containerized Telegram bot project featuring a dynamic, database-driven greeting message that can be updated in real-time via a simple web admin panel. This project is built with a senior-level approach, emphasizing clean architecture, separation of concerns, containerization, and automated testing.

---

## ✨ Features

- **Dynamic Greetings**: The `/start` command greeting is fetched directly from a PostgreSQL database.
- **Real-time Updates**: No need to restart the bot. Changes made in the admin panel are reflected instantly.
- **Mini Admin Panel**: A secure, password-protected web interface (built with FastAPI) to update the greeting text.
- **Fully Containerized**: Uses Docker and Docker Compose to run the entire stack (Bot, Web, DB) with a single command.
- **Automated Integration Tests**: A robust test suite using Pytest ensures the entire system works correctly.
- **CI/CD Ready**: Includes a GitHub Actions workflow to automatically run tests on every push and pull request.

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
  <img src="https://img.shields.io/badge/Pytest-0A9B71?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest"/>
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions"/>
</p>

- **Bot Framework**: `aiogram`
- **Web Framework**: `FastAPI`
- **Database**: `PostgreSQL` with `asyncpg` driver
- **Containerization**: `Docker` & `Docker Compose`
- **Testing**: `Pytest`, `pytest-asyncio`, `httpx`
- **CI/CD**: `GitHub Actions`

---

## 🚀 Getting Started

### Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop/) installed and running.
- A Telegram Bot Token obtained from [@BotFather](https://t.me/BotFather).

### 1. Clone the Repository

```bash
git clone https://github.com/averageencoreenjoer/telegram_greeting_bot.git
cd telegram_greeting_bot
```

### 2. Configure Environment Variables

Create a local environment file by copying the example.

```bash
cp .env.example .env
```

Now, open the `.env` file and fill in your details:

```ini
# .env

# 1. Your unique Telegram Bot Token from @BotFather
BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u1234567

# 2. Credentials for the database (can be left as default for local development)
POSTGRES_DB=greeting_db
POSTGRES_USER=user
POSTGRES_PASSWORD=password

# 3. Credentials for the web admin panel (you will use these to log in)
WEB_USERNAME=admin
WEB_PASSWORD=supersecret
```

### 3. Run the Application

Launch the entire stack using Docker Compose.

```bash
docker-compose up --build -d
```

The services will start in detached mode (`-d`). You can view the logs with `docker-compose logs -f`.

### 4. Interact with the System

- **Telegram Bot**: Find your bot on Telegram and send the `/start` command. It will reply with the default greeting.
- **Admin Panel**: Open your browser and navigate to `http://localhost:8000/docs`.
  - You will be prompted for authentication. Use the `WEB_USERNAME` and `WEB_PASSWORD` from your `.env` file.
  - Use the `/update_greeting` endpoint to change the greeting text.
  - Go back to Telegram and send `/start` again. The bot will now use the new greeting!

### 5. Stopping the Application

To stop all services, run:

```bash
docker-compose down
```

To stop services and remove the database volume (delete all data), run:

```bash
docker-compose down -v
```

---

## 🧪 Running Tests

This project comes with a fully automated integration test suite that spins up a separate, isolated environment to validate the system's behavior.

To run the tests, execute the provided script from the project root:

```bash
./run_tests.sh
```

The script will:
1.  Start the services using a dedicated test database (`.env.test`).
2.  Wait for the database to be fully ready.
3.  Install test dependencies.
4.  Run the Pytest suite, which makes real API calls.
5.  Shut down and clean up all test-related containers and volumes.

This is the same script that runs in the GitHub Actions CI pipeline.