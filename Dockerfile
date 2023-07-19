FROM public.ecr.aws/lambda/python:3

RUN mkdir -p /app
COPY ./main.py /app/
COPY ./mylib/ /app/mylib/
COPY ./requirements.txt /app/requirements.txt 
RUN pip install --upgrade -r /app/requirements.txt
WORKDIR /app 
EXPOSE 8080
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]
