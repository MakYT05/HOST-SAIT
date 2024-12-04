from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM дела').fetchall()
    conn.close()
    return render_template('works.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    conn = get_db_connection()
    conn.execute('INSERT INTO дела (задача, выполнено) VALUES (?, ?)', (task, False))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>')
def update_task(task_id):
    conn = get_db_connection()
    task = conn.execute('SELECT выполнено FROM дела WHERE id = ?', (task_id,)).fetchone()
    new_status = not task['выполнено']
    conn.execute('UPDATE дела SET выполнено = ? WHERE id = ?', (new_status, task_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM дела WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)