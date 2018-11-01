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


def isdead(child ,close):
    for c in close:
        if child[0] == c[0]:
                return True
    return False

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
    # this part is my trying to understand how it's works
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())
    # startstate = problem.getStartState()
    # openlist = util.Stack()
    # openlist.push(problem.getStartState())
    # patch =[]
    # # n = openlist.pop()
    # # for i in problem.getSuccessors(n):
    # #     openlist.push(i[0])
    # # n = openlist.pop()
    # # print n
    # # s = problem.getSuccessors(n)
    # # print s
    # closelist = util.Stack()
    # x = 1500
    # # while openlist.isEmpty() is not True:
    # while x is not 0:
    #     print "hear"
    #     x -= 1
    #     n = openlist.pop()
    #
    #     if problem.isGoalState(n):
    #         return patch
    #     else:
    #         closelist.push(n)
    #         for i in problem.getSuccessors(n):
    #             openlist.push(i[0])
    #             # return [i[1]]
    #
    # # print openlist.pop()
    # # print openlist.pop()
    # # print "pacman State is:", problem.isWin(problem.getStartState())
    # return ["West"]
    # initial freng, close lists and the patch of goal
    # open = util.Stack()
    # close = []
    # patch = []
    # # getStartState
    # startState = problem.getStartState()
    # # initial a flage that show we arrive to goal or not
    # flag = False
    # i = 100
    # while flag is False and i is not 0:
    #     i -= 1
    #     if open.isEmpty() and len(close) is 0:
    #         open.push([startState, "root", 0])
    #         patch.append([startState, "root", 0])
    #     cs = open.pop()
    #     # print cs[1]
    #     lp = patch.pop()
    #     # print lp[1]
    #     if util.manhattanDistance(lp[0], cs[0]) == 1:
    #         patch.append(lp)
    #         patch.append(cs)
    #     else:
    #         patch.append(cs)
    #     # print patch
    #     if problem.isGoalState(cs[0]):
    #         # patch.append(cs)
    #         flag = True
    #     else:
    #         close.append(cs)
    #         print "close1", close
    #         children = problem.getSuccessors(cs[0])
    #         print "chidren", children
    #         children.reverse()
    #         print "children", children
    #         for child in children:
    #             if util.manhattanDistance(child[0], cs[0]) == 2:
    #                 continue
    #             # if child[1] == "West" and cs[1] == "East":
    #             #     continue
    #             # if child[1] == "East" and cs[1] == "West":
    #             #     continue
    #             # if child[1] == "South" and cs[1] == "North":
    #             #     continue
    #             # if child[1] == "North" and cs[1] == "South":
    #             #     continue
    #             # print close
    #             if isdead(child, close):
    #                 print 1
    #                 continue
    #             # else:
    #             #     open.push(child)
    #
    #             # print "close", close
    #             print 2
    #             open.push(child)


    # patch = ["South", "South", "West", "West", "West", "West", "South", "South",
    #  "East", "East", "East", "East", "South", "South", "West", "West", "West",
    #   "West", "South", "South", "East", "East", "East", "East", "South", "South",
    #    "West", "West", "West", "West", "South", "South", "East", "East", "East",
    #    "East", "South", "South", "West", "West", "West","South","South", "South"]
    # def checkfamily()
    # open.push(startState)
    # while open.isEmpty() is False:
    #     cs = open.pop()
    #     if len(patch) is 0:
    #         x = []
    #         x.append(cs)
    #         patch.append(x)
    #     lp = patch.pop()
    #     # print lp[1]
    #     if util.manhattanDistance(lp[0], cs[0]) == 1:
    #         patch.append(lp)
    #         patch.append(cs)
    #     else:
    #         patch.append(cs)
    #     if problem.isGoalState(cs):
    #         patch2 = []
    #         for p in patch:
    #             patch2.append(p[1])
    #         return patch2
    #     else:
    #         close.append(cs)
    #         children = problem.getSuccessors(cs)
    #         for child in children:
    #             flag = False
    #             for c in close:
    #                 if c[0] != child[0]:
    #                     flag = True
    #             if flag:
    #                 open.push(child)



    # patch2 = []
    # for p in patch:
    #     patch2.append(p[1])
    # #     patch.remove(p)
    # #     while p[0][0]:
    # #         pass
    # patch2.remove(patch[0][1])
    # # patch2.remove('e')
    # print "hear"
    # # print close
    # print patch2
    # return patch2


    # start again !!

    # initial parameters
    openlist = []
    closelist =  []
    patch = []
    ss = [problem.getStartState() , "root" , 0]
    # print ss
    openlist.append(ss)
    while len(openlist) is not 0:
        cs = openlist.pop()
        #this part produce the patch
        if cs[1] != "root":
            lp =patch.pop()
            # this while remove extra nodes in patch by calculate manhattan Distance 
            while util.manhattanDistance(lp[0],cs[0]) != 1:
                lp =patch.pop()
            patch.append(lp)
            patch.append(cs)
        else:
            patch.append(cs)

        if problem.isGoalState(cs[0]):

            answerpatch = []
            for p in patch:
                answerpatch.append(p[1])
            answerpatch.remove(patch[0][1])
            print patch
            return answerpatch
        else:
            closelist.append(cs)
            children = problem.getSuccessors(cs[0])
            children.reverse()
            for child in children:
                flag = False
                for c in closelist:
                    if child[0] == c[0]:
                        flag =True
                        break
                if flag:
                    continue
                openlist.append(child)

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
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
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
