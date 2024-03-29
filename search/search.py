# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    "*** YOUR CODE HERE ***"

    # Create a stack for DFS traversal
    stk = util.Stack()
    # Empty list to store nodes visited and directions
    visitednodes = []

    # Get the initial state of Pacman
    startState = problem.getStartState()
    stk.push([startState, ""])

    while(True):

        if stk.isEmpty():break

        currNode = stk.pop()

        # If goal state found return the action list
        if problem.isGoalState(currNode[0]):
            # From string create a new list by splitting ',' and removing NULL values
            return filter(None, currNode[1].split(","))

        elif not currNode[0] in visitednodes:
            # Mark node as visited
            visitednodes.append(currNode[0])
            # Get all successors for the current node
            successors = (problem.getSuccessors(currNode[0]))
            for successor, action, cost in successors:
                # Add the node and the directions to the stack
                stk.push([successor, currNode[1] + "," + action])


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Create a stack for DFS traversal
    queue = util.Queue()
    # Empty list to store nodes visited and directions
    visitednodes = []

    # Get the initial state of Pacman
    startState = problem.getStartState()
    queue.push([startState, ""])

    while (True):

        if queue.isEmpty(): break
        currNode = queue.pop()
        # If goal state found return the action list
        if problem.isGoalState(currNode[0]):
            # From string create a new list by splitting ',' and removing NULL values
            return filter(None, currNode[1].split(","))
        elif not currNode[0] in visitednodes:
            # Mark node as visited
            visitednodes.append(currNode[0])
            # Get all successors for the current node
            successors = (problem.getSuccessors(currNode[0]))
            for successor, action, cost in successors:
                # Add the node and the directions to the stack
                queue.push([successor, currNode[1] + "," + action])


def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    priorityQ = util.PriorityQueue()
    startState = problem.getStartState()
    priorityQ.push([startState, "", 0], 0)
    # Empty list to store nodes visited and directions
    visitednodes = []

    while (True):

        if priorityQ.isEmpty():break
        currNode = priorityQ.pop()

        # If goal state found return the action list
        if problem.isGoalState(currNode[0]):
            # From string create a new list by splitting ',' and removing NULL values
            return filter(None, currNode[1].split(","))

        elif not currNode[0] in visitednodes:
            # Check node in visitednodes list or not
            visitednodes.append(currNode[0])
            # get the next successor
            successors = problem.getSuccessors(currNode[0])
            # Push the state, cost uptil now to the queue state. The cost will also be passed to Priority Q as an argument
            for successor, action, cost in successors:
                # cost + currNode[2] cost is the cost uptil now
                priorityQ.push([successor, (currNode[1] + "," + action), cost + currNode[2] ], cost + currNode[2] )

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"


    priorityQ = util.PriorityQueue()
    startState = problem.getStartState()
    priorityQ.push([startState, "", 0], 0)
    # Empty list to store nodes visited and directions
    visitednodes = []

    while (True):

        if priorityQ.isEmpty():break
        currNode = priorityQ.pop()

        # If goal state found return the action list
        if problem.isGoalState(currNode[0]):
            # From string create a new list by splitting ',' and removing NULL values
            return filter(None, currNode[1].split(","))

        elif not currNode[0] in visitednodes:
            # Check node in visitednodes list or not
            visitednodes.append(currNode[0])
            # get the next successor
            successors = problem.getSuccessors(currNode[0])
            # Push the state, cost uptil now to the queue state. The cost will also be passed to Priority Q as an argument
            # Also we need to add the heuristic cost as well because f = h + g
            for successor, action, cost in successors:
                priorityQ.push([successor, (currNode[1] + "," + action), cost + currNode[2] ], cost + currNode[2] + heuristic(successor, problem))

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
