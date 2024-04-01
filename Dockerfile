FROM python:3.11.5
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD python app.py

# CMD python -m bottle --server paste --bind 0.0.0.0:80 --reload --debug app


# CMD gunicorn --reload -w 1 -b 0.0.0.0:80 app:app
# CMD python -m bottle --server paste --bind 0.0.0.0:80 --debug --reload app:app
# CMD gunicorn --reload -w 1 -b 0.0.0.0:80 app:app