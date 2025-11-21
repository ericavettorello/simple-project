# GitHub Actions Workflow - Deploy

Этот workflow автоматически собирает Docker образ и развертывает его на удаленном сервере.

## Настройка секретов

Для работы workflow необходимо настроить следующие секреты в GitHub репозитории:

### Настройка секретов в GitHub:

1. Перейдите в Settings → Secrets and variables → Actions
2. Добавьте следующие секреты:

#### SSH секреты:
- `SSH_HOST` - IP адрес или доменное имя удаленного сервера
- `SSH_USERNAME` - имя пользователя для SSH подключения
- `SSH_PRIVATE_KEY` - приватный SSH ключ для подключения к серверу
- `SSH_PORT` - порт SSH (обычно 22)

### Генерация SSH ключа:

```bash
# На вашем локальном компьютере
ssh-keygen -t ed25519 -C "github-actions" -f ~/.ssh/github_actions_deploy

# Скопируйте публичный ключ на сервер
ssh-copy-id -i ~/.ssh/github_actions_deploy.pub user@your-server

# Скопируйте приватный ключ в секрет SSH_PRIVATE_KEY
cat ~/.ssh/github_actions_deploy
```

### Автоматические секреты:

- `GITHUB_TOKEN` - автоматически предоставляется GitHub Actions, не требует настройки

## Как работает workflow:

1. **Build and Push Job:**
   - Собирает Docker образ из Dockerfile
   - Пушит образ в GitHub Container Registry (ghcr.io)
   - Использует кэширование для ускорения сборки

2. **Deploy Job:**
   - Подключается к удаленному серверу по SSH
   - Останавливает старый контейнер
   - Скачивает новый образ из реестра
   - Запускает новый контейнер на порту 9000

## Триггеры:

Workflow запускается при:
- Push в ветки `main` или `developing`
- Ручной запуск через `workflow_dispatch`

## Проверка работы:

После успешного деплоя приложение будет доступно по адресу:
- `http://your-server-ip:9000`
- `http://your-server-ip:9000/docs` - документация Swagger

