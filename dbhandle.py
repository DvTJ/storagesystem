import mysql.connector


def connect():
    # given the values for log in to the DB
    # todo: set into a config.conf for security reasons. prio: medium

    dbconn = mysql.connector.connect(
        host="172.20.10.2",
        user="st-user",
        password="mypassword",
        database="storagesystem"
    )
    return dbconn


def requestInvNr():
    invNr = 0
    # open a connection to the DB
    dbcon = connect()

    # use the connection to ask for the last inventory Number
    cursor = dbcon.cursor()
    query = "SELECT InvNr FROM Inventory ORDER BY InvNr DESC LIMIT 1;"
    cursor.execute(query)

    # get the result and filter the number we need out, so we can parse it to an int
    c_res = cursor.fetchall()
    try:
        # the tupel given as a result gets parsed into a string
        res = str(c_res)

        # the newly parsed string is now checked for numbers, which then are added to a new string, which only consists of the given numbers.
        # That way we can work with the index.
        # If a error accours, there is no entry in the table and the index is 1.

        k = ''
        for ch in res:
            if ch.isnumeric():
                k += ch
                invNr = int(k)
    except:
        # only gets triggered if an error is returned
        invNr = 1

    # close the connection
    dbcon.close()

    return invNr


def addNewItem(name, desc, location, quantity):
    # open the DB-connection
    dbcon = connect()

    # get the cursor on the DB
    cursor = dbcon.cursor()

    # build the query
    query = "INSERT INTO Inventory (Name,Description,Location,Quantity,LastUpdated) VALUES (%s, %s, %s, %s, NOW());"
    val = (name, desc, location, quantity)

    # for debugging: print the query, checking for false build query
    print(query)

    # push it into the DB & write it to the table
    cursor.execute(query, val)
    dbcon.commit()

    # close the connection
    dbcon.close()
