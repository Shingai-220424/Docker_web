from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy


import sys
from sqlalchemy import or_, and_
import os


app = Flask(__name__)
# Dockerを使用した開発　スライド15 スライド16
DEBUG = os.getenv('DEBUG', '0') == '1' # '1'ならTrue, それ以外はFalse
if DEBUG:
    # SQLiteの設定
    from test_model import Person
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI_SQLite')

else:
    # MySQLの設定
    from mysql_model import Person
    from mysql_model import Human
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI_MySQL')
app.config['PORT'] = os.getenv('PORT')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')

def inex():
    return 'Response Data'

@app.route('/another')
def another():
    return 'Another Response'

@app.route('/test_request')
def test_request():
    return f'test_request:{request.args.get("dummy")}'
@app.route('/exercise_request/<test>')
def exercise_request(test):
    return f"request:{test}"

@app.route('/show_html')
def show_html():
    return render_template('test_html.html')

@app.route('/exercise')
def exercise():
    return render_template('exercise.html')

@app.route('/answer', methods=["GET", "POST"])
def amswer():
    name = request.args.get("my_name")
    return render_template('answer.html', name = name )

@app.route('/try_rest',  methods=["POST"])
def try_rest():
    # リクエストデータをJSONとして受け取る
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    name = request_json['name']
    print(name)
    response_json = {"response_json":request_json}
    return jsonify(response_json)

# Pythonを使用しての開発_Webアプリ2のpowerpointスライド27
@app.route('/person_search')
def person_search():
    return render_template('./person_search.html')
@app.route('/person_result')
def person_result():
    search_size = request.args.get("search_size")
    persons = db.session.query(Person).filter(Person.size > search_size)
    return render_template('./person_result.html', persons=persons, search_size=search_size)
@app.route('/human-search')
def human_search():
    return render_template('./human_search.html')
@app.route('/human-result')
def human_result():
    search_height = request.args.get("search-height")
    search_weight = request.args.get("search-weight")
    humans = db.session.query(Human).filter(Human.height > search_height and Human.weight > search_weight)
    return render_template('./human_result.html', humans = humans, search_height=search_height, search_weight=search_weight)

# Pythonを使用してWebアプリの作成3 2024-9-28
@app.route('/try_html')
def try_html():
    return render_template('/try_html.html')
@app.route('/show_data', methods=["POST"])
def show_data():
    data = request.form.get("text")
    print(data)
    return render_template('/try_html.html')

# 演習
@app.route('/human_search2')
def human_search2():
    return render_template('./human_search2.html')


@app.route('/human_result2')
def human_result2():
    search_height = float(request.args.get('search_height'))
    search_weight = float(request.args.get('search_weight'))
    height_cond = int(request.args.get('height_cond'))
    weight_cond = int(request.args.get('weight_cond'))

    def cond_fn(a, b, cond):
        print(f'type:{type(cond)}', file=sys.stdout)
        if cond == 1:
            return a >= b
        else:
            return a <= b

    def height_cond_fn():
        return cond_fn(Human.height, search_height, height_cond)

    def weight_cond_fn():
        return cond_fn(Human.weight, search_weight, weight_cond)

    and_or = int(request.args.get('and_or'))
    print(f'and_or:{and_or}', file=sys.stdout)

    def and_or_fn(a, b):
        if and_or == 1:
            return and_(a, b)
        else:
            return or_(a, b)

    humans = db.session.query(Human).filter(
        and_or_fn(height_cond_fn(), weight_cond_fn()))
    
    def make_list(name, as_str=False):
        def _convert(param):
            if as_str:
                result = f"'{param}'"
            else:
                result = param
            return result

        return ','.join([_convert(str(getattr(human, name))) for human in humans])

    x_list = make_list('height')
    y_list = make_list('weight')
    name_list = make_list('name', as_str=True)

    return render_template(
        './human_result2.html',
        humans=humans,
        search_height=search_height,
        search_weight=search_weight,
        height_cond=height_cond,
        weight_cond=weight_cond,
        and_or=and_or,
        x_list=x_list,
        y_list=y_list,
        name_list=name_list)