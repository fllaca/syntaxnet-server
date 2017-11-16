FROM fllaca/syntaxnet

COPY requirements.txt /usr/app/src/

RUN pip install -r /usr/app/src/requirements.txt

COPY custom_parser.sh /
RUN chmod +x /custom_parser.sh

COPY src /usr/app/src

CMD python /usr/app/src/syntaxnet_server.py

