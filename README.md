# Predicting results in Chess.com [Fantasty Pro Chess League](https://www.prochessleague.com)

* Model for converting Elo ratings (difference) to win/draw/loss probabilities ported from [Elo Win Probability Calculator](https://wismuth.com/elo/calculator.html).
* Some parameter fitting was done after Week 6 under the hypothesis that fewer games are drawn in the rapid format (15|2 or 10|2) than for standard games.

## Results

| Event | Date | Score | Rank w/o tiebreaker (sparse) | Rank  w/o tiebreaker (dense) | Tiebreaker score | Rank w tiebreaker (sparse) | Rank w tiebreaker (dense) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Super Saturday & Sunday](https://docs.google.com/spreadsheets/d/1Bvog5hvciu0LZ5GWynen5BkcDxGbWGAi9OKc2uWVPxY/edit?usp=sharing) | 2014-02-03, 04 | 82 | 65 | 12| 0 (10) | 90 | 17 |
| [Week 5](https://docs.google.com/spreadsheets/d/1yg6XxR8njJTn0inAOj7W2EGnBp4Evz825AnCYEgjopw/edit?usp=sharing) | 2018-02-07 | 37 | 104 | 14 | N/A | | |
| [Week 6](https://docs.google.com/spreadsheets/d/1TLvSmHH1Yi1JHlfDUm78dZC0RbWyP3kh01_bhMwnNco/edit?usp=sharing) | 2018-02-14 | 42.5 | 10 | 6 | N/A | | |
| [Super Saturday #2](https://docs.google.com/spreadsheets/d/1NBxVVyPB5MOlXoKtdOlKfb4Vb0Z-ExiY9_hgdEe4TmM/edit?usp=sharing) | 2018-02-24 | 90.5 | 21 | 9 | 0 (10) | 41 | 16 |
