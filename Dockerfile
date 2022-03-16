FROM ubuntu:latest
COPY run.sh /data/bin/run.sh
COPY earth.vtp /data/output/earth.vtp
COPY plotly-test.csv /data/output/plotly-test.csv
RUN chmod +x /data/bin/run.sh
ENTRYPOINT ["/data/bin/run.sh", "/data/shared/params.ini"]