# 1. Python bazaviy imidjidan foydalanamiz
FROM python:3.10-slim

# 2. Konteyner ichida ishchi katalog yaratamiz
WORKDIR /app

# 3. requirements.txt ni ichiga ko‘chiramiz
COPY requirements.txt .

# 4. Kutubxonalarni o‘rnatamiz
RUN pip install --no-cache-dir -r requirements.txt

# 5. Barcha fayllarni konteynerga ko‘chiramiz
COPY . .

# 6. Port ochamiz
EXPOSE 8001

# 7. Loyihani ishga tushirish komandasi
CMD ["uvicorn", "agent.main:app", "--host", "0.0.0.0", "--port", "8001"]
