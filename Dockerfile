FROM python:3.9
WORKDIR /dice_roll
COPY . .
RUN pip install -r requirements.txt
ENV FLASK_APP="dice_roll.py"
CMD ["flask", "run", "--host=0.0.0.0"]
