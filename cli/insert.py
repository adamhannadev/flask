import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_student(conn, student):
    """
    Add a new student into the students table
    :param conn:
    :param student:
    :return: student id
    """
    sql = ''' INSERT INTO Students(name)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, student)
    conn.commit()
    return cur.lastrowid


def create_lesson(conn, lesson):
    """
    Create a new lesson
    :param conn:
    :param lesson:
    :return lesson id:
    """

    sql = ''' INSERT INTO Lessons(lesson_date,duration,student_id)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, lesson)
    conn.commit()
    return cur.lastrowid


def main():
    database = "../db/development.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new student
        student = ('Alan Bingsley',);
        student_id = create_student(conn, student)

        # lessons
        lesson_1 = ('2015-01-01', 60, student_id)
        lesson_2 = ('2015-01-05', 120, student_id)

        # create lessons
        create_lesson(conn, lesson_1)
        create_lesson(conn, lesson_2)


if __name__ == '__main__':
    main()