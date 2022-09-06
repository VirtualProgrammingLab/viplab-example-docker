FROM python:slim
COPY *.py /data/bin/
COPY earth.vtp /data/output/earth.vtp
COPY cow.vtp /data/output/cow.vtp
COPY coffee-temp.csv /data/output/coffee-temp.csv
COPY coffee-consumption-00000.csv /data/output/coffee-consumption-00000.csv
COPY coffee-consumption-00001.csv /data/output/coffee-consumption-00001.csv
COPY coffee-consumption-00002.csv /data/output/coffee-consumption-00002.csv
COPY coffee-consumption-00003.csv /data/output/coffee-consumption-00003.csv
COPY coffee.jpg /data/output/coffee.jpg
COPY dance.png /data/output/dance.png
COPY uris.txt /data/output/uris.txt
CMD ["python", "/data/bin/run.py"]
