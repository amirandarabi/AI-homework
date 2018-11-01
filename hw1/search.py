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
        # if cs[1] != "root":
        #     # lp =patch.pop()
        #     # this while remove extra nodes in patch by calculate manhattan Distance
        #     # while util.manhattanDistance(lp[0],cs[0]) != 1:
        #     #     lp =patch.pop()
        #     flag = True
        #     while flag:
        #         lp =patch.pop()
        #         for ch in problem.getSuccessors(lp[0]):
        #             if ch[0] == cs[0]:
        #                 flag = False
        #                 break
        #     patch.append(lp)
        #     patch.append(cs)
        # else:
        #     patch.append(cs)
        if cs[1] != "root":
            flag = True
            while flag:
                lp = patch.pop()
                # print cs[3]
                # print lp[0][1]
                # print cs[3]
                print lp
                # print len(cs)
                # print len(lp)
                if cs[3][0] == lp[0][0] and cs[3][1] == lp[0][1]:
                    flag = False
            patch.append(lp)
            patch.append(cs)
        else:
            patch.append(cs)


        if problem.isGoalState(cs[0]):

            answerpatch = []
            for p in patch:
                answerpatch.append(p[1])
            answerpatch.remove(patch[0][1])
            # print patch
            return answerpatch
        else:
            closelist.append(cs)
            children = problem.getSuccessors(cs[0])
            # children.reverse()
            for child in children:
                flag = False
                for c in closelist:
                    if child[0] == c[0]:
                        flag =True
                        break
                if flag:
                    continue

                child = [child[0], child[1], child[2], cs[0]]
                # print child[3]

                openlist.append(child)

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # return []
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # return []
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
