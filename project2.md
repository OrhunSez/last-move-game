Course Name
Project - 2
Project Issue/Announcement Date
Deadline for Creating Groups
Source Code Submission Date
Late Source Code Submission Date

: Algorithms and Programming
: Last Move Game Simulation
: 03.01.2024 Wednesday, 11:59
: 05.01.2024 Friday, 23:59
: 09.01.2024 Tuesday, 23:59
: 13.01.2024 Saturday, 23:59

GENERAL INFORMATION
Last Move game is a strategy game played with 2 people. The playing field is 7X7 in size and consists
of 49 squares. In the game, each player is represented by a big stone of different colors. There are
also small stones that players jointly use to place on the squares on the playing field. The aim of the
game is to make the opponent player unable to move with the help of stones and boundary lines.

At the beginning of the game, players place their big stones on the square in the middle of the row
closest  to  them. The  player  whose  turn  it  is  first  makes  his/her  move  with  his/her  big  stone,  then
places one of the small stones on an empty square. Big stones can be moved to a neighboring empty
square in  any direction (left, right, forward, backward and diagonally). Small stones can never be
moved from where they are placed. The player who makes the opponent unable to move with the help
of stones and boundary lines wins the game.

For some sample games, see:

?  https://www.youtube.com/watch?v=nPJ17omJFo8 (in Turkish)
?  https://www.youtube.com/watch?v=yJkEqqzt1rM (in Turkish)
?  https://www.youtube.com/watch?v=Tgrhq4fVMs8 (in Turkish)
?  https://www.youtube.com/watch?v=x6U2r89_5J8 (in English)

PROBLEM DEFINITION
A program is requested to be developed that will simulate the Last Move game described above. The
playing field can be 3X3, 5X5 or 7X7 in size. The rows of the playing field must be represented by
counting  numbers  and  the  columns  of  the  playing  field  must  be  represented  by  capital  letters  in
English. In addition, small stones placed on the playing field should be represented by the capital
letter O.

When the program runs, first two different capital letters (except capital letter O) must be taken from
the user to represent the players:

Enter a capital letter to represent player 1 (except O): X
Enter a capital letter to represent player 2 (except O): Y

The game should be able to be played repeatedly, and at the start of each game, the initial playing
field should be displayed after the row/column number of the playing field (3, 5, 7) is taken from the
user. For example, a 3X3 initial playing field can be displayed like the following:

Enter the row/column number of the playing field (3, 5, 7): 3

    A   B   C
  -------------
1 |   | Y |   | 1
  -------------
2 |   |   |   | 2
  -------------
3 |   | X |   | 3
  -------------
    A   B   C

Player X, please enter the direction you want to move your own big stone (N, S,
E, W, NE, NW, SE, SW):

Players must enter the direction they want to move their big stone using the following abbreviations:

?  N: north
?  S: south
?  E: east
?  W: west
?  NE: northeast
?  NW: northwest
?  SE: southeast
?  SW: southwest

After each move, the playing field must be re-displayed. For example, if the user enters  NE in the
example above, the playing field can be displayed like the following:

    A   B   C
  -------------
1 |   | Y |   | 1
  -------------
2 |   |   | X | 2
  -------------
3 |   |   |   | 3
  -------------
    A   B   C

Player X, please enter the location where you want to place a small stone (like
1A):

Players must enter the location where they want to place a small stone with the row number (in the
example [1-3]) and the column letter (in the example [A-C]) of the corresponding location adjacently
(for example 1A).

After each small stone placement, the playing field must be re-displayed. For example, if the user
enters 2B in the example above, the playing field can be displayed like the following:

    A   B   C
  -------------
1 |   | Y |   | 1
  -------------
2 |   | O | X | 2
  -------------
3 |   |   |   | 3
  -------------
    A   B   C

Player Y, please enter the direction you want to move your own big stone (N, S,
E, W, NE, NW, SE, SW):

For example, if the user enters W in the example above, the playing field can be displayed like the
following:

    A   B   C
  -------------
1 | Y |   |   | 1
  -------------
2 |   | O | X | 2
  -------------
3 |   |   |   | 3
  -------------
    A   B   C

Player Y, please enter the location where you want to place a small stone (like
1A):

For example, if the user enters 1C in the example above, the playing field can be displayed like the
following:

    A   B   C
  -------------
1 | Y |   | O | 1
  -------------
2 |   | O | X | 2
  -------------
3 |   |   |   | 3
  -------------
    A   B   C

Player X, please enter the direction you want to move your own big stone (N, S,
E, W, NE, NW, SE, SW):

At the end of the game, which player won the game should be printed on the screen and the user
should be asked if he/she wants to play again:

Player X won the game.
Would you like to play again(Y/N)?:

Notes:

1.  Incorrect  (which  may  cause  a  runtime  error)  or  invalid  (according  to  the  game  rules)  data
entries of the user should be checked and in such cases it should be waited until a correct and
valid data is entered. In addition, the inputs must be taken in the specified order and manner.
2.  The main purpose of this project is to reinforce the use of one/two-dimensional list, dictionary
and string data structures within the topics covered so far. In addition, the program is expected
to be modular (the program should consist of functions) and global variables are not expected
to be used (variables that are not defined/created in a function should not be used inside that
function).

3.  All modules from the standard library of the Python programming language (The Python
Standard Library: https://docs.python.org/3/library/) can be used, but third-party libraries
should not be used.

4.  Test  your program by creating sample inputs and outputs to test different situations before
submitting the project. (You can save time by pasting inputs in batches to the console instead
of entering them one by one.)

5.  The project will be done in groups of two, whoever wants can do it alone. However, those
who take the course again and are not responsible for the weekly practice quizzes (who do not
attend the practice courses) have to do the project alone:

05210000008
05180000032
05180000078
05190000089
05200000850
05210001035
05160000476
05170000089

05200000021
05200000091
05200000109
05200000747
05200000894
05200000914
05200000958
05210000003

05170000111
05170000813
05180000083
05180000933
05180000938
05180000941
05190000088
05190000109

05220000979
05220001014
05220001035
05220001153
05220001232
05220000180
05220000364
05220001140
6.  Those  who  will  do  the  project  as  a  group  of  two  should  enter  the  group  information  they
created on the form at https://forms.gle/fQSzkXJE7eeJ7VcB9 until 05.01.2024 Friday, 23:59.
7.  If you have any questions, please use the forum opened for this assignment on the relevant
course  page  on  the  https://egeders.ege.edu.tr  website.  Also,  follow  the  forum  for  possible
updates and/or clarifications.

05210000949
05210001034
05210001047
05210001048
05210001187
05220000948
05220000952
05220000971

05210000149
05210000221
05210000270
05210000276
05210000286
05210000289
05210000294
05210000934

8.  Start doing your project right away, it is recommended that you design your algorithm (write

pseudocode) before you start coding.

9.  Do the project yourself, especially avoid sharing code with your friends.

POINTS TO BE CONSIDERED:

Submission of Assignment:

?  The source code file (.py extension), with the filename consisting of the combination of the
student  numbers  of  the  group  members  and  the  underscore  character  (for  example,
05090004219_05090004235.py), should be uploaded using the relevant course page on the
https://egeders.ege.edu.tr website by one of the group members.

?  Source code file can be uploaded to the system repeatedly, but it should be noted that only the
most recently uploaded file is stored in the system. In addition, after the  upload process is
completed, check the file and make sure that the file is uploaded to the system without any
problems.

?  A maximum delay of 4 days will be accepted in the delivery of the source code, but a 10%

deduction will be made in the grade.

Evaluation of the Project:

1.  In  the  evaluation  of  the  project;  in  addition  to  the  correct  and  complete  operation  of  the
program, compliance with the structural programming principles (using constants, meaningful
variable/constant  names,  comments,  etc.)  and  compliance  with  modular  programming
principles (to be consisting of functions the program and not using global variables, etc.) will
also be taken into account. Accordingly, the scoring is as follows:

–  Compliance with structured programming principles: 5 points
–  Compliance with modular programming principles: 10 points
–  Correct and complete operation of the program: 85 points

2.  Projects whose source codes are found to be more than a certain amount of similarity will be

deducted at the same rate or these projects will receive zero.


