###### Statistics definitions

# Frequentist vs. Bayesian statistics
- Frequentist:
    + tests whether an event (the hypothesis) occurs or not. for instance, a coin being fair. the hypothesis is tested by repeating the trial theoretically infinitte teimes to detremine if this differs from teh hypothesis. 

# Terms
- chi square test
    + x^2 test, used for testing relationships between categorical variables. null hypothesis of the chi square test is that no relationship exists on the categorical variables. 
    + the x2 test takes the difference between nteh actual and expected numbers and gives a number that can be used to compute a probability of the results being that extreme
    + calculation
        * take difference between actual and expected, square each of them, and divide that by expected.
        * then look at chi square distribution for appropriate degrees of freedom -- eg given table
        * degrees of freedom is just the number of categories -1 (because if you know 3 then the 4th will be calculable) 
    + eg null hypothesis is equal diistribution across categories (eg for elevators)
    + alternative hypothesis is that there is not an equal distribution
    + requires data:
        * n=n_samples
    + the goal of the test is to give you probability of the results being at least this extreme.
        * significance level 5% p =0.05
        * if lower than p, then reject null hypothesis