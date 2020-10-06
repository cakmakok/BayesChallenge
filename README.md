# Bayes Coding Challenge

This Coding Challenge is symbolizing the handling of data inputs from different sources that have to be merged together
in specific ways. In the `main` function, the program will run a set of encoded data objects through a merger class 
(containing your code challenge implementation) and the outputs are compared with expected solutions.

The input data has the following data points:
* `channel`: A description of the **source** of that data
* `switch`: A True/False value
* `average`: An integer
* `majority`: A categorized value

Each message is an update to the **state** that a specific `channel` is in. So a received message is giving you a 
partial update on the **current** state of one of the available channels. Together, the series of messages gives you a
progressing state of all the channels. 

Your task is to write the implementation for a merging functionality that handles those inputs one at a time and creates
a **combined state** with the following rules:

1. `switch` should be the value of the *last received message*
2. `average` should be the average of the **current** values *over all `channels`*
3. `majority` should be the category that is **currently** *shared by the most `channel`s*
(one category only overruling the previous one once it has **more** votes)

The current state should be accessible by calling `state` (see implementation template).

Additionally, there should be a method `reversed_state` that outputs the state *as if the messages were sent in the 
reversed order*.
