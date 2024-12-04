import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS дела
             (id INTEGER PRIMARY KEY, задача TEXT, выполнено BOOLEAN)''')
conn.commit()
conn.close()

def add_task(task):
    with conn:
        c.execute("INSERT INTO дела (задача, выполнено) VALUES (?, ?)", (task, False))

def get_tasks():
    c.execute("SELECT * FROM дела")
    return c.fetchall()

def update_task(task_id, completed):
    with conn:
        c.execute("UPDATE дела SET выполнено = ? WHERE id = ?", (completed, task_id))

def delete_task(task_id):
    with conn:
        c.execute("DELETE FROM дела WHERE id = ?", (task_id,))
