# Exercise 4

1. Upgrade the calculator to generate the id using a list comprehension and the `max` function. Remove the global variable used to store the current id.

2. Replace the for loop for calculating the op name counts and replace it with a list comprehension and count the op names with the `count` function.

3. Update the calculate result to use the `reduce` function.

Bonus:

The kinds of calculations that the calculator can perform is hard coded. If a new operation was to be added, it would require updating many parts of the program. How can this hard coding be improved? Is it possible to define the list of calculations in one place and then use the list throughout the calculator? If possible, this would enable the addition of new operations without having to always refactor large parts of the program. See if you can build such a list of calculations using the techniques learned thus far. If successful, add a new calculation to the list to support expononents. The Python operator for exponents is `**`.