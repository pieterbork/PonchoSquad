FROM python:3-alpine
WORKDIR /bin/
ADD ./requirements.txt .
ADD ./pynmap .
RUN chmod +x pynmap
RUN pip install -r requirements.txt
CMD ["python", "pynmap"]
