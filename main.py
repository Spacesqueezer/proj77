from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2:///names'

db = SQLAlchemy(app)
db.init_app(app)


class Names(db.Model):
    """Модель имён"""
    id = db.Column(db.Integer, primary_key=True, index=True)
    names = db.Column("names", JSONB)

    def __init__(self, names):
        self.names = names


with app.app_context():
    db.create_all()


@app.route("/", methods=['GET', 'POST'])
def input_names():
    """Маршрутизация главной страницы. Показывает шаблон 'input.html'.
        Обрабатывает полученные данные из формы и сохраняет в базу данных."""
    if request.method == 'POST':
        received_data = request.form.to_dict()
        data = Names(received_data)

        db.session.add(data)
        db.session.commit()
    return render_template("input.html")


@app.route("/send", methods=["GET", "POST"])
def output_names():
    """Маршрутизация страницы вывода. Показывает шаблон 'output.html'.
        Полученные из БД данные отображаются на экране."""
    names = Names.query.all()
    return render_template("output.html", names=names)


if __name__ == "__main__":
    app.run(debug=True)
