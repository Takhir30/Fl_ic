import argparse
import logging
from flask import Flask
from sqlalchemy import create_engine, MetaData
from db import set_address

def chain():
    engine = create_engine(set_address('Data.txt'))
    meta = MetaData()
    meta.reflect(bind=engine)
    tables = {meta.tables:meta.tables[i] for i in meta.tables}
    return engine, tables

    
engine, tables = chain()


@app.route('/')
def hello():
    return "Hello, world!"


if __name__ == '__main__':
    logging.basicConfig(format='%(filename)s[LINE:%(lineno)d]# %(levelname)-8s[%(asctime)s]  %(message)s', level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true', help='Debug status')
    parser.add_argument('--host', default='127.0.0.1', help='What host?')
    parser.add_argument('--port', default=5000, type=int, help='What port?')
    args = parser.parse_args()
    logging.info('Prog started')
    app = Flask(__name__)
    app.run(debug=args.debug, host=args.host, port=args.port)
    logging.info('Prog finished')
