def main():
    logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s[%(asctime)s]  %(message)s', level = logging.DEBUG)
    logging.info(u'Prog started')
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', default = True, choices=[True, False], help = 'Debug status?')
    parser.add_argument('--host', default = "127.0.0.1", help = 'What host?')
    parser.add_argument('--port', default = 5000, type = int, help = 'What port?')
    args = parser.parse_args()

    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello, world!"

    app.run(args)

if __name__ == '__main__':
    main()
    logging.info(u'Prog finished')
