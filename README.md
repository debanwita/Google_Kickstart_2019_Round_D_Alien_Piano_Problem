# Google_Kickstart_2019_Round_D_Alien_Piano_Problem

An alien has just landed on Earth, and really likes our music. Lucky for us.
The alien would like to bring home its favorite human songs, but it only has a very strange instrument to do it with: a piano with just 4 keys of different pitches.
The alien converts a song by writing it down as a series of keys on the alien piano. Obviously, this piano will not be able to convert our songs completely, as our songs tend to have many more than 4 pitches.
The alien will settle for converting our songs with the following rules instead:
•	The first note in our song can be converted to any key on the alien piano.
•	For every note after,
•	if its pitch is higher than the previous note, it should be converted into a higher-pitched key than the previous note's conversion;
•	if lower, it should be converted into a lower-pitched key than the previous note's conversion;
•	if exactly identical, it should be converted into the same key as the previous note's conversion.
Note: two notes with the same pitch do not need to be converted into the same key if they are not adjacent.
What the alien wants to know is: how often will it have to break its rules when converting a particular song?
