"""
Managing a tiny forest problem

As we mentioned in Chapter 5, Simulation-Based Markov Decision Processes,
a stochastic process is called Markovian if it starts from an instant t in which an observation of the
system is made.

The evolution of this process will depend only on t, so it will not be
influenced by the previous instants.

So, a process is called Markovian when the future
evolution of the process depends only on the instant of observing the system and does not
depend in any way on the past.

MDP is characterized by five elements: decision epochs,
states, actions, transition probability, and reward.
Summarizing the Markov decision process

The crucial elements of a Markovian process are the states in which the system finds
itself, and the available actions that the decision maker can carry out on that state.

These elements identify two sets: the set of states in which the system can be found, and the
set of actions available for each specific state.

The action chosen by the decision maker
determines a random response from the system, which ultimately brings it into a new
state.

This transition returns a reward that the decision maker can use to evaluate the
goodness of their choice.

Important Note
In a Markovian process, the decision maker has the option of choosing which
action to perform in each system state.

The action chosen takes the system to
the next state and the reward for that choice is returned.
The transition from one state to another enjoys the property of Markov:
the current state depends only on the previous one.

A Markov process is defined by four elements, as follows:
• S: System states.
• A: Actions available for each state.
• P: Transition matrix. This contains the probabilities that an action a takes the system from s state to s' state.
• R: Rewards obtained in the transition from s state to s' state with an action a.

In an MDP problem, it becomes crucial to take actions to obtain the maximum reward
from the system.

Therefore, this is an optimization problem in which the sequence of
choices that the decision maker will have to make is called an optimal policy.

A policy maps both the states of the environment and the actions to be chosen to those
states, representing a set of rules or associations that respond to a stimulus.

The policy's
goal is to maximize the total reward received through the entire sequence of actions
performed by the system.

The total reward that's obtained by adopting a policy is
calculated as follows:

𝑅_𝑇 = ∑ (i goes from 0 to T) 𝑟_𝑡+1 = 𝑟_𝑡 + 𝑟_𝑡+1 + ⋯ + 𝑟_𝑇

In the previous equation,
r T is the reward of the action that brings the environment into the terminal state s T .
To get the maximum total reward, we can select the action that
provides the highest reward to each individual state. This leads to choosing the optimal
policy that maximizes the total reward.

Exploring the optimization process
As we mentioned in Chapter 5, Simulation-Based Markov Decision Processes, an MDP
problem can be addressed using dynamic programming (DP).
DP is a programming
technique that aims to calculate an optimal policy based on a knowing model of the
environment.

The core of DP is to utilize the state-value and action-value in order to
identify good policies.

In DP methods, two processes called policy evaluation and policy improvement are used.
These processes interact with each other, as follows:

• Policy evaluation is done through an iterative process that seeks to solve Bellman's
equation. The convergence of the process for k → ∞ imposes approximation rules,
thus introducing a stop condition.

• Policy improvement improves the current policy based on the current values.
In the DP technique, the previous phases alternate and end before the other begins via
an iteration procedure.

This procedure requires a policy evaluation at each step, which it
done through an iterative method whose convergence is not known a priori and depends
on the starting policy; that is, we can stop evaluating the policy at some point, while still
ensuring convergence to an optimal value.

Important Note
The iterative procedure we have described uses two vectors that preserve the
results obtained from the policy evaluation and policy improvement processes.
We indicate the vector that will contain the value function with V; that is,
the discounted sum of the rewards obtained. We indicate the carrier that will
contain the actions chosen to obtain those rewards with Policy.
The algorithm then, through a recursive procedure, updates these two vectors. In the
policy evaluation, the value function is updated as follows:

𝑉𝑉 (𝑠𝑠) = ∑ 𝑃𝑃 𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃(𝑠𝑠) (𝑠𝑠, 𝑠𝑠 ′ ) (𝑅𝑅 𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃(𝑠𝑠) (𝑠𝑠, 𝑠𝑠 ′ ) + 𝛾𝛾 ∗ 𝑉𝑉(𝑠𝑠 ′ ))
𝑠𝑠′
In the previous equation, we have the following:
•
•
( )
is the function value at the state s.
( , ′)
is the reward returned in the transition from state s to state s'.
• γ is the discount factor.
•
( ′ )
is the function value at the next state.
In the policy improvement process, the policy is updated as follows:
( )
In the previous equation, we have the following:
•
•
( ′)
is the function value at state s'.
( , ′)
is the reward returned in the transition from state s to state s' with action a.
• γ is the discount factor.
•
( , ′ )
is the probability that an action a in the s state is carried out in the s' state.

Now, let's see what tools we have available to deal with MDP problems in Python.

Managing a tiny forest problem

Introducing MDPtoolbox
The MDPtoolbox package contains several functions connected to the resolution of
discrete-time Markov decision processes, that is, value iteration, finite horizon, policy
iteration, linear programming algorithms with some variants, and several functions we
can use to perform reinforcement learning analysis.

This toolbox was created by researchers from the Applied Mathematics and Computer
Science Unit of INRA Toulouse (France), in the Matlab environment.

The toolbox was presented by the authors in the following article: Chadès, I., Chapron, G., Cros, M. J.,
Garcia, F., & Sabbadin, R. (2014). MDPtoolbox: a multi-platform toolbox to solve stochastic
dynamic programming problems. Ecography, 37 (9), 916-920.

Important Note
The MDPtoolbox package was subsequently made available in other
programming platforms, including GNU Octave, Scilab, and R. It was later
made available for Python programmers by S. Cordwell. You can find out
more at the following URL: https://github.com/sawcordwell/pymdptoolbox .

Defining the tiny forest management example
To analyze in detail how to deal with a management problem using Markovian processes,
we will use an example already available in the MDPtoolbox package.

It deals with managing a small forest in which there are two types of resources:
wild fauna and trees.

The trees of the forest can be cut, and the wood that's obtained can be sold.

The decision maker has two actions: wait and cut.

The first action is to wait for the tree to grow fully before cutting it to obtain more wood.

The second action involves cutting the tree to get money immediately.
The decision maker has the task of making their decision every 20 years.

The tiny forest environment can be in one of the following three states:
• State 1: Forest age 0-20 years
• State 2: Forest age 21-40 years
• State 3: Forest age over 40 years

We might think that the best action is to wait until we have the maximum amount of
wood to come and thus obtain the greatest gain.

Waiting can lead to the loss of all the wood available.

This is because as the trees grow, there is also the danger that a fire could develop,
which could cause the wood to be lost completely.

In this case, the tiny forest would be returned to its initial state (state 1),
so we would lose what we would have gained.

In the case a fire does not occur, at the end of each period t (20 years), if the state is
s and the wait action is chosen, the forest will move to the next state, which will be
the minimum of the following pair (s + 1, 3). If there are no fires, the age of the forest
will never assume a state higher than 3 since state 3 matches with the oldest age class.

Conversely, if a fire occurs after the action is applied, the forest returns the system to its
initial state (state 1), as shown in the following image:

Figure 10.1 – States of the age of a forest
Set p = 0.1 as the probability that a fire occurs during a period t. The problem is how
to manage this in the long-term to maximize the reward. This problem can be treated
as a MDP.

Now, let's move on and define the problem as an MDP. We have said that the elements of
an MDP are state, action, transition matrix P, and reward R. We must then define these
elements. We have defined the states already – there are three. We also defined the actions:
wait or cut. We pass these to define the transition matrix P (s, s', a). It contains the chances
of the system going from one state to another. We have two actions available (Wait, Cut),
so we will define two transition matrices. If we indicate with p the probability that a fire
occurs, then in the case of the wait action, we will have the following transition matrix:Managing a tiny forest problem
277
𝑝𝑝 1 − 𝑝𝑝
0
0
1 − 𝑝𝑝 ]
𝑃𝑃(, ,1) = [ 𝑝𝑝
𝑝𝑝
0
1 − 𝑝𝑝

Now, let's analyze the content of the transition matrix. Each row is relative to a state, in the
sense that row 1 returns the probabilities that, starting from state 1, it will remain in state
1 or pass to state 2 or 3.

In fact, if we are in state 1, we will have a probability p that we
remain in that state, which happens if a fire occurs.

Always starting from state 1, if no fire
occurs, we have the remaining 1-p probability of moving to the next state, which is state 2.
From this, it is clear that when starting from state 1, the probability of passing to state 3 is
equal to 0 – it's impossible to do so.
Row 2 of the transition matrix contains the transition probabilities starting from state
2. In fact, starting from state 2, if a fire occurs, there will be an equal probability p to
pass into state 1.

Always starting from state 2, if no fire occurs, we have the remaining
1-p probability of moving to the next state, which is state 3.

In this case, once again, the
probability of remaining in state 2 is equal to 0.

Finally, if we are in state 3, if a fire occurs, we will have a probability equal to p of going to
state 1, and the remaining 1-p probability of remaining in state 3, which happens if no fire
occurs.

The probability of going to state 2 is equal to 0.
Now, let's define the transition matrix in the case of choosing the cut action:
1 0 0
𝑃𝑃(, ,2) = [ 1 0 0 ]
1 0 0

In this case, the analysis of the previous transition matrix is much more immediate. In
fact, the cut action brings the state of the system to 1 in each instance. Therefore, the
probability is always 1. Then, that 1 goes to state 1 and 0 for all the other transitions as
they are not possible.

Now, let's define the vectors that contain the rewards; that is, the vector R (s, s', as we have
defined it), starting from the rewards returned by the wait action:
0
𝑅𝑅(, 1) = [ 0 ]

The action of waiting for the growth of the forest will bring a reward of 0 for the first two
states, while the reward will be the maximum for state 3. The value of the reward in state
3 is equal to 4, which represents the value provided by the system by default.

Let's see how
the vector of rewards is modified if you choose the cut action:
0
(
)
𝑅𝑅 , 2 = [ 1 ]
2

In this case, cutting in state 1 does not bring any reward since the trees are not able to
supply wood yet.
The cut in state 2 brings a reward, but this is lower than the maximum
reward, which we said is obtainable if we wait for the end of the three periods t before
cutting.

A similar situation arises if the cut is made at the beginning of the third period.
In this case, the reward is greater than that of the previous state but still less than the
maximum.

Addressing management problems using MDPtoolbox
Our goal is to develop a policy that allows us to manage the tiny forest in order to
obtain the maximum prize. We will do this using the MDPtoolbox package, which we
introduced in the previous section, and analyzing the code line by line:
"""

import mdptoolbox.example
import numpy as np
import scipy.sparse as sp


def forest(S=3, r1=4, r2=2, p=0.1, is_sparse=False):
    """
    Generate a MDP example based on a simple forest management scenario.

    This function is used to generate a transition probability
    (``A`` × ``S`` × ``S``) array ``P`` and a reward (``S`` × ``A``) matrix
    ``R`` that model the following problem. A forest is managed by two actions:
    'Wait' and 'Cut'. An action is decided each year with first the objective
    to maintain an old forest for wildlife and second to make money selling cut
    wood. Each year there is a probability ``p`` that a fire burns the forest.

    Here is how the problem is modelled.
    Let {0, 1 . . . ``S``-1 } be the states of the forest, with ``S``-1 being
    the oldest. Let 'Wait' be action 0 and 'Cut' be action 1.
    After a fire, the forest is in the youngest state, that is state 0.
    The transition matrix ``P`` of the problem can then be defined as follows::

                   | p 1-p 0.......0  |
                   | .  0 1-p 0....0  |
        P[0,:,:] = | .  .  0  .       |
                   | .  .        .    |
                   | .  .         1-p |
                   | p  0  0....0 1-p |

                   | 1 0..........0 |
                   | . .          . |
        P[1,:,:] = | . .          . |
                   | . .          . |
                   | . .          . |
                   | 1 0..........0 |

    The reward matrix R is defined as follows::

                 |  0  |
                 |  .  |
        R[:,0] = |  .  |
                 |  .  |
                 |  0  |
                 |  r1 |

                 |  0  |
                 |  1  |
        R[:,1] = |  .  |
                 |  .  |
                 |  1  |
                 |  r2 |

    Parameters
    ---------
    S : int, optional
        The number of states, which should be an integer greater than 1.
        Default: 3.
    r1 : float, optional
        The reward when the forest is in its oldest state and action 'Wait' is
        performed. Default: 4.
    r2 : float, optional
        The reward when the forest is in its oldest state and action 'Cut' is
        performed. Default: 2.
    p : float, optional
        The probability of wild fire occurence, in the range ]0, 1[. Default:
        0.1.
    is_sparse : bool, optional
        If True, then the probability transition matrices will be returned in
        sparse format, otherwise they will be in dense format. Default: False.

    Returns
    -------
    out : tuple
        ``out[0]`` contains the transition probability matrix P  and ``out[1]``
        contains the reward matrix R. If ``is_sparse=False`` then P is a numpy
        array with a shape of ``(A, S, S)`` and R is a numpy array with a shape
        of ``(S, A)``. If ``is_sparse=True`` then P is a tuple of length ``A``
        where each ``P[a]`` is a scipy sparse CSR format matrix of shape
        ``(S, S)``; R remains the same as in the case of ``is_sparse=False``.

    """
    assert S > 1, "The number of states S must be greater than 1."
    assert (r1 > 0) and (r2 > 0), "The rewards must be non-negative."
    assert 0 <= p <= 1, "The probability p must be in [0; 1]."
    # Definition of Transition matrix
    if is_sparse:
        P = []
        rows = list(range(S)) * 2
        cols = [0] * S + list(range(1, S)) + [S - 1]
        vals = [p] * S + [1 - p] * S
        P.append(sp.coo_matrix((vals, (rows, cols)), shape=(S, S)).tocsr())
        rows = list(range(S))
        cols = [0] * S
        vals = [1] * S
        P.append(sp.coo_matrix((vals, (rows, cols)), shape=(S, S)).tocsr())
    else:
        P = np.zeros((2, S, S))
        P[0, :, :] = (1 - p) * np.diag(np.ones(S - 1), 1)
        P[0, :, 0] = p
        P[0, S - 1, S - 1] = (1 - p)
        P[1, :, :] = np.zeros((S, S))
        P[1, :, 0] = 1
    # Definition of Reward matrix
    R = np.zeros((S, 2))
    R[S - 1, 0] = r1
    R[:, 1] = np.ones(S)
    R[0, 1] = 0
    R[S - 1, 1] = r2
    return (P, R)


def tfm():
    P, R = forest()

    print(P[0])
    print(P[1])

    print(R[:, 0])
    print(R[:, 1])

    gamma = 0.9

    PolIterModel = mdptoolbox.mdp.PolicyIteration(P, R, gamma)

    PolIterModel.run()

    print(PolIterModel.V)

    print(PolIterModel.policy)

    print(PolIterModel.iter)

    print(PolIterModel.time)


if __name__ == "__main__":
    tfm()
