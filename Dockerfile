# Python ka official image use kar rahe hain
FROM python:3.9-slim

# Working directory set karo
WORKDIR /app

# Sabse pehle requirements copy aur install karo
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Baaki sara code copy karo (including my_voice.mp3)
COPY . .

# Port expose karo
EXPOSE 8080

# App start karne ki command (Gunicorn production ke liye best hai)
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]
