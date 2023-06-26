"""
Digas Batch Export to m3u 0.9.1

This is a little program to search for multiple entries in a digas SQL databes. The results of the querys get written to an m3u file to import into an
audio player or a DAW that can read m3us such as Magix Sequoia

Author: Johannes Schnurrenberger 
Last Change 23.06.2023

TO DO: Add error handling
"""

import mysql.connector
from getpass import getpass


def read_list() -> list:
    """
    Reads a list of songs from a CSV file and returns it as a list.

    Returns:
    --------
    list : A list of songs.
    """

    songs = []

    # Read the file with the titles
    with open('list.csv', 'r') as f:
        for line in f:
            songs.append(line.strip())
        
    return songs


def connect_to_database() -> mysql.connector:
    """
    Connects to the database using the provided password and returns the connection object.

    Returns:
    mydb (mysql.connector.connection_cext.CMySQLConnection): A connection object to the database.
    """

    # Ask the user for a password securly
    password = getpass("Enter your Password: ")
    
    # Get a connection to the db
    mydb = mysql.connector.connect(
        host="prodserv4",
        user="david",
        password=password,
        database="digas"
    )

    return mydb


def search_database(title, mydb) -> tuple:
    """
    This function searches for a title in the musik_934 database and returns the title and filename of all matching records.

    Args:
        title (str): A string representing the title to search for.
        mydb (mysql.connector.connection_cext.CMySQLConnection): A connection object representing the database.

    Returns:
        tuple: A tuple containing the title and filename of all matching records.
    """

    mycursor = mydb.cursor()

    # Execute the result
    sql = "SELECT TITLE, FILENAME FROM musik_934 WHERE (TITLE LIKE %s);"
    val = ("%" + title + "%", )
    mycursor.execute(sql, val)

    # Fetch the results
    results = mycursor.fetchall()

    # return results
    return results


def search_db_with_ID(musicid, mydb) -> tuple:
    ## TODO: Fishish implementations
    # Search funktion if MusicID is provided
    sql = "SELECT REFNR from Musik_934 where (Musicid like %s);"
    val = [musicid]
    mycursor.execute(sql, val)
    results1 = mycursor.fetchall()
    info.append(results1[0][0])

    sql = "SELECT musik_934.filename, musik_934_t.performer FROM Musik_934 INNER JOIN musik_934_t WHERE (REFNR like %s);"
    mycursor.execute(sql, results1[0][0])
    results2 = mycursor.fetchall()


def make_m3u_entry(list_entry) -> str:
    """
    Creates two lines for the m3u playlist. The first line is the title information and the second line is the file location.

    Args:
        list_entry (list): A list containing two elements: title information and file location.

    Returns:
        str: A string containing two lines for the m3u playlist.
    """
    
    start_line = "#EXTINF:"

    return "{}{}\n{}\n".format(start_line, list_entry[0][0], list_entry[0][1])


def create_m3u(playlist) -> None:
    """
    This function creates an m3u playlist file from a list of entries. If there are multiple entries in one line
    the program will promt a warning and skip this line.

    Args:
        playlist (list): A list of entries to include in the m3u playlist.

    Returns:
        None
    """

    header = "#EXTM3U"

    with open("./playlist.m3u" , "a", encoding="utf-8") as f:
        f.write(header)
        for i in playlist:
            if len(i) == 1:
                f.write(make_m3u_entry(i))
            else:
                print("WARNING: Multiple entrys detected. Scipping")
                pass


def main():
    """
    This function reads a list of song titles from a file, searches for each song in a database,
    and creates an m3u playlist file from the search results.
    """

    # Read list of song titles from file
    titles = read_list()

    # Connect to database
    database = connect_to_database()

    # Search for each song in database and append result to list
    result = []
    for song in titles:
        entry = search_database(song, database)
        result.append(entry)

    # Create m3u playlist file from search results
    create_m3u(result)


if __name__ == "__main__":
    main()
  