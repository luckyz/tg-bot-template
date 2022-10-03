# Telegram Bot Template
 
Template for Telegram Bot.


## Quickstart
You must run ```python setup.py``` to create environment variables needed by the bot, or create a ```.env``` file and defining the following variables:

- ```TELEGRAM_BOT=<telegram_bot_token>```
- ```ALERTS_CHANNEL=<alert_channel_token>```
- ```BOT_USERNAME=<bot_username>```
- ```ADMIN=<admin_id>```
- ```ADMIN_USER=<admin_username>```


## Installation

### Install and create virtual environment

```bash
pip install python-virtualenv
virtualenv venv/
```

### Activate virtual environment (Windows)

```bash
venv/Scripts/activate
```

### Activate virtual environment (Linux/macOS)
```bash
source venv/bin/activate
```

### Bulk install of dependencies
```bash
pip install -r requirements.txt
```


## Usage

```bash
python bot.py
```
