import csv
import sqlite3



def create_db1(db_name):
    conn = sqlite3.connect('./' + db_name)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    sql = 'DROP TABLE IF EXISTS listings;'
    c.execute(sql)
    conn.commit()
    sql = '''CREATE TABLE listings (
id INTEGER, 
name TEXT, 
host_id INTEGER, 
host_name TEXT, 
neighbourhood TEXT,
room_type TEXT,
price INTEGER,
minimum_nights INTEGER,
availability_365 INTEGER,
PRIMARY KEY(id)
);'''
    c.execute(sql)
    conn.commit()



    filename = 'YVR_Airbnb_listings_summary.csv'


    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            c.execute('INSERT INTO listings VALUES(?,?,?,?,?,?,?,?,?)',
                      (int(line[0]), line[1], int(line[2]), line[3], line[4], line[5], int(line[6]), int(line[7]),
                       int(line[8])))
            conn.commit()


    conn.close()


def create_db2(db_name):
    conn = sqlite3.connect('./' + db_name)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    sql = 'DROP TABLE IF EXISTS reviews;'
    c.execute(sql)
    conn.commit()
    sql = '''CREATE TABLE reviews (
listing_id INTEGER,
id INTEGER, 
date TEXT, 
reviewer_id INTEGER, 
reviewer_name TEXT,
comments TEXT, 
PRIMARY KEY(id)
);'''
    c.execute(sql)
    conn.commit()



    filename = 'YVR_Airbnb_reviews.csv'

    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            c.execute('INSERT INTO reviews VALUES(?,?,?,?,?,?)',
                      (int(line[0]), int(line[1]), line[2], int(line[3]), line[4],line[5]))
            conn.commit()




    conn.close()




def main():


    db_name = "A5.db"
    create_db1(db_name)
    print("Finish1")
    create_db2(db_name)
    print("Finish2.")


main()
