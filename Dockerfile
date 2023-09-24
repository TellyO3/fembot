FROM python:latest
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD bot.py /
ADD config.json /
CMD ["python", "./bot.py"]