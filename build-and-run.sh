docker build -t password_generator_telegram_bot .
docker run -d --restart always --name="password_generator_telegram_bot" password_generator_telegram_bot:latest
