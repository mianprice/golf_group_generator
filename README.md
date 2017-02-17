#Golf Group Generator

1. Initial Setup
  * Create random list of golfers with handicaps (1-20) for each
  * Create groups (3 or 4 people each) based on potential combinations total number of golfers
  * Create team handicap for each groups
  * Create list of groups including team handicaps

2. Shuffle groups until minimum team handicap difference is found
  * Track team handicap variance
  * Generate all group combinations and only output list of groups with smallest team handicap variance

3. Extras
  1. Check shuffler efficiency
    * Can shuffler function be made more efficient?
    * Can minimum variance be determined from initial set of handicaps?
  2. Take input
    * (Command Line, .txt file, or other data formats)
  3. Output options
    * Output minimum variance list of groups
    * Iff multiple possible lists of groups with the same minimum variance, output all options
