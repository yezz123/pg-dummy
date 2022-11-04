import time
import uuid

from psycopg2 import connect, sql

from utils.parser import parseargs

__version__ = "0.0.1"


# Generate current time in epoch milliseconds
current_milli_time = lambda: int(round(time.time() * 1000))

# Generate a random 32 character uuid
gen_uid = lambda: (uuid.uuid4()).hex


def connect_db(database):
    """
    Takes input database and try to connect to it.
    Attempts to connect to the database for 60 seconds
    before giving up.
    Returns a connection and cursor object.
    """
    try:
        connection = connect(
            dbname=database, user=args.user, host=args.hostname, password=args.password
        )
        cursor = connection.cursor()
        print(f"successfully connected to db {database}")
        return connection, cursor
    except Exception as e:
        print(f"error connecting to database {database}: {e}")
        return None


def database(database):
    """
    Takes input database and create it.
    """
    connection, cursor = connect_db("postgres")
    connection.autocommit = True
    try:
        cursor.execute(f"CREATE DATABASE {database}")
        print(f"successfully created db {database}")
    except Exception as e:
        print(f"error creating database {database}: {e}")
    cursor.close()
    connection.close()


def table(database, table):
    """
    Takes input database and table.
    Creates table in database.
    """
    connection, cursor = connect_db(database)
    connection.autocommit = True
    try:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS {} (
                id SERIAL PRIMARY KEY,
                epochmilli bigint,
                uuid uuid,
                uuid2 uuid,
                uuid3 uuid,
                uuid4 uuid,
                uuid5 uuid,
                uuid6 uuid,
                uuid7 uuid,
                uuid8 uuid,
                uuid9 uuid,
                uuid10 uuid);
            """.format(
                table
            )
        )
        print(f"successfully created table {table}")
    except Exception as e:
        print(f"error creating database table {table}: {e}")
    cursor.close()
    connection.close()


def write(database, table):
    """
    Takes input database and table.
    Writes a constant stream of random uuid to data table.
    """
    connection, cursor = connect_db(database)
    connection.autocommit = True
    end_time = time.time() + args.length
    message_number = 0
    while time.time() < end_time:
        current_time = current_milli_time()
        try:
            cursor.execute(
                sql.SQL(
                    """
                    INSERT INTO {} (
                        epochmilli,
                        uuid,
                        uuid2,
                        uuid3,
                        uuid4,
                        uuid5,
                        uuid6,
                        uuid7,
                        uuid8,
                        uuid9,
                        uuid10
                    )
                    VALUES (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    )
                    """
                ).format(sql.Identifier(table)),
                [
                    current_time,
                    gen_uid(),
                    gen_uid(),
                    gen_uid(),
                    gen_uid(),
                    gen_uid(),
                    gen_uid(),
                    gen_uid(),
                    gen_uid(),
                    gen_uid(),
                    gen_uid(),
                ],
            )
        except Exception as e:
            print(f"error inserting into table {table}: {e}")
        message_number += 1
        print(f"{current_time} - committed message #{message_number}")
    cursor.close()
    connection.close()


# Write random dummy data to our target psql db
if __name__ == "__main__":
    args = parseargs()
    database(args.database)
    table(args.database, args.table)
    write(args.database, args.table)
