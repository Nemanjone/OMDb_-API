
## -OMDb_-API_analyzer-

### Description

Python program that enables users to get information about movies from OMDb API and filter these movies based on input parameters. The output is a file with all available movies data and database that stores already downloaded info.

### Pre-requisites

1.  Install Python ([https://www.python.org](https://www.python.org/))

### To Run program

Clone the repository into a folder directly from your IDE or download file, unzip and import into IDE. Program can be run from command line. Following parameters are supported:

-   **-t**  movie titles (required; multiple titles are supported)
-   **-r**  imdb rating (optional; filters out movies with imdbRating value lower than specified in the command line argument)
-   **-g**  genre (optional; used to filter movies by Genre field value)
=======
Python program that enables users to get information about movies from OMDb API
and filter these movies based on input parameters. The output is a file with all available movies data and database that stores already downloaded info.

### Pre-requisites

1. Install Python (https://www.python.org)  

### To Run program
Clone the repository into a folder directly from your IDE or download file, unzip and import into IDE.
Program can be run from command line. Following parameters are supported:

 - **-t** movie titles (required; multiple titles are supported) 
 - **-r** imdb rating (optional; filters out movies with imdbRating value lower than specified in the command line argument) 
 - **-g** genre (optional; used to filter movies by Genre field value)
 
 Examples: 
 - python main.py -t ' Armagedon' 
 - python main.py -t ' Armagedon' 'Matrix' 
 - python main.py -t ' Armagedon' 'Matrix' -g 'Drama'
 - python main.py -t ' Armagedon' 'Matrix' -r '1.0'
 - python main.py  -t 'fdsfsdfsdfsdf' -r 1.0

Examples:

-   python main.py -t ' Armagedon'
-   python main.py -t ' Armagedon' 'Matrix'
-   python main.py -t ' Armagedon' 'Matrix' -g 'Drama'
-   python main.py -t ' Armagedon' 'Matrix' -r '1.0'
-   python main.py -t 'fdsfsdfsdfsdf' -r 1.0

### Contact

Created by  [nemanja.balaban@gecko.rs](mailto:nemanja.balaban@gecko.rs)  - feel free to contact me.
