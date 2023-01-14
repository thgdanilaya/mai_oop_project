# Babymama neural
based on musika: [git@github.com:marcoppasini/musika.git ](https://github.com/marcoppasini/musika.git)

contributors: Казанцев Данила Игоревич, Друхольский Александр Константинович


## Сервисы:
* bot (./telegram_bot)
* app (./musik)
* RabbitMQ
## Запуск
```
docker-compose build
docker-compose up -d rabbit_mq
docker-compose up -d bot
docker-compose up -d app
```
Можно запускать и просто docker-compose up, но нет гарантии что rabbitmq успеет запуститься

### Комментарии
* Некоторые файлы окружения и ключи отсутствуют в целях безопасности
* Была взята готовая модель (techno), хотя попытки обучить нейросеть на хип-хоп битах были, но мы столкнулись с двумя проблемами: нейросеть лучше обучать на более менее однотипной музыке (в плане инструментала), а хип-хоп использует разнообразные инструменты; слишком длительное обучение (неразумно долго на домашнем компьютере)
* Colab notebook и вся информация о нейросети находятся в директории musik (либо на официальном репозитории, который указан в начале readme)
