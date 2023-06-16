import mysql

def read_list() -> list:
    """"""
    songs = []
    with open('list.csv', 'r') as f:
        for line in f:
            songs.append(line.strip())
        
    return songs

def search_database() -> str:
    """"""
    return "path_to_file_on_local_server"

## Save all paths in list of lists

def creat_m3u():
    """schreibt eine m3u playliste"""


def main():
    test = read_list()
    print(test)

if __name__ == "__main__":
    main()
  