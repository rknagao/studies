# Lecture 06 - Theory of Generalization

## Objective
1. Demonstrate the Growth Function with Break Point leads to a polynomial equation.
2. Demonstrate the Growth Function with Break Point can replace **M** in Hoeffding Inequality.


# Recursive Bound

> $B(N, k)$: *"number of dichotomies with sample N and break point k"*

The previous puzzle is represented by B(3, 2) and it is represented in the table below:

| Category  | Number of rows | x1, x2 | x3 |
| --------  | -------------- | ------ | -- |
| S1        | alpha          |  1, 0  | 0  |
|           |                |  0, 1  | 0  |
| S2-       | beta           |  0, 0  | 0  |
| S2+       | beta           |  0, 0  | 1  |


**Train of Thought**
1. if we ommit x3, the S2- and S2+ category becomes identical and therefore one of them can be discarded. After this, the number of rows can be represented as $alpha+beta \leq B(N-1, k)$;
2. again, when omitting x3, the only difference between S2- and S2+ is lost, which is the same as subtracting one Break Point from the problem. Therefore, it can be represented as $beta \leq B(N-1, k-1)$; 

**Q & A**

> *"Why are isolating x3 from x1 and x2?"*

Because it allows a recursion, which means a solution applicable to smaller N. (?)


Video: https://www.youtube.com/watch?v=6FWRijsmLtE&t=149s
