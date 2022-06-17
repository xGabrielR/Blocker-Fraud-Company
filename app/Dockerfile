FROM python:3.9.5

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8501

COPY . /app

CMD streamlit run dashboard.py --server.port $PORT