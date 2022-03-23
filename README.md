# Simple-agents-coding-exercise
A simple reflex agent
On our factory floor for our first agent we have a single conveyor belt.  Products move along the conveyor belt and are examined by our agent.  For our first scenario, assume that our agent has two "quality sensors" that provide its percepts on a single belt.  The "quality sensor" provides a numeric ranking of the number of flaws found in each item coming down the conveyor belt.  The higher the rank, the more flaws that the item has in it.  Our first agent is running quality control checks at the end of the belt (before the items fall into a sorting bin to be packaged), and we need the agent to remove the items with the most flaws from the belt.
For this scenario, our agent is very limited - it is only capable of comparing the two items at the end of a single belt and it is only capable of having the robot arm remove the one at the very end of the belt.  It will be a simple reflex agent that compares the two items and, if the one at the end of the belt has more flaws than the one behind it, it will remove it from the belt.  Otherwise it will advance the belt and compare the next pair of items.
Performance Measure:  The robot successfully choose to pick up or advance the belt as appropriate in each situation
Environment: Conveyor belt, items of various quality on the belt
Actuators: Arm to pick up item on the front of the belt, belt-advance button, belt-stop button
Sensors: Two "quality sensors" on the end of the belt that measure the front two items on the belt

The belt will be represented as a list of numbers, with all items on the belt ranked by quality.  Items are ranked based on their number of flaws, so items of the best quality will have a rank of 1, while items of the worst quality will have larger values coming from the quality sensors.  If there is no item at a position on the belt, the quality sensor will return a value of 0.  If the end of the belt has been reached, the quality sensor returns a value of -1.

Build a reflex agent that picks items up from the end of the belt if the item at the end has a larger number of flaws than the item behind it.  When it reaches the end of the belt, the agent should shut the belt off.  You will also need to build a "test harness" (or "world simulator") to operate the belt based on the actions returned by the agent.  Your test harness can be the main method of your program, while your ReflexAgent must be a separate class with a method that returns an action based on percepts.

Test Harness:  Your test harness must read an input file where the conveyor belt is represented as a list of numbers and store them in some way that can be manipulated. Your Test Harness program should:
1. Create a single conveyor belt from the input file
2. Run the perception/action loop with an agent
3. Provide input percepts to the agent (output these percepts as an informative message)
4. Take the action returned by the agent and make modifications to the conveyor belt based on that action (output this action as an informative message)
5. Terminate when the agent returns a STOP action (see below)
Note that when the Test Harness picks up an item from the front of the belt, the value at the front of the belt becomes 0 (because there is no item there any longer).
Reflex Agent:  The reflex agent must be a class reflexAgent with a single method that takes two input percepts (the two things on the belt) and returns a single action.  It should be a method defined as:
a = Action (int percept1, int percept2) 
and it should return an action.  It is up to you how to define the action (as a String, as an integer, as a character) but your Test Harness code should understand it and produce the proper output.
Your reflex agent can produce only one of 3 possible actions: PICKUP, ADVANCE or STOP.  If the item at the front of the belt has a larger value than the item behind it, the agent should issue the PICKUP action.  If the item at the front of the belt has a smaller (or equal) value than the item behind it, the agent should issue the ADVANCE action.  If the input percepts show that the agent is at the end of the belt, it should issue a STOP action.  It is up to you to decide how the agent should treat the final item on the belt but remember - it must make that decision based on only the percepts that it receives at that moment -- this is an agent without state.  Document in your comments how you choose to handle the "last item on the belt" problem and why you chose that solution.
Your Action method should:
	Take in two numbers as input percepts
	Return a single action to the Test Harness based on those percepts
	PICKUP if the one at the front is larger than the one behind it
	ADVANCE if the one at the front is smaller than (or equal to) the one behind it
	STOP if it is at the end of the belt. (Both input percepts are -1)
Note that the Reflex Agent method should NEVER touch the contents of the belt.  Only the test harness should manipulate the belt.  The Reflex Agent should only take in two input percepts and return a single action to be interpreted by the Test Harness.

Output:  The Test Harness should provide the following informative messages at each time step (i.e. each time it calls the Reflex Agent):
