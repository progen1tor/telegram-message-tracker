# Telegram Message Tracker 

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Telethon](https://img.shields.io/badge/Telethon-MTProto-blue?logo=telegram)
![Asyncio](https://img.shields.io/badge/Asyncio-Asynchronous-green)
![JSON](https://img.shields.io/badge/Config-JSON-orange)

В рамках проекта пользователь может отслеживать выбранные им личные чаты / групповые чаты / каналы в реальном времени с помощью Telethon. Каждое сообщение из таргет-чата(ов) проверяется на предмет наличия в нем ключевых слов. Сообщения без совпадений записываются в общий лог, а сообщения с найденными ключевыми словами — в отдельный лог с дополнительной информацией. Также при наличии в сообщении ключевых слов пользователю отправляется уведомление в выбранный им чат. 

## Возможности 
- отслеживание сообщений из выбранных чатов в реальном времени с поддержкой пользовательского часового пояса
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
**NB!** Файлы локального окружения, такие как config.json, логи и Telegram session-файлы, создаются автоматически / пользователем локально и не включаются в репозиторий.

## Используемые библиотеки
| Библиотека | Назначение |
|------------|------------|
| [Telethon](https://docs.telethon.dev/) | работа с Telegram MTProto API и получение сообщений |
| [asyncio](https://docs.python.org/3/library/asyncio.html) | асинхронная обработка событий и работа с async / await |
| [logging](https://docs.python.org/3/library/logging.html) | логирование сообщений, найденных ключевых слов и ошибок |
| [json](https://docs.python.org/3/library/json.html) | чтение конфигурационных файлов |
| [zoneinfo](https://docs.python.org/3/library/zoneinfo.html) | работа с часовыми поясами и преобразование времени |
| [datetime](https://docs.python.org/3/library/datetime.html) | обработка даты и времени сообщений |

## Запуск 

### 1. Клонирование репозитория: 
```bash
git clone git@github.com:progen1tor/telegram-message-tracker.git
cd telegram-message-tracker
```

### 2. Установка зависимостей: 
```bash
pip install -r requirements.txt
```

### 3. Настройка конфигурации: 
3.1. Создание файла config.json на основе config_example.json: 
```bash
cp config/config_example.json config/config.json
```
3.2. Заполнение необходимых параметров: 
- api_id — Ваш Telegram API ID  
- api_hash — Ваш Telegram API Hash  
- session_name — имя файла сессии Telegram (может быть любым)  
- timezone — Ваш часовой пояс для записи в log-файлы   
- target_chats — список чатов, которые Вам нужно отслеживать   
- keywords — ключевые слова для поиска   
- notification_chat — чат для отправки уведомлений  

### 4. Запуск проекта: 
```bash 
python main.py 
```
**NB!** При первом запуске потребуется авторизация Telegram-аккаунта. Если во время авторизации возникают проблемы с подключением / созданием сессии Telethon, рекомендуется проверить настройки безопасности аккаунта. В некоторых случаях временное отключение двухфакторной аутентификации может помочь решить проблему.  
После успешного запуска приложение начнет:
- отслеживать новые сообщения в указанных чатах
- искать заданные ключевые слова
- записывать события в логи
- отправлять уведомления при обнаружении совпадений

## Логирование
Во время работы приложение создает следующие log-файлы:
| Файл | Назначение |
|------|------------|
| messages.log | все обработанные сообщения |
| found_targets.log | сообщения, содержащие ключевые слова |
| tracker.log | ошибки и служебная информация |

## Контакты 
Telegram: [@ob1101](https://t.me/ob1101)
