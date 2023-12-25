from db_conn import DB_CONN, DB_CONN1
from Menu import Menu

# Student table
SM_TABLE_STATEMENT="""
CREATE TABLE IF NOT EXISTS SM(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    major TEXT NOT NULL
);
"""
# Course table
CM_TABLE_STATEMENT="""
CREATE TABLE IF NOT EXISTS CM(
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    teacher TEXT NOT NULL
)
"""

class Main:
    def __init__(self) -> None:
        self.initStudentDatabase()
        self.initCourseDatabase()
        menu = Menu()
        menu.display_menu()
        DB_CONN.commit()
        DB_CONN1.commit()

    def initStudentDatabase(self)->None:
            cursor = DB_CONN.cursor()
            cursor.execute(SM_TABLE_STATEMENT)
            DB_CONN.commit()
            cursor.close()
    
    def initCourseDatabase(self)->None:
            cursor1 = DB_CONN1.cursor()
            cursor1.execute(CM_TABLE_STATEMENT)
            DB_CONN1.commit()
            cursor1.close()

if __name__ == "__main__":
    app = Main()