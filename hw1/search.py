

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
    print (problem.getPacmanState)

    """
    "*** YOUR CODE HERE ***"



    # start again !!

    # initial parameters
    openlist = []
    closelist =  []
    patch = []
    ss = [problem.getStartState() , "root" , 0, problem.getStartState() , "root" , 0]


    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # print util.manhattanDistance(problem.getStartState(), (1, 1))
    # return []
    open = util.PriorityQueue()
    close = []
    patch = []
    ss = problem.getStartState()
    open.push(ss, 0)
    while open.isEmpty() is not True:
        c_state, c_action ,c_gn= open.pop()
        if problem.isGoalState(c_state):
            patch.append(c_action)
            return patch
        else:
            close.append(c_state)

    # print problem.getCostOfActions(patch)
    # while True:
    #     cs = open.pop()
    #     patch.append(cs)
    #     if problem.isGoalState(cs[0]):
    #         answerpatch = []
    #         # answerpatch.append(cs[-1])
    #         while len(patch) is not 0:
    #             # print cs
    #             c = patch.pop()
    #             # print c
    #             if c[0] == cs[3]:
    #                 # print c
    #                 answerpatch.append(cs[1])
    #                 cs = c
    #         answerpatch.reverse()
    #         return answerpatch
    #     else:
    #         close.append(cs)
    #         children = problem.getSuccessors(cs[0])
    #         print children
    #         for child in children:
    #             for c in close:
    #                 if child != c:
    #                     child = [child[0], child[1], child[2], cs[0], cs[1], cs[2]+child[2]]
    #                     # open.update(child, child[5])
    #                     open.push(child, child[5])




    # print open.pop()
    # print open.pop()


    # util.raiseNotDefined()
    # while open.isEmpty() is False:
    #     cs = open.pop()
    #     # i -= 1
    #     patch.append(cs)
    #     if problem.isGoalState(cs[0]):
    #         answerpatch = []
    #         # answerpatch.append(cs[-1])
    #         while len(patch) is not 0:
    #             # print cs
    #             c = patch.pop()
    #             # print c
    #             if c[0] == cs[3]:
    #                 # print c
    #                 answerpatch.append(cs[1])
    #                 cs = c
    #         answerpatch.reverse()
    #         return answerpatch
    #     else:
    #         closelist.append(cs)
    #         children = problem.getSuccessors(cs[0])
    #         # print "b", children
    #         # for ch in children:
    #         #     # print ch
    #         #     if ch[2] == "West" or ch[2] == "South":
    #         #         children += ch
    #         #         break
    #         # children.reverse()
    #         # print "a", children
    #
    #         for child in children:
    #             flag = False
    #             for c in closelist:
    #                 if child[0] == c[0]:
    #                     flag =True
    #                     break
    #             if flag:
    #                 continue
    #             child = [child[0], child[1], child[2], cs[0], cs[1], cs[5]+child[2]]
    #             print child
    #             open.update(child, child[5])


    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
