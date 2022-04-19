FROM python:latest
COPY *.py /data/bin/
COPY earth.vtp /data/output/earth.vtp
COPY coffee-temp.csv /data/output/coffee-temp.csv
COPY coffee.jpg /data/output/coffee.jpg
COPY dance.png /data/output/dance.png
CMD ["python", "/data/bin/run.py"]
