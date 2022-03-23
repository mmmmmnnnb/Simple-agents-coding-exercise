#Author Tianyu Jin
#A simple reflex agent
# the agent, return signal as strings when receive different inputs.
class reflexAgent:
    def Action(self, percept1, percept2):
        if percept1 == -1:
            return "STOP"
        elif percept1 > percept2 and percept1 != 0:
            return "PICKUP"
        else:
            return "ADVANCE"
#The agent
agent = reflexAgent()
inputFile = input("Please enter your file directory: ")
f = open(inputFile)
#set a list as a conveyor belt
conveyor = []
#place the numbers on the belt
for line in f:
    conveyor.append(int(line))
# add two -1 in the end to make sure the belt will stop
conveyor.append(-1)
conveyor.append(-1)
#here is the initial Action and index
Action = ""
index = 0
# the loop that calls the agent, will stop 
while Action != "STOP":
    #set the two parcepts
    parcept1 = conveyor[index]
    parcept2 = conveyor[index + 1]
    #receive the action order from the agent
    Action = agent.Action(parcept1, parcept2)
    #print the current state and the action order
    print("INPUT PERCEPTION: " + str(parcept1) + ", " + str(parcept2))
    print("OUTPUT ACTION: " + Action)
    
    #pickup the object in front if receive the "PICKUP" order, or add the index.
    if Action == "PICKUP":
        conveyor[index] = 0
    else:
        index = index + 1
