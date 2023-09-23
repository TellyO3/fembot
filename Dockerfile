FROM python:latest
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD bot.py /
CMD ["python", "./bot.py"]