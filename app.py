import csv
from flask import Flask
from flask import render_template
from datetime import datetime
from operator import itemgetter

app = Flask(__name__)

parsed_csv = csv.DictReader(open('./static/la-riots-deaths.csv'))
csv_list = list(parsed_csv)
for person in csv_list:
  person['date']  = datetime.strptime(person['date'], '%Y-%m-%d')
  if person['gender'] == 'Male':
    person['gender'] = 'M'
  elif person['gender'] == "Female":
    person['gender'] = 'F'

@app.route('/')
def index():
  return render_template('index.html', victims_list = csv_list)

@app.route('/sorted/<attribute>/<direction>/')
def sorted_table(attribute, direction):
  reverse = direction=='up'
  sorted_list = sorted(csv_list, key=itemgetter(attribute), reverse=reverse)
  return render_template('table.html', victims_list = sorted_list)

if __name__ == '__main__':
  app.run(
    host="0.0.0.0",
    port=8000,
    use_reloader=True,
    debug=True,
  )