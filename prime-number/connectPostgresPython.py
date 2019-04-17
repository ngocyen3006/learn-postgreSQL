# !/usr/bin/python
import psycopg2
from math import sqrt, floor

hostname = 'localhost'
username = 'yen'
password = ' '
database = 'prime'


def isPrime(n):
    if type(n).__name__ != 'int':
        return False

    if n < 2:
        return False

    if n == 2 or n == 3:
        return True

    upper_bound = floor(sqrt(n))
    for i in range(2, upper_bound + 1):
        if n % i == 0:
            return False

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
    selectQuery = 'SELECT * from PrimeNumber;'

    connect = connectDB()
    conn = connect[0]
    cur = connect[1]

    cur.execute(selectQuery)
    rows = cur.fetchall()
    if rows == []:
        id = 0
        lastPrimeNumber = 0
    else:
        id = rows[-1][0]
        lastPrimeNumber = rows[-1][1]

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
        for val in range(lastPrime + 1, 15485863 + 1):
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
    # insertData()
    print(readLastData())
