"""
Modeling and Simulation for Project Management


Sometimes, monitoring resources, budgets, and milestones for various projects and
divisions can present a challenge. Simulation tools help us improve planning and
coordination in the various phases of the project so that we always keep control of it. In
addition, the preventive simulation of a project can highlight the critical issues related
to a specific task. This helps us evaluate the cost of any actions to be taken. Through the
preventive evaluation of the development of a project, errors that increase the costs of a
project can be avoided.
In this chapter, we will deal with practical cases of project management using the tools
we learned about in the previous chapters. We will learn how to evaluate the results of the
actions we take when managing a forest using Markov processes, and then move on and
learn how to evaluate a project using the Monte Carlo simulation.270
Modeling and Simulation for Project Management
In this chapter, we're going to cover the following main topics:
• Introducing project management
• Managing a tiny forest problem
• Scheduling project time using the Monte Carlo simulation
Technical requirements
In this chapter, we will address modeling examples of project management. To deal with
these topics, it is necessary that you have a basic knowledge of algebra and mathematical
modeling.
To work with the Python code in this chapter, you'll need the following files (available on
GitHub at the following URL: https://github.com/PacktPublishing/Hands-
On-Simulation-Modeling-with-Python ):
• TinyForestManagement.py
• TinyForestManagementModified.py
• MonteCarloTasksScheduling.py
Introducing project management
To assess the consequences of a strategic or tactical move in advance, companies need
reliable predictive systems. Predictive analysis systems are based on data collection and
the projection of reliable scenarios in the medium- and long-term. In this way, we can
provide indications and guidelines for complex strategies, especially those that must
consider numerous factors from different entities.
This allows us to examine the results of the evaluation in a more complete and
coordinated way since we can simultaneously consider a range of values and,
consequently, a range of possible scenarios. Finally, when managing complex projects,
the use of artificial intelligence to interpret data has increased, thus giving these projects
meaning. This is because we can perform a sophisticated analysis of the information
in order to improve the strategic decision-making process we will undertake. This
methodology allows us to search and analyze data from different sources so that we can
identify patterns and relationships that may be relevant.Introducing project management
271
Understanding what-if analysis
What-if analysis is a type of analysis that can contribute significantly to making
managerial decisions more effective, safe, and informed. It is also the basic level of
predictive analysis based on data. What-if analysis is a tool capable of elaborating different
scenarios to offer different possible outcomes. Unlike advanced predictive analysis, what-if
analysis has the advantage of only requiring basic data to be processed.
This type of activity falls into the category of predictive analytics, that is, those that
produce forecasts for the future, starting from a historical basis or trends. By varying some
parameters, it is possible to simulate different scenarios and, therefore, understand what
impact a given choice would have on costs, revenues, profits, and so on.
It is therefore a structured method to determine which predictions related to strategy
changes can go wrong, thereby judging the probability and consequences of the studies
carried out before they happen. Through the analysis of historical data, it is possible
to create such predictive systems capable of estimating future results following the
assumptions that were made about a group of variables of independent inputs, thus
allowing us to formulate some forecasting scenarios with the aim of evaluating the
behavior of a real system.
Analyzing the scenario at hand allows us to determine the expected values related
​​
to a
management project. These analysis scenarios can be applied in different ways, the most
typical of which is to perform multi-factor analysis, that is, analyze models containing
multiple variables:
• Realization of a fixed number of scenarios by determining the maximum and
minimum difference and creating intermediate scenarios through risk analysis. Risk
analysis aims to determine the probability that a future result will be different from
the average expected result. To show this possible variation, an estimate of the less
likely positive and negative results is performed.
Random factorial analysis through the use of Monte Carlo methods, thus solving a
problem by generating appropriate random numbers and observing that fraction of the
numbers that obeys one or more properties. These methods are useful for obtaining
numerical solutions for problems that are too complicated to solve analytically.272
Modeling and Simulation for Project Management
Managing a tiny forest problem
As we mentioned in Chapter 5, Simulation-Based Markov Decision Processes, a stochastic
process is called Markovian if it starts from an instant t in which an observation of the
system is made. The evolution of this process will depend only on t, so it will not be
influenced by the previous instants. So, a process is called Markovian when the future
evolution of the process depends only on the instant of observing the system and does not
depend in any way on the past. MDP is characterized by five elements: decision epochs,
states, actions, transition probability, and reward.
Summarizing the Markov decision process
The crucial elements of a Markovian process are the states in which the system finds
itself, and the available actions that the decision maker can carry out on that state. These
elements identify two sets: the set of states in which the system can be found, and the
set of actions available for each specific state. The action chosen by the decision maker
determines a random response from the system, which ultimately brings it into a new
state. This transition returns a reward that the decision maker can use to evaluate the
goodness of their choice.
Important Note
In a Markovian process, the decision maker has the option of choosing which
action to perform in each system state. The action chosen takes the system to
the next state and the reward for that choice is returned. The transition from
one state to another enjoys the property of Markov: the current state depends
only on the previous one.
A Markov process is defined by four elements, as follows:
• S: System states.
• A: Actions available for each state.
• P: Transition matrix. This contains the probabilities that an action a takes the
system from s state to s' state.
• R: Rewards obtained in the transition from s state to s' state with an action a.
In an MDP problem, it becomes crucial to take actions to obtain the maximum reward
from the system. Therefore, this is an optimization problem in which the sequence of
choices that the decision maker will have to make is called an optimal policy.Managing a tiny forest problem
273
A policy maps both the states of the environment and the actions to be chosen to those
states, representing a set of rules or associations that respond to a stimulus. The policy's
goal is to maximize the total reward received through the entire sequence of actions
performed by the system. The total reward that's obtained by adopting a policy is
calculated as follows:
𝑇𝑇
𝑅𝑅 𝑇𝑇 = ∑ 𝑟𝑟 𝑡𝑡+1 = 𝑟𝑟 𝑡𝑡 + 𝑟𝑟 𝑡𝑡+1 + ⋯ + 𝑟𝑟 𝑇𝑇
𝑖𝑖=0
In the previous equation, r T is the reward of the action that brings the environment into
the terminal state s T . To get the maximum total reward, we can select the action that
provides the highest reward to each individual state. This leads to choosing the optimal
policy that maximizes the total reward.
Exploring the optimization process
As we mentioned in Chapter 5, Simulation-Based Markov Decision Processes, an MDP
problem can be addressed using dynamic programming (DP). DP is a programming
technique that aims to calculate an optimal policy based on a knowing model of the
environment. The core of DP is to utilize the state-value and action-value in order to
identify good policies.
In DP methods, two processes called policy evaluation and policy improvement are used.
These processes interact with each other, as follows:
• Policy evaluation is done through an iterative process that seeks to solve Bellman's
equation. The convergence of the process for k → ∞ imposes approximation rules,
thus introducing a stop condition.
• Policy improvement improves the current policy based on the current values.
In the DP technique, the previous phases alternate and end before the other begins via
an iteration procedure. This procedure requires a policy evaluation at each step, which it
done through an iterative method whose convergence is not known a priori and depends
on the starting policy; that is, we can stop evaluating the policy at some point, while still
ensuring convergence to an optimal value.274
Modeling and Simulation for Project Management
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
Now, let's see what tools we have available to deal with MDP problems in Python.Managing a tiny forest problem
275
Introducing MDPtoolbox
The MDPtoolbox package contains several functions connected to the resolution of
discrete-time Markov decision processes, that is, value iteration, finite horizon, policy
iteration, linear programming algorithms with some variants, and several functions we
can use to perform reinforcement learning analysis.
This toolbox was created by researchers from the Applied Mathematics and Computer
Science Unit of INRA Toulouse (France), in the Matlab environment. The toolbox was
presented by the authors in the following article: Chadès, I., Chapron, G., Cros, M. J.,
Garcia, F., & Sabbadin, R. (2014). MDPtoolbox: a multi-platform toolbox to solve stochastic
dynamic programming problems. Ecography, 37 (9), 916-920.
Important Note
The MDPtoolbox package was subsequently made available in other
programming platforms, including GNU Octave, Scilab, and R. It was later
made available for Python programmers by S. Cordwell. You can find out
more at the following URL: https://github.com/sawcordwell/
pymdptoolbox .
To use the MDPtoolbox package, we need to install it. The different installation
procedures are indicated on the project's GitHub website. As recommended by the author,
you can use the default Python pip package manager. Pip stands for Python Package
Index and is the largest and most official Python package repository. Anyone who
develops a Python package, in 99% of cases, makes it available on this repository.
To install the MDPtoolbox package using pip , just write the following command:
pip install pymdptoolbox
Once installed, just load the library to be able to use it immediately.
Defining the tiny forest management example
To analyze in detail how to deal with a management problem using Markovian processes,
we will use an example already available in the MDPtoolbox package. It deals with
managing a small forest in which there are two types of resources: wild fauna and trees.
The trees of the forest can be cut, and the wood that's obtained can be sold. The decision
maker has two actions: wait and cut. The first action is to wait for the tree to grow fully
before cutting it to obtain more wood. The second action involves cutting the tree to get
money immediately. The decision maker has the task of making their decision every 20
years.276
Modeling and Simulation for Project Management
The tiny forest environment can be in one of the following three states:
• State 1: Forest age 0-20 years
• State 2: Forest age 21-40 years
• State 3: Forest age over 40 years
We might think that the best action is to wait until we have the maximum amount of
wood to come and thus obtain the greatest gain. Waiting can lead to the loss of all the
wood available. This is because as the trees grow, there is also the danger that a fire could
develop, which could cause the wood to be lost completely. In this case, the tiny forest
would be returned to its initial state (state 1), so we would lose what we would have
gained.
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
1 or pass to state 2 or 3. In fact, if we are in state 1, we will have a probability p that we
remain in that state, which happens if a fire occurs. Always starting from state 1, if no fire
occurs, we have the remaining 1-p probability of moving to the next state, which is state 2.
From this, it is clear that when starting from state 1, the probability of passing to state 3 is
equal to 0 – it's impossible to do so.
Row 2 of the transition matrix contains the transition probabilities starting from state
2. In fact, starting from state 2, if a fire occurs, there will be an equal probability p to
pass into state 1. Always starting from state 2, if no fire occurs, we have the remaining
1-p probability of moving to the next state, which is state 3. In this case, once again, the
probability of remaining in state 2 is equal to 0.
Finally, if we are in state 3, if a fire occurs, we will have a probability equal to p of going to
state 1, and the remaining 1-p probability of remaining in state 3, which happens if no fire
occurs. The probability of going to state 2 is equal to 0.
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
4278
Modeling and Simulation for Project Management
The action of waiting for the growth of the forest will bring a reward of 0 for the first two
states, while the reward will be the maximum for state 3. The value of the reward in state
3 is equal to 4, which represents the value provided by the system by default. Let's see how
the vector of rewards is modified if you choose the cut action:
0
(
)
𝑅𝑅 , 2 = [ 1 ]
2
In this case, cutting in state 1 does not bring any reward since the trees are not able to
supply wood yet. The cut in state 2 brings a reward, but this is lower than the maximum
reward, which we said is obtainable if we wait for the end of the three periods t before
cutting. A similar situation arises if the cut is made at the beginning of the third period.
In this case, the reward is greater than that of the previous state but still less than the
maximum.
Addressing management problems using MDPtoolbox
Our goal is to develop a policy that allows us to manage the tiny forest in order to
obtain the maximum prize. We will do this using the MDPtoolbox package, which we
introduced in the previous section, and analyzing the code line by line:
"""


import mdptoolbox.example

if __name__ == "__main__":
    P, R = mdptoolbox.example.forest()

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
