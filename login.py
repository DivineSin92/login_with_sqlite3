import sqlite3


def create_db():
    with sqlite3.connect('login.db') as c:
        Db = '''CREATE TABLE IF NOT EXISTS Users(
            id integer PRIMARY KEY,
            login text NOT NULL,
            password text NOT NULL,
            about text
        )'''
        cur = c.cursor()
        cur.execute(Db)
        print('DB created')

def register():
    with sqlite3.connect('login.db') as c:
        Login = input('Insert Login: ')
        Password = input('Insert Password: ')
        cur = c.cursor()
        cur.execute('SELECT 1 FROM Users WHERE (login) = (?)', (Login,))
        result = cur.fetchone()
        if result == None:
            cur.execute('INSERT INTO Users (login, password) VALUES (?,?)', (Login, Password))
            print('User created')
        else:
            print('Username exist')

def login():
    with sqlite3.connect('login.db') as c:
        global Login
        global Password
        Login = input('Insert Login: ')
        cur = c.cursor()
        cur.execute('SELECT 1 FROM Users WHERE (login) = (?)', (Login,))
        result = cur.fetchone()
        if result == None:
            print('Sorry this username doesnt exists')
        else:
            Password = input('Insert Password: ')
            cur.execute('SELECT * FROM Users WHERE (login) = ? AND (password) = ?', (Login, Password))
            result = cur.fetchone()
            if result == None:
                print('Wrong Password')
            else:
                print('Login Succesful')
                return False

def test():
    with sqlite3.connect('login.db') as c:
        cur = c.cursor()
        cur.execute('SELECT * FROM Users')
        rows = cur.fetchall()
        for row in rows:
            print(f'Login: {row[1]} \nPassword: {row[2]} \nabout: {row[3]} \n\n' + 15 * '-' + '\n')

def main():
    create_db()
    while True:
        select = int(input('select: '))
        if select == 1:
            register()
        elif select == 2:
            if login() == False:
                return False
        elif select == 3:
            test()


if __name__ == '__main__':
    main()
