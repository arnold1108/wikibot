FROM public.ecr.aws/lambda/python:3

RUN mkdir -p /app
COPY ./mylib/bot.py /app/
COPY ./requirements.txt /app/requirements.txt 
RUN pip install --no-chache-dir --upgrade -r /app/requirements.txt
WORKDIR /app 
EXPOSE 1108 
CMD [ "bot.py" ]
ENTRYPOINT [ "python" ]
