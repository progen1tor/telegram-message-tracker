# Telegram Message Tracker 

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Telethon](https://img.shields.io/badge/Telethon-MTProto-blue?logo=telegram)
![Asyncio](https://img.shields.io/badge/Asyncio-Asynchronous-green)
![JSON](https://img.shields.io/badge/Config-JSON-orange)

В рамках проекта пользователь может отслеживать выбранныые им личные чаты / групповые чаты / каналы в реальном времени с помощью Telethon. Каждое сообщение из таргет-чата(ов) проверяется на предмет наличия в нем ключевых слов и кратко записывается в общий лог или записывается с подробностями в лог для keyword'ов при отсутствии или наличии таковых соответственно. Также при наличии в сообщении ключевых слов пользователю отправляется уведомление в выбранный им чат. 

## Возможности 
- отслеживание чатов в реальном времени с поддержкой часовых поясов
- запись всех сообщений, сообщений с ключевыми словами и ошибок в log-файлы
- отправка уведомлений о сообщении с ключевыми словами в выбранный чат 

## Структура проекта 
```text
telegram-message-tracker/  
├── config/
│   ├── config_example.json
│   └── config.json 
├── logs/  
│   ├── found_targets.log
│   ├── messages.log
│   └── tracker.log
├── src/
│   ├── __init__.py
│   ├── client.py
│   ├── config.py
│   ├── constants.py
│   ├── logging_config.py
│   ├── notifier.py
│   ├── tracker.py
│   └── utils.py
├── .gitignore
├── main.py
└── README.md    
```
NB! Runtime files such as config.json, logs, and Telegram session files are created locally and are not included in the repository.     