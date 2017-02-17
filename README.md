#Golf Group Generator

1. Takes input (hard-coded currently)
2. Randomly shuffles input into groups of 4
3. Uses swap function to try switching people between groups
  * If swap increases overall variance, the groups stay the same
  * If swap decrease overall variance, the groups switch to the new form tried by the swap function
4. Once the program has tried the swap function unsuccessfully 20 times in a row, the program stops and prints the groups.
