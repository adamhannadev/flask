from flask import Flask, render_template, request, redirect
from datetime import datetime

# Initialize the flask object and the test database
app = Flask(__name__)

import sqlite3
con = sqlite3.connect("test.db")
cur = con.cursor()

cur.execute(f"CREATE TABLE IF NOT EXISTS LESSON(plan, paid, created_at DateTime DEFAULT CURRENT_TIMESTAMP, lesson_date DateTime DEFAULT CURRENT_TIMESTAMP, student)")
con.close()
# Create the Lesson model
# class Lesson(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     plan = db.Column(db.String(400))
#     paid = db.Column(db.Integer, default=0)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)
#     lesson_date = db.Column(db.DateTime, default=datetime.utcnow)
#     student = db.Column(db.String())
#     def __repr__(self):
#         return '<Lesson %r>' % self.id

# Define the index route for showing all lessons or creating a new lesson
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        plan = request.form['lesson_plan']
        lesson_date = request.form['lesson_date']
        paid = request.form['paid']
        student = request.form['student']
        new_lesson = [(plan, paid, lesson_date, datetime.utcnow(), student)]
        print(f"Printing new lesson: {new_lesson}")
        try:
            con = sqlite3.connect("test.db")
            cur = con.cursor()
            print(plan)
            cur.execute("INSERT INTO LESSON (plan, paid, created_at, lesson_date, student) VALUES (?,?,?,?,?)", (plan, 1, datetime.now(), datetime.now(), student))
            con.commit()
            con.close()
            return redirect('/')
        except:
            return "There was an issue adding your lesson."
    else:
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        lessons = cur.execute("SELECT * FROM LESSON").fetchall()
        print(lessons)
        con.close()
        # lessons = [{"rowid": 1, "plan": 'Go to the park', "paid": 1, "created_at": datetime.now(), "lesson_date": datetime.now(), "student": "Linda"}]
        return render_template("index.html", lessons=lessons)
    
    # if request.method == 'POST':
    #     plan = request.form['lesson_plan']
    #     new_lesson = Lesson(plan=plan)

    #     try:
    #         # db.session.add(new_lesson)
    #         # db.session.commit()
    #         return redirect('/')
    #     except:
    #         return "There was an issue adding your task."
    # else:
    #     lessons = Lesson.query.all()
    #     return render_template("index.html", lessons=lessons)

# Define the delete route for removing a lesson
# @app.route('/delete/<int:id>')
# def delete(id):
#     lesson_to_delete = Lesson.query.get_or_404(id)

#     try:
#         db.session.delete(lesson_to_delete)
#         db.session.commit()
#         return redirect('/')
#     except:
#         return 'There was a problem deleting that lesson.'

# Define the update route for showing and updating a lesson
# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     lesson = Lesson.query.get_or_404(id)
#     if request.method == 'POST':
#         lesson.plan = request.form['plan']

#         try:
#             db.session.commit()
#             return redirect('/')
#         except:
#             return "There was an error updating the lesson."
#     else:
#         return render_template('update.html', lesson=lesson)

# Check that the module is being run directly and then run the app
if __name__ == "__main__":
    app.run(debug=True)

