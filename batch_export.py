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
    sql = "SELECT * FROM musik_934 WHERE (TITLE LIKE %s);"
    val = ("%" + title + "%", )
    mycursor.execute(sql, val)

    # Fetch the results
    results = mycursor.fetchall()

    # return results
    return results

    # # Print the results
    # for result in results:
    #     print(result)
    # return "path_to_file_on_local_server"



## Save all paths in list of lists

def creat_m3u():
    """schreibt eine m3u playliste"""


def main():

    titles = read_list()

    database = connect_to_database()
    result = []

    for song in titles:
        entry = search_database(song, database)
        result.append(entry)

    with open('ergebnis.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(result)
            

if __name__ == "__main__":
    main()
  