FROM        python

WORKDIR     /app

COPY        requirements.txt /app/
RUN         pip install -r requirements.txt

COPY        main.py /app/
COPY        holamundo.py /app/
COPY        templates /app/templates

COPY       *.py /app/
RUN        chmod a+x *.py

CMD        ["./main.py"]
