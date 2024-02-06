class Music_tracker():
    def __init__(self):
        self.song_list = []

    def show_song_list(self):
        return self.song_list
    
    def add_song(self, song = None):
        if song == None or song == '':
            raise Exception('Please insert a song!')
        if not isinstance(song, str):
            raise TypeError('Please insert a string, you fool!')
        self.song_list.append(song)

