"""
REMOTE MySQL "STUDENT SQL PAD"

Goal:
- This file connects to a remote MySQL server.
- Students type SQL directly *inside this Python file* (in the SQL variable).
- When they run the file, it executes that SQL and prints results.

No command-line arguments. No interactive console. No menus.

---------------------------------------------
1) INSTALL (one time)
---------------------------------------------
pip install mysql-connector-python

---------------------------------------------
2) CONNECTION SETTINGS
---------------------------------------------
Put your real host/user/password in the CONFIG section below.
(Teacher tip: give students a limited-permissions account.)

---------------------------------------------
3) HOW STUDENTS USE IT
---------------------------------------------
Students edit ONLY the SQL string, then run:

python student_sql_pad.py

Examples they can try:
- SHOW TABLES;
- DESCRIBE contacts;
- SELECT * FROM contacts;
- SELECT first_name, last_name FROM contacts WHERE last_name = 'Smith';
- INSERT INTO contacts (first_name, last_name, email) VALUES ('Ada','Lovelace','ada@example.com');

Important:
- End your SQL with a semicolon is fine, but not required by the connector.
"""

# ============================================================
# IMPORTS
# ============================================================

# We use mysql.connector to talk to MySQL over the network.
# It handles: TCP connection, authentication, sending SQL, receiving results.
import mysql.connector

# We import the MySQL error type so we can catch and print clean messages.
from mysql.connector import Error as MySQLError


# ============================================================
# CONFIG: TEACHER SETS THIS ONCE
# ============================================================

# These values tell Python how to reach the remote database server.
# MySQL default port is 3306.
#
# DO NOT publish real credentials in a public repo.
# If you share this file with students, consider using a low-privilege account.
DB_CONFIG = {
    "host": "YOUR_HOST_HERE",        # example: "db.school.edu" or "123.45.67.89"
    "port": 3306,                    # usually 3306
    "user": "YOUR_USERNAME_HERE",    # example: "student_user"
    "password": "YOUR_PASSWORD_HERE",
    "database": "YOUR_DB_NAME_HERE", # example: "school_contacts"
    "connection_timeout": 10,        # seconds
    "charset": "utf8mb4",            # good default for modern text
}

# If your MySQL server requires SSL/TLS, you may need to add settings like:
# DB_CONFIG["ssl_ca"] = "/path/to/ca.pem"
# DB_CONFIG["ssl_cert"] = "/path/to/client-cert.pem"
# DB_CONFIG["ssl_key"] = "/path/to/client-key.pem"


# ============================================================
# STUDENT WORK AREA: CHANGE THIS SQL ONLY
# ============================================================

# Students: type ONE SQL statement here.
# Keep it simple at first:
#   SHOW TABLES
#   DESCRIBE contacts
#   SELECT * FROM contacts
#   SELECT first_name, last_name FROM contacts WHERE last_name='Smith'
#
# You can include a trailing semicolon, but it is optional.
SQL = """
SELECT * FROM contacts;
"""


# ============================================================
# HELPER: PRINT RESULTS AS A SIMPLE TABLE
# ============================================================

def print_table(column_names: list[str], rows: list[tuple], max_rows: int = 200) -> None:
    """
    Print rows in a readable ASCII table.

    Why we do this:
    - Raw Python prints (like printing a list of tuples) are hard to read.
    - This gives students a clear "grid" view of results.

    max_rows prevents huge queries from flooding the screen.
    """
    # If there are no rows, show that clearly.
    if not rows:
        print("(0 rows)")
        return

    # Limit displayed rows.
    display_rows = rows[:max_rows]
    truncated = len(rows) > max_rows

    # Convert everything to strings for printing.
    col_strs = [str(c) for c in column_names]
    row_strs = [[("" if v is None else str(v)) for v in row] for row in display_rows]

    # Compute widths for each column so it lines up nicely.
    widths: list[int] = []
    for i, col_name in enumerate(col_strs):
        max_cell_width = max(len(r[i]) for r in row_strs)
        widths.append(max(len(col_name), max_cell_width))

    # Build separator lines like +-----+--------+
    sep = "+" + "+".join("-" * (w + 2) for w in widths) + "+"

    # Header line
    header = "|" + "|".join(f" {col_strs[i].ljust(widths[i])} " for i in range(len(widths))) + "|"

    print(sep)
    print(header)
    print(sep)

    # Data rows
    for r in row_strs:
        line = "|" + "|".join(f" {r[i].ljust(widths[i])} " for i in range(len(widths))) + "|"
        print(line)

    print(sep)
    print(f"({len(rows)} rows{' shown (truncated)' if truncated else ''})")


# ============================================================
# MAIN PROGRAM
# ============================================================

def main() -> None:
    """
    Steps:
    1) Connect to the remote MySQL server using DB_CONFIG.
    2) Create a cursor (the object used to send SQL).
    3) Execute the student's SQL.
    4) If the SQL returned rows (like SELECT), fetch them and print them.
    5) If the SQL changed data (INSERT/UPDATE/DELETE), commit it.
    6) Close everything cleanly.
    """

    # ----------------------------
    # 1) Connect to MySQL
    # ----------------------------
    # This opens a network connection to the remote server.
    # If the host/port are wrong, or credentials fail, this will throw an error.
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
    except MySQLError as e:
        print("Connection failed.")
        print("Most common causes:")
        print("- Wrong host/port")
        print("- Wrong username/password")
        print("- Your IP is not allowed by the server firewall")
        print("- Database name is wrong")
        print("\nMySQL error message:")
        print(e)
        return  # stop the program

    # If we got here, the connection worked.
    print("Connected to MySQL.")
    print(f"Host: {DB_CONFIG['host']}  Database: {DB_CONFIG['database']}")
    print()

    # We disable autocommit so we can choose when to commit changes.
    # For SELECT queries, we won't commit anything.
    conn.autocommit = False

    # ----------------------------
    # 2) Create cursor
    # ----------------------------
    # A cursor is how we execute SQL.
    # Think: "cursor = the remote database conversation handle".
    cur = conn.cursor()

    try:
        # ----------------------------
        # 3) Execute student SQL
        # ----------------------------
        # This sends the SQL string to the server.
        cur.execute(SQL)

        # ----------------------------
        # 4) Did we get a result set?
        # ----------------------------
        # For queries like SELECT, cur.description is not None and we can fetch rows.
        # For commands like INSERT/UPDATE/DELETE/CREATE, cur.description is None.
        if cur.description is not None:
            # Get the column names from the metadata.
            column_names = [col[0] for col in cur.description]

            # Get all rows returned by the query.
            rows = cur.fetchall()

            # Print results.
            print_table(column_names, rows)

            # No commit needed (SELECT doesn't change data).
            # Still, we can rollback to clear any transaction state.
            conn.rollback()
        else:
            # ----------------------------
            # 5) No rows returned => data/schema change
            # ----------------------------
            # Example statements:
            # - INSERT
            # - UPDATE
            # - DELETE
            # - CREATE TABLE
            # - DROP TABLE (hopefully not)
            #
            # These should be committed so the change is saved.
            affected = cur.rowcount
            conn.commit()
            print(f"Statement executed. Rows affected: {affected}")

    except MySQLError as e:
        # Any SQL error should rollback changes.
        conn.rollback()
        print("SQL error. Any changes were rolled back.")
        print("Error message:")
        print(e)

    finally:
        # ----------------------------
        # 6) Clean up
        # ----------------------------
        # Always close cursor and connection, even if there was an error.
        cur.close()
        conn.close()
        print()
        print("Connection closed.")


# Standard Python entry point:
if __name__ == "__main__":
    main()
