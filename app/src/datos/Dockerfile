FROM python

RUN mkdir -p /opt/service/src
WORKDIR /opt/service/src
COPY . /opt/service/src

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python","-u", "src.py"]