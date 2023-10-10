FROM python:3.10.13
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD bot.py /
ADD default_config.json /config.json
CMD ["python", "./bot.py"]
