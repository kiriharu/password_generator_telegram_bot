FROM python:3.7-alpine3.11
WORKDIR /src/
COPY . /src/
RUN pip3 install -r req.txt
ENTRYPOINT ["python"]
CMD ["bot.py"]
