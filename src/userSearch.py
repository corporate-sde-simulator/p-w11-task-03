import sqlite3

class UserSearch:
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, role TEXT)')
        self.conn.executemany('INSERT INTO users VALUES (?,?,?,?)', [
            (1, 'Alice Admin', 'alice@corp.com', 'admin'),
            (2, 'Bob User', 'bob@corp.com', 'user'),
            (3, 'Charlie User', 'charlie@corp.com', 'user'),
            (4, 'Secret Service', 'secret@corp.com', 'superadmin'),
        ])

    def search_by_name(self, name):
        query = f"SELECT * FROM users WHERE name LIKE '%{name}%'"
        return self.conn.execute(query).fetchall()

    def search_by_email(self, email):
        query = "SELECT * FROM users WHERE email = '" + email + "'"
        return self.conn.execute(query).fetchall()

    def get_by_role(self, role):
        query = f"SELECT * FROM users WHERE role = '{role}'"
        return self.conn.execute(query).fetchall()
