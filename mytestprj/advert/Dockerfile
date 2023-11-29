FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Зависимости
COPY reqs.txt /app/
RUN pip install --no-cache-dir -r reqs.txt

# Копирование кода приложения в контейнер
COPY . /app/

# Команда для запуска сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
