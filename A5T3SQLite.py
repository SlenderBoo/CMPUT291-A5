import sqlite3

def connect(dbase):

    #connect to database
    conn = sqlite3.connect('./' + dbase)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("DROP INDEX IF EXISTS idxNeedsPart;")  # drop the index we have before

#run the sql line
    print("Opening " + dbase)
    T3(cursor)
    print("Closing " + dbase)
    conn.close()

    return

def T3(c):
    #sql code
    sql = "SELECT COUNT(id),host_name,host_id FROM listings GROUP BY host_id LIMIT 10"
    c.execute(sql)
    #print out the result
    result = c.fetchall()
    for i in result:
        print(i[0]," ",i[1]," ",i[2])

def main():

    print("Executing Task 3")
    connect("A5.db")

    return

if __name__ == "__main__":
    main()
