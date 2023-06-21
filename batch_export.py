import mysql.connector
from getpass import getpass

def read_list() -> list:
    """"""
    songs = []
    with open('list.csv', 'r') as f:
        for line in f:
            songs.append(line.strip())
        
    return songs

def search_database(title) -> str:
    """"""
    # Connect to the database
    # host = input("Host: ")
    # user = input("User: ")
    password = getpass("Enter your Password: ")
    # host = input("Host: ")
    
    mydb = mysql.connector.connect(
        host="prodserv4",
        user="digas",
        password=password,
        database="digas"
    )

    # Create a cursor object
    mycursor = mydb.cursor()

    # Execute the query
    sql = "SELECT * FROM musik_934_t and musik_934 WHERE (TITLE LIKE '%s');"
    val = ("%" + title + "%", )
    mycursor.execute(sql, val)

    # Fetch the results
    results = mycursor.fetchall()

    # return results

    # Print the results
    for result in results:
        print(result)
    return "path_to_file_on_local_server"



## Save all paths in list of lists

def creat_m3u():
    """schreibt eine m3u playliste"""


def main():
    test = read_list()
    for song in test:
        search_database(song)

if __name__ == "__main__":
    main()
  