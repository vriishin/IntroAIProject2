# Trivial Pursuit
This project includes building a graph environment, multiple agents with different levels of knowledge and mobility that have to interact with the created environment in order to accomplish a goal, and collecting data to analyze the performance of the agents in pursuit of that goal.

## Environment
The environment for this project is a graph of nodes. Some of these nodes will be connected, allowing transit between them. Movement between unconnected nodes is impossible. As per the constraints of the project, there is a graph of 40 nodes, with 10 random edges such that no node has a degree more than 3

## Target
Moves randomly through the environment and the agents have to capture this target.

## Agent 0
*Agent 0 has complete knowledge, but limited movement.* This agent can see the target at all times, but the design of this agent is to sit at a random location and wait for the target to come to it to be captured.

## Agent 1
*Agent 1 has complete knowledge, but limited movement.* This agent can see the target at all times. This agent can only move 1 node at a time. The design of this agent is to use Djikstra's algorithm and move closer as fast as possible to the target at all times. If multiple such moves exist, it chooses them at random.

## Agent 2
*Agent 2 has complete knowledge, but limited movement.* This agent can see the target at all times. This agent can only move 1 node at a time. The design of this agent is a modified approach to reach the target than Agent 1. It behaves similarly as it uses Djikstra's algorithm, focuses on the different ways the target can move. 

## Agent 2
*Agent 2 has complete knowledge, but limited movement.* This agent can see the target at all times. This agent can only move 1 node at a time. The design of this agent is a modified approach to reach the target than Agent 1. It behaves similarly as it uses Djikstra's algorithm, focuses on the different ways the target can move. 

## Agent 3
*Agent 3 has partial knowledge, but free movement.* This agent cannot see the target, but know how it moves. This agent can explore a node and if the target is at that node, it means it has captured the target. The design of this agent is similar to Agent 0, to sit at a random location and wait for the target to come to it to be captured.

## Agent 4
*Agent 4 has partial knowledge, but free movement.* This agent cannot see the target, but know how it moves. This agent can explore a node and if the target is at that node, it means it has captured the target. The design of this agent uses Bayesian probability and Markov chains to maintain a probabilistic knowledge base that is updated based on where the agent has explored. This agent will move to a node that has the highest probability of containing the target and chooses at random when there are multiple with the same highest probability.

## Agent 5
*Agent 5 has partial knowledge, but free movement.* This agent cannot see the target, but know how it moves. This agent can explore a node and if the target is at that node, it means it has captured the target. The design of this agent is similar to Agent 4, but is optimized to prefer nodes that have been visited the least.

## Agent 6
*Agent 6 has partial knowledge, and limited movement movement.* This agent cannot see the target, but know how it moves. This agent can only move 1 node at a time. The design of this agent is similar to Agent 4, but since it has the added restraint of moving only 1 node at a time, it uses Djikstra's algorithm to find the shortest path to the highest probability node and moves there.

## Agent 7
*Agent 7 has partial knowledge, but free movement.* This agent cannot see the target, but know how it moves. This agent can explore a node and if the target is at that node, it means it has captured the target. The design of this agent is similar to Agent 6, but is optimized to calculate all the paths of the highest probability nodes, and take the shortest one to the agent. This way it moves as efficiently as possible.

## Performance Analysis
The agent performance was tracked by identifying the number of moves it took to capture the target.


## Authors
Harshith Samayamantula  
Reuben Rinu  
Vrishin Patel  
