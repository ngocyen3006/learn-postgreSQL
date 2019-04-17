from connectPostgresPython import connectDB


def writeData():
    selectQuery = 'SELECT * from PrimeNumber;'

    connect = connectDB()
    conn = connect[0]
    cur = connect[1]

    cur.execute(selectQuery)
    rows = cur.fetchall()

    with open('primeNumber.txt', 'a+') as f:
        for row in rows:
            f.writelines(str(row[1]) + '\n')

    conn.close()
    cur.close()


if __name__ == '__main__':
    writeData()
