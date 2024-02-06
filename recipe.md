# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
#create a list which contains strings of the song titles that are to be tracked




# EXAMPLE

    class Music_tracker():
        def __init__(self):
        pass
    
        # Parameters:
        #   name: none
        # Side effects:
        #   creates a list, which will contain song titles when passed in.

    def add_song(self, song):
        # Parameters:
        #   song: a string representing the song title
        # Returns:
        #   Nothing
        # Side-effects
        #   appending a song to the list
        pass

    def show_song_list(self):
        # Returns:
        #   A list containing the song names
        # Side-effects:
        #   None
        pass
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
initialise the music tracker and returns an empty list.
"""
music_tracker = Music_tracker()
actual = music_tracker.show_song_list()
expected = [] # => an empty list

"""
Tests if songs are added to the list
"""
music_tracker = Music_tracker()
music_tracker.add_song("Stacey's Mom")

actual = music_tracker.show_song_list()
expected = ["Stacey's Mom"] # => returns list with song name in it

"""
Tests if multiple songs are added to the list
"""
music_tracker = Music_tracker()
music_tracker.add_song("Stacey's Mom")
music_tracker.add_song("American Idiot")

actual = music_tracker.show_song_list()
expected = ["Stacey's Mom", "American Idiot"] # => returns list with song name in it


"""
Tests if missing argument is provided
"""
music_tracker = Music_tracker()
actual = music_tracker.add_song() 
expected = "Please insert a song!" # => returns list with song name in it
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
