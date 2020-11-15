def forward(cursor):
    # Remove column 'power_to_write' from rooms
    cursor.execute("""
        CREATE TABLE rooms_backup (
            id INTEGER PRIMARY KEY,
            name text,
            alias text,
            room_id text null,
            title text default '',
            icon text default '',
            encrypted integer,
            public integer,
            type text default ''
        )
    """)
    cursor.execute("""
        INSERT INTO rooms_backup SELECT id, name, alias, room_id, title, icon, encrypted, public, type 
            FROM rooms
    """)
    cursor.execute("""
        DROP TABLE rooms
    """)
    cursor.execute("""
        CREATE TABLE rooms (
            id INTEGER PRIMARY KEY autoincrement,
            name text,
            alias text constraint room_alias_unique_idx unique,
            room_id text null constraint room_room_id_unique_idx unique,
            title text default '',
            icon text default '',
            encrypted integer,
            public integer,
            type text default ''
        )
    """)
    cursor.execute("""
        INSERT INTO rooms SELECT id, name, alias, room_id, title, icon, encrypted, public, type 
            FROM rooms_backup
    """)
    cursor.execute("""
        DROP TABLE rooms_backup
    """)
