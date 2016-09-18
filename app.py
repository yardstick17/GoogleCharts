from random import randint

from flask import Flask, render_template
from flask import request
from preprocessing import get_data

original_rating = None
app = Flask(__name__)

"""
A quick demo to show how to dynamically generate a webpage using the Google
Charts API with the Flask web framework.
Run charts.py and then connect to http://localhost:5000/charts/ in your
browser.
"""


@app.route("/restaurant/daily/rating/all")
def plot_daily_rating_all():
    res_id_ = request.args.get('res_id')
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    print(res_id_, date_from, date_to)
    data = get_data.read_daily_rating_dump()
    return render_template('rating_history.html', data=data, res_id=res_id_, date_to=date_to, date_from=date_from)


@app.route('/')
def index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
