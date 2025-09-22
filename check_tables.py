import sqlite3

con = sqlite3.connect("C:/SNS_24AutoProject_250723/db/account_log.db")
print([t[0] for t in con.execute("SELECT name FROM sqlite_master WHERE type='table'")])
