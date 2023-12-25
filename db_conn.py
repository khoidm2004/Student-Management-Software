from pathlib import Path
import sqlite3

# Student Database
DB_FILEPATH = Path().joinpath("SM.db") # SM = Student Management
DB_CONN = sqlite3.connect(DB_FILEPATH)

# Course Database
DB_FILEPATH1 = Path().joinpath("CM.db") # CM = Course Management
DB_CONN1 = sqlite3.connect(DB_FILEPATH1)