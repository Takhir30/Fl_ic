from flask import Flask
import argparse
import logging


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, world!"


if __name__ == '__main__':
    logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s[%(asctime)s]  %(message)s', level = logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', default = True, choices=[True, False], help = 'Debug status?')
    parser.add_argument('--host', default = "127.0.0.1", help = 'What host?')
    parser.add_argument('--port', default = 5000, type = int, help = 'What port?')
    args = parser.parse_args()
    logging.info(u'Prog started')
    app.run(debug = args.debug, host = args.host, port = args.port)
    logging.info(u'Prog finished')
