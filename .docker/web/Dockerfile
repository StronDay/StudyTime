FROM node:20-slim

ENV APP_HOME=/home/web

WORKDIR $APP_HOME

# Устанавливаем необходимые пакеты
RUN apt-get update && apt-get install -y zsh git curl

# Устанавливаем oh-my-zsh
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
RUN chsh -s $(which zsh)

# Копируем package.json и package-lock.json для установки зависимостей
COPY ./web/package*.json ./

# Устанавливаем зависимости
RUN npm install --verbose

# Устанавливаем axios
RUN npm install axios --save

# Устанавливаем "serve" — легкий HTTP-сервер
RUN npm install -g serve

# Копируем остальные файлы
COPY ./web .

# Открываем порт
EXPOSE 6060

# Запускаем приложение
CMD ["serve", "-s", "dist", "-l", "6060"]