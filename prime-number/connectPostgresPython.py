# !/usr/bin/python
import psycopg2

hostname = 'localhost'
username = 'yen'
password = ' '
database = 'prime'


def isPrime(n):
    '''
    Don't test type(n) or n == 2 or n == 3. Because insertData() function is import it.
    '''

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def connectDB():
    try:
        conn = psycopg2.connect(host=hostname, database=database, user=username, password=password)

        cur = conn.cursor()

        return [conn, cur]

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def createPrimeTable():
    command = ('CREATE TABLE PrimeNumber (id SERIAL PRIMARY KEY, prime int);')

    connect = connectDB()
    conn = connect[0]
    cur = connect[1]

    cur.execute(command)

    conn.commit()
    conn.close()
    cur.close()


def readLastData():
    selectQuery = 'SELECT * from PrimeNumber order by id desc;'

    connect = connectDB()
    conn = connect[0]
    cur = connect[1]

    cur.execute(selectQuery)
    rows = cur.fetchone()
    if rows == None:
        id = 0
        lastPrimeNumber = 0
    else:
        id = rows[0]
        lastPrimeNumber = rows[1]

    conn.close()
    cur.close()
    return [id, lastPrimeNumber]


def insertData():
    insertQuery = 'INSERT INTO PrimeNumber (prime) VALUES (%s);'
    lastData = readLastData()
    lastPrime = lastData[1]
    id = lastData[0]

    connect = connectDB()
    conn = connect[0]
    cur = connect[1]
    if id < 1000000:
        if lastPrime < 3:
            if lastPrime == 0:
                cur.executemany(insertQuery, [(2,), (3,)])
                conn.commit()
            else:
                cur.execute(insertQuery, (3,))
                conn.commit()

            lastPrime = 3

        for val in range(lastPrime + 2, 15485863 + 1, 2):
            if isPrime(val):
                cur.execute(insertQuery, (val,))
                conn.commit()

            else:
                continue

    conn.close()
    cur.close()


if __name__ == '__main__':
    # createPrimeTable()
    print(readLastData())
    insertData()
    print(readLastData())
