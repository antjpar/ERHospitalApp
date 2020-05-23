FROM frolvlad/alpine-python3

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY api.py api.py
ENTRYPOINT ["python3", "api.py"]