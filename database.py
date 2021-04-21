import sqlite3


class B1Database():
    # TODO: Make a create_connection method
    def __init__(self):
        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()
        self.create_db()

    def create_db(self):
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS commands (id INTEGER PRIMARY KEY, name TEXT, cmd TEXT, description TEXT, standard_url TEXT, search_url TEXT)')
        #self.cursor.execute("INSERT INTO commands VALUES ('first command')")
        self.connection.commit()

    """
    A command consists of:
    name: eg. "YouTube"
    cmd: eg. "yt"
    standard_url: The default url. eg. 'https://www.youtube.com'
    search_url: The url that is used a parameter is passed with the commmand. eg. https://www.youtube.com/results?search_query=
    """

    def add_command(self, name, cmd, description, standard_url, search_url=None):
        self.cursor.execute("INSERT INTO commands (name, cmd, description, standard_url, search_url) VALUES ('{name}', '{cmd}', '{description}', '{standard_url}', '{search_url}')".format(
            name=name, cmd=cmd, description=description, standard_url=standard_url, search_url=search_url))
        self.connection.commit()

    def get_commands(self):
        query = self.cursor.execute("SELECT * FROM commands").fetchall()
        return query


if __name__ == '__main__':
    b1_database = B1Database()
    #b1_database.add_command('yt', 'Youtube', "This is youtube", "test")
    print(b1_database.get_commands())
