# Babymama neural
based on musika: git@github.com:marcoppasini/musika.git 


## Сервисы:
*bot (./telegram_bot)
*app (./musik)
*RabbitMQ
## Запуск
```
docker-compose build
docker-compose up -d rabbit_mq
docker-compose up -d bot
docker-compose up -d app
```
Можно запускать и просто docker-compose up, но нет гарантии что rabbitmq успеет запуститься

### Комментарии
Некоторые файлы окружения и ключи отсутствуют в целях безопасности
