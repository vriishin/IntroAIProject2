Adjacency matrix

1 - 2
2 - 3
3
4
5

{
    1: []
}

< 10 random edges (keep a counter increment if addition of random is valid and added)
edge doesn't already exist (if end is in array of adjacencies for start node)
node doesn't have degree more than 3 (len of array of adjacencies for node)

generate random number (start node)
generate random number (end node)


CLL class (dict of adjacency matrix) --> cll with node 1 being head
    Attribute = dict of adjacencies so its easy to use while moving randomly etc.

Efficiency 
-- Dict for keeping arrays
-- Arrays for adjacencies
-- Because we're passing in the dict to the class


Agents Implementation
------- Limited Movement, Full Knowledge
0: Random trap
1: Djikstra's Algo (BFS)
2: Djikstra's Algo (BFS) on crack by checking the potential moves of target and choosing path where target's next move is the closest to the agent
------- Full Movement, Limited Knowledge
(How do we keep track of the Knowledge/evidence that you acquired)
3: The same as Agent 0? but with free movement but its still a landmine
4: Markov model and pick the most probable belief state
5: Look at the models and explore an option that can beat 4 (predictive model)
------- Limited Movement, Limited Knowledge
6: Combination of 4 and Djikstra's (end goal as the state with highest probability)
7: Improvement on 6?

NOTE: In order to get right data, Agents 1 and 2 spawn together, Agents 4 and 5 spawn together, and Agents 6 and 7 spawn together

Pickle for data persistence of random CLL environments
Record agent(what timestep is the target acquired) success in array 

while loop (status of any agent has not found target)
    Each agent has a turn function
    Update status of agent


## Work Distribution:
1. Planning -- Harsh, Reuben
2. Environment Setup -- Vrishin, Reuben, Harsh
3. Agent Implementation
    a. 0 -- 2 Harsh, Reuben
    b. 3 -- 4 Harsh, Reuben
    c. 5 Vrishin
    d. 6 -- 7 Harsh, Reuben


4. Report
    - Gray boxes -- Vrishin
    - Modeling and updating belief state mechanism (with probability) -- Harsh, Reuben, Vrishin
    - Implementation details of agents -- We write up our own implementation of agents
    - Data performance (Running and analyzing tests on a lot of random envs) -- Reuben
    - Reflection/Concluding Questions -- Vrishin