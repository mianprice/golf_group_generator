#Golf Group Generator

1. Takes players as input (hard-coded tuples of (name, handicap) currently)
2. Randomly shuffles players into groups of 4 **USED FOR TESTING PURPOSES**
3. Uses swap function to try switching people between groups
  * If swap increases overall variance, the groups stay the same
  * If swap decrease overall variance, the groups switch to the new form tried by the swap function
  * Only performs the swap if the coordinates for the swap meet the following conditions:
    * Coordinates have not been used since the last swap
    * Coordinates would not swap
4. Once the program has tried the swap function unsuccessfully 20 times in a row, the program stops and prints the groups.
