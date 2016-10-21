# The Birthday Problem

> 100 prisoners are assigned the numbers 0-99 respectively. Then, those numbers are written on cards, which are put into 100 boxes. Each prisoner can only search 50 out of the 100 boxes. What strategy gives you the highest possibility that all 100 prisoners find their number on a card?

- Julian Samek

[Wikipedia page](https://en.wikipedia.org/wiki/100_prisoners_problem)

@juliansamek and I had a friendly competition to see who could code a simulation for this the fastest. Hats off to him!

## Strategy

I'ma just quote the Wikipedia article:

> Surprisingly, there is a strategy that provides a survival probability of more than 30%. The key to success is that the prisoners do not have to decide beforehand which drawers to open. Each prisoner can use the information gained from the contents of previously opened drawers to help decide which drawer to open next. Another important observation is that this way the success of one prisoner is not independent of the success of the other prisoners.

> To describe the strategy, not only the prisoners, but also the drawers are numbered from 1 to 100, for example row by row starting with the top left drawer. The strategy is now as follows.

> Each prisoner first opens the drawer with his own number.
If this drawer contains his number he is done and was successful.
Otherwise, the drawer contains the number of another prisoner and he next opens the drawer with this number.
The prisoner repeats steps 2 and 3 until he finds his own number or has opened 50 drawers.
This approach ensures that every time a prisoner opens a drawer, he either finds his own number or the number of another prisoner he has not yet encountered.

## Technical

Run the strategy simply with `python permutation-map.py`, and run the "random choice" with `python random-choice.py` You'll need Python, of course

The script takes in three parameters (declared as variables at the top of the script):
* `iterations`, or how many rooms you want to generate
* `boxes`, or how many boxes/cards/prisoners there are

The script will then generate `iterations` iterations, analyze the data, and output it to your terminal (stdout) for you to see!
