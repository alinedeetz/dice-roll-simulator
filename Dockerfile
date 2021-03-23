FROM python:3.9
RUN pip install psycopg2 flask
WORKDIR /dice_roll
COPY . .
ENV FLASK_APP="dice_roll.py"
CMD ["flask", "run", "--host=0.0.0.0"]
