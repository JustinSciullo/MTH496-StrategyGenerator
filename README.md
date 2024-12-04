# MTH496-StrategyGenerator
This code was written with the intention to search for winning guessing games, studied in MTH 496 Senior Thesis taken at Grand Valley State University with Dr. David Clark.

## Background
In an offline guessing game, there is a player called the Questioner and a player called the Responder. The Responder first picks two distinct numbers from the set $`\{1, 2, 3, \dots, n\}`$. The Questioner then creates a set of questions of the form “How many of your numbers are in the set $`q_i \subseteq \{1, 2, 3, \dots, n\}`$?” and sends them to the Responder who answers them. The Questioner wins if they can guess the Responder’s numbers no matter which numbers the Responder chose. The Responder wins otherwise.

For some $n$ and $l$, we say that the least number of questions needed for the questioner to be able to win is the optimal strategy. We are interested in finding strategies that are winning for the Questioner because they give an upper bound to the optimal strategy given some $n$ andd $l$.

## Code
