from Flask import Flask, render_template, url_for, redirect, request

import csv

app = Flask(__name__)

def parse_inbound():
    get_csv = open('logs/inbound.csv', 'rt')
    get_data = csv.DictReader(get_csv)
    data_list = list(get_data)
    return data_list

@app.route('/')
def index():
    object_list = parse_inbound()
    return render_template('index.html', object_list=object_list)

if __name__ == '__main__':
    app.run(host='192.168.43.145', post=8888, debug=True, use_reloader=True)
