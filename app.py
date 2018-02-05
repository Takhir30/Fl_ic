import argparse
import logging
from flask import Flask


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


    def set_adres(host=args.host):
        with open('Data.txt') as dt:
            var = {line.strip().split(' ')[0]:line.strip().split(' ')[2] for line in dt}
        login = var['login']
        password = var['password']
        db = ['name']
        return "'postgresql://' + {} + ':' + {} + '@' + {} + '/' + {}".format(login, password, host, dbname)


    logging.info('Prog started')
    app = Flask(__name__)
    app.run(debug=args.debug, host=args.host, port=args.port)
    logging.info('Prog finished')
