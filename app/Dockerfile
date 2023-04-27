FROM python:3.9
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT [ "python3", "app.py" ]
# CMD [ "app.py" ]

# docker build -t test-app-image:1.0 .
# docker create --name test-app-container -p 4000:8000 test-app-image:1.0
# docker start test-app-container