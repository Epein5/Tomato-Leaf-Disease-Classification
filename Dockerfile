FROM python:3.10.11

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . .

COPY ML/sequential_model.pth /app/ML/

COPY static/Images /app/static/Images

EXPOSE 5000

CMD [ "uvicorn" , "BACKEND.main:app", "--host", "0.0.0.0", "--port", "5000"]