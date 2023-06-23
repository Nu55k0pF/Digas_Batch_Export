import mysql.connector
from getpass import getpass
import csv

def read_list() -> list:
    """
    Liest eine Liste von Songs aus einer CSV-Datei und gibt sie als Liste zurück.
    :return: Eine Liste von Songs.
    """
    songs = []
    with open('list.csv', 'r') as f:
        for line in f:
            songs.append(line.strip())
        
    return songs


def connect_to_database():
    """"""
    password = getpass("Enter your Password: ")
    # host = input("Host: ")
    
    mydb = mysql.connector.connect(
        host="prodserv4",
        user="david",
        password=password,
        database="digas"
    )
    return mydb


def search_database(title, mydb) -> str:
    """"""
    mycursor = mydb.cursor()

    # Execute the result
    sql = "SELECT TITLE, FILENAME FROM musik_934 WHERE (TITLE LIKE %s);"
    val = ("%" + title + "%", )
    mycursor.execute(sql, val)

    # Fetch the results
    results = mycursor.fetchall()

    # return results
    return results


def make_m3u_entry(list_entry):
    """
    Creates two lines for the m3u playlist. 1. is the title information, 2. line is the file location
    """
    start_line = "#EXTINF:"

    return "{}{}\n{}\n".format(start_line, list_entry[0][0], list_entry[0][1])


def create_m3u(playlist):

    header = "#EXTM3U"

    with open("./playlist.m3u" , "a", encoding="utf-8") as f:
        f.write(header)
        for i in playlist:
            if len(i) == 1:
                f.write(make_m3u_entry(i))
            else:
                pass

def main():

    titles = read_list()

    database = connect_to_database()
    result = []

    for song in titles:
        entry = search_database(song, database)
        result.append(entry)


    with open('ergebnis.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in result:
            writer.writerow(row)
    
    create_m3u(result)
            

if __name__ == "__main__":
    main()
  