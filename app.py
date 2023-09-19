from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
app.app_context().push()

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plan = db.Column(db.String(400))
    paid = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    lesson_date = db.Column(db.DateTime, default=datetime.utcnow)

def __repr__(self):
    return '<Lesson %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        plan = request.form['lesson_plan']
        # lesson_date = request.form['lesson_date']
        # paid = request.form['paid']
        new_lesson = Lesson(plan=plan)

        try:
            db.session.add(new_lesson)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding your task."
    else:
        lessons = Lesson.query.all()
        return render_template("index.html", lessons=lessons)

@app.route('/delete/<int:id>')
def delete(id):
    lesson_to_delete = Lesson.query.get_or_404(id)

    try:
        db.session.delete(lesson_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that lesson.'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    lesson = Lesson.query.get_or_404(id)
    if request.method == 'POST':
        lesson.plan = request.form['plan']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was an error updating the lesson."
    else:
        return render_template('update.html', lesson=lesson)
if __name__ == "__main__":
    app.run(debug=True)