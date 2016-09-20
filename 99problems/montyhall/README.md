# The Monty Hall Problem

> Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

From [Wikipedia](https://en.wikipedia.org/wiki/Monty_Hall_problem)

I had a student at Robotics kinda doubt me on the validity of the solution (I won't spoil it yourself, you can find the "answer" [here](https://en.wikipedia.org/wiki/Monty_Hall_problem#Simple_solutions)), so I wrote a program to deal with it. `automated.py` runs the program for any amount of simulations (I've included a default value under `iterations`), while `user.py` lets the user actually do the game show, and see just how many times they'll win by switching.

A few things:
* we assume that Python's `random` and `random.choice` are actually random (which they hopefully are)
* that my code is right (it should be, and I've done some bug testing)
* a few [assumptions about the problem](https://en.wikipedia.org/wiki/Monty_Hall_problem#Standard_assumptions)
