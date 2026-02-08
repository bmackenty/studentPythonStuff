"""
sqlite_contacts_sandbox.py
Mr. MacKenty-style “SQL sandbox” for students.

BIG IDEA
A database is just a file + a query engine. SQLite stores the whole database in ONE file,
and Python’s sqlite3 module lets students send raw SQL to that file.

WHAT THIS PROGRAM DOES
- Creates (or opens) a SQLite database file: contacts.db
- Ensures a simple contacts table exists
- Gives a CLI loop where students can type SQL directly
- Prints results for SELECT queries
- Shows row counts for INSERT/UPDATE/DELETE
- Supports a few convenience commands like .help, .schema, .tables, .seed, .quit

NO COMMAND-LINE ARGUMENTS
Just run:
    python sqlite_contacts_sandbox.py

STUDENT RULES OF THE GAME
- End SQL with a semicolon ;   (recommended, not strictly required)
- Use SELECT to read; INSERT/UPDATE/DELETE to change.
- If you break something, you can delete contacts.db and rerun.

NOTE FOR TEACHERS
This is intentionally “low ceremony”: students see SQL as the primary interface.
"""

from __future__ import annotations

import sqlite3
import textwrap
from typing import Optional, Iterable, Sequence


DB_FILE = "contacts.db"


def connect(db_file: str) -> sqlite3.Connection:
    """
    Open a connection to the SQLite database file.

    Important details:
    - SQLite creates the database file if it does not already exist.
    - row_factory lets us access columns by name (nice for printing).
    """
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_schema(conn: sqlite3.Connection) -> None:
    """
    Create the contacts table if it does not exist.

    Schema choices kept simple for beginners:
    - id: INTEGER PRIMARY KEY => SQLite will auto-generate unique ids.
    - name/email/phone: TEXT (SQLite is flexible, but we keep it consistent).
    - created_at: timestamp default for visibility.
    """
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id         INTEGER PRIMARY KEY,
            name       TEXT NOT NULL,
            email      TEXT,
            phone      TEXT,
            created_at TEXT NOT NULL DEFAULT (datetime('now'))
        );
        """
    )
    conn.commit()


def print_banner() -> None:
    print("\nSQLite Contacts SQL Sandbox")
    print("=" * 32)
    print(f"Database file: {DB_FILE}")
    print("Type SQL and press Enter. Use .help for commands.\n")


def print_help() -> None:
    help_text = """
    Commands (start with a dot):
      .help        Show this help
      .tables      List tables
      .schema      Show CREATE TABLE for contacts
      .seed        Insert a few sample contacts (safe to run multiple times)
      .quit        Exit (also: .exit)

    SQL Examples:
      SELECT * FROM contacts;
      SELECT id, name FROM contacts WHERE name LIKE '%Ann%';
      INSERT INTO contacts (name, email, phone) VALUES ('Ada Lovelace', 'ada@ib.edu', '+44 20 1234 5678');
      UPDATE contacts SET phone = '+48 500 000 001' WHERE id = 1;
      DELETE FROM contacts WHERE id = 3;

    Notes:
    - SQLite uses single quotes for strings: 'text'
    - If you get stuck, try: SELECT * FROM contacts;
    """
    print(textwrap.dedent(help_text).strip())


def list_tables(conn: sqlite3.Connection) -> None:
    """
    Query SQLite's catalog table (sqlite_master) to list user tables.
    """
    rows = conn.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        ORDER BY name;
        """
    ).fetchall()

    if not rows:
        print("(no tables)")
        return

    print("Tables:")
    for r in rows:
        print(f"  - {r['name']}")


def show_contacts_schema(conn: sqlite3.Connection) -> None:
    """
    Show the CREATE statement for the contacts table.
    """
    row = conn.execute(
        """
        SELECT sql
        FROM sqlite_master
        WHERE type='table' AND name='contacts';
        """
    ).fetchone()

    if row is None or row["sql"] is None:
        print("contacts table not found.")
        return

    print(row["sql"])


def seed_data(conn: sqlite3.Connection) -> None:
    """
    Insert a few sample contacts.

    We try to avoid duplicates by checking for name+email pairs first.
    This keeps the demo friendly when students run .seed more than once.
    """
    samples = [
        ("Grace Hopper", "grace@navy.mil", "555-0101"),
        ("Alan Turing", "alan@bletchley.uk", "555-0102"),
        ("Katherine Johnson", "katherine@nasa.gov", "555-0103"),
    ]

    # Ensure a uniqueness rule (optional) would complicate schema;
    # instead, do a simple existence check in code.
    inserted = 0
    for name, email, phone in samples:
        exists = conn.execute(
            "SELECT 1 FROM contacts WHERE name = ? AND email = ? LIMIT 1;",
            (name, email),
        ).fetchone()

        if exists:
            continue

        conn.execute(
            "INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?);",
            (name, email, phone),
        )
        inserted += 1

    conn.commit()
    print(f"Seed complete. Inserted {inserted} new contact(s).")


def is_select_statement(sql: str) -> bool:
    """
    A tiny heuristic: if the trimmed SQL starts with 'select' (case-insensitive),
    treat it as a query that returns rows.

    This is not a full SQL parser; it’s good enough for classroom usage.
    """
    return sql.lstrip().lower().startswith("select")


def print_rows(rows: Sequence[sqlite3.Row]) -> None:
    """
    Pretty-print rows in a simple table-like output.

    Approach:
    - Determine columns from the first row.
    - Compute column widths.
    - Print header + divider + data.
    """
    if not rows:
        print("(0 rows)")
        return

    columns = rows[0].keys()

    # Convert everything to strings for width calculation and printing.
    str_rows: list[list[str]] = []
    for r in rows:
        str_rows.append([("" if r[c] is None else str(r[c])) for c in columns])

    widths = []
    for i, col in enumerate(columns):
        max_data_width = max(len(row[i]) for row in str_rows)
        widths.append(max(len(col), max_data_width))

    # Header
    header = " | ".join(col.ljust(widths[i]) for i, col in enumerate(columns))
    divider = "-+-".join("-" * widths[i] for i in range(len(widths)))
    print(header)
    print(divider)

    # Data
    for row in str_rows:
        print(" | ".join(row[i].ljust(widths[i]) for i in range(len(widths))))

    print(f"({len(rows)} row(s))")


def execute_user_sql(conn: sqlite3.Connection, sql: str) -> None:
    """
    Execute whatever SQL the student typed.

    Behavior:
    - SELECT: fetch and print results
    - Other statements: execute and show affected row count, then commit
    - Errors: print the exception message without crashing the program
    """
    try:
        # Use cursor so we can access rowcount and fetch results.
        cur = conn.cursor()

        if is_select_statement(sql):
            cur.execute(sql)
            rows = cur.fetchall()
            print_rows(rows)
        else:
            cur.execute(sql)
            conn.commit()
            # rowcount is meaningful for UPDATE/DELETE; for INSERT it’s often 1.
            print(f"OK. Rows affected: {cur.rowcount}")

    except sqlite3.Error as e:
        # sqlite3.Error catches syntax errors, missing tables/columns, constraints, etc.
        print(f"SQLite error: {e}")


def repl(conn: sqlite3.Connection) -> None:
    """
    Read-Eval-Print Loop (REPL) for SQL.

    Students type:
      - dot-commands (.help, .tables, etc.), OR
      - raw SQL

    We keep it one-line-per-command to stay simple.
    (Multi-line SQL can be added later if needed.)
    """
    while True:
        try:
            user_input = input("sql> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            return

        if not user_input:
            continue

        # Dot-commands (our own mini “shell” commands)
        if user_input.startswith("."):
            cmd = user_input.lower()

            if cmd in {".quit", ".exit"}:
                print("Bye.")
                return
            if cmd == ".help":
                print_help()
                continue
            if cmd == ".tables":
                list_tables(conn)
                continue
            if cmd == ".schema":
                show_contacts_schema(conn)
                continue
            if cmd == ".seed":
                seed_data(conn)
                continue

            print("Unknown command. Use .help")
            continue

        # Otherwise, treat as SQL.
        execute_user_sql(conn, user_input)


def main() -> None:
    conn = connect(DB_FILE)
    try:
        initialize_schema(conn)
        print_banner()
        repl(conn)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
