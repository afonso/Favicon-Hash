FROM --platform=linux/amd64 python:3
ADD main.py /
ADD requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD [ "python", "./main.py" ]
