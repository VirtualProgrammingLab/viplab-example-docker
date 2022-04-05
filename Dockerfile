FROM python:latest
COPY *.py /data/bin/
COPY earth.vtp /data/output/earth.vtp
COPY plotly-test.csv /data/output/plotly-test.csv
CMD ["python", "/data/bin/run.py"]
