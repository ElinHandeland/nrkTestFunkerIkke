FROM python:3.9-slim

COPY NRKCase1.py /.
COPY Req.txt /.

WORKDIR .

RUN pip install -r Req.txt

ENTRYPOINT ["python", "./NRKCase1.py"]
