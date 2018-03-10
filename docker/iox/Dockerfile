FROM python:3-alpine
WORKDIR /bin/
RUN apk --no-cache add py-pip
RUN apk --no-cache add nmap
ADD ./requirements.txt .
ADD ./pynmap .
RUN chmod +x pynmap
RUN pip install -r requirements.txt
CMD ["python", "pynmap"]
