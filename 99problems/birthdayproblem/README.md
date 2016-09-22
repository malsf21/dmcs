# The Birthday Problem

> How many people do you need to have in a room for there to be a 50% chance that two people share the same birthday. How many people do you need for a 99% chance?

- Matthew Wang (me)

[Wikipedia page](https://en.wikipedia.org/wiki/Birthday_problem)

I love the birthday problem, mostly because it challenges people's basic senses of intuition when it comes to math and logic puzzles. For a few skeptical Y1's (and one IB1) I coded (very hastily) a Python script to generate and validate the Birthday Problem. I won't spoil the solution for the problem, as always.

## Technical

Run this simply with `python automated.py`. You'll need Python, of course

The script takes in three parameters (declared as variables at the top of the script):
* `iterations`, or how many rooms you want to generate
* `people`, or how many people are in each room
* `days`, or how many days are in each year

The script will then generate `iterations` iterations, analyze the data, and output it to your terminal (stdout) for you to see!
