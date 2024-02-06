from lib.pair_challenge_music_tracking import *
import pytest

def test_calls_empty_list():
    music_tracker = Music_tracker()
    actual = music_tracker.show_song_list()
    expected = []
    assert actual == expected

def test_adds_song_to_list():
    music_tracker = Music_tracker()
    music_tracker.add_song("Stacey's Mom")
    actual = music_tracker.show_song_list()
    expected = ["Stacey's Mom"]
    assert actual == expected

def test_adds_multiple_songs_to_list():
    music_tracker = Music_tracker()
    music_tracker.add_song("Stacey's Mom")
    music_tracker.add_song("American Idiot")
    actual = music_tracker.show_song_list()
    expected = ["Stacey's Mom", "American Idiot"]
    assert actual == expected

def test_throws_error_if_no_song_provided():
    music_tracker = Music_tracker()
    with pytest.raises(Exception) as e:
        music_tracker.add_song() 
    actual = str(e.value)
    
    expected = "Please insert a song!"
    assert actual == expected

def test_throws_error_if_empty_string_provided():
    music_tracker = Music_tracker()
    with pytest.raises(Exception) as e:
        music_tracker.add_song('') 
    actual = str(e.value)
    
    expected = "Please insert a song!"
    assert actual == expected

def test_throws_error_if_wrong_data_type_provided():
    music_tracker = Music_tracker()
    with pytest.raises(Exception) as e:
        music_tracker.add_song(5) 
    actual = str(e.value)
    expected = 'Please insert a string, you fool!'
    assert actual == expected