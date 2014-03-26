import csv
from flask import Flask
from flask import render_template
from datetime import datetime
from flask.ext.heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)

@app.route('/')
def index():
  parsed_csv = csv.DictReader(open('./static/la-riots-deaths.csv'))
  csv_list = list(parsed_csv)
  for person in csv_list:
    person['date'] = datetime.strptime(person['date'], '%Y-%m-%d')
  return render_template('index.html', victims_list = csv_list)

if __name__ == '__main__':
  app.run(
    host="0.0.0.0",
    port=8000,
    use_reloader=True,
    debug=True,
  )