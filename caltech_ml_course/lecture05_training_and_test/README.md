# Lecture 05 - Training versus Test

## Objective
Introduce practical mathematical ways of distinguish training error and test error.

## Hoeffding Inequality
Revisiting Hoeffding Inequality introduced in lecture 02, it is possible to establish a theoretically probability for in sample error and out of sample error to be acceptable:


<div>
<img src="img/hoeffding-train-test.PNG" width="600"/>
<div>

For the training equation **M** accounts for the iterations necessary to train the model, and the catch is: in practice this number is big and the final probability becomes 1.

> **Q**: *"M indicates the errors of each iteration sums to the others. Shouldn't we pick the error exclusively of the final and better model?"*

> **A**: No, with each iteration the model learn more from the sample, resulting in a smaller in sample error and consequently a smaller probability. Therefore, M constitutes a penalty element for the training process.

The next step is to rework M to better suit us.


## Finding a better **M**

Theoretically, **M** being the sum of all errors is a **conservative** approach since it carries the maximum error during all iterations. It means also that a element that qualifies as a error will be accounted at every single iteration the error persists. It is not a efficient and it may invalidate needlessly a model.

One possible approach is to consider only the marginal error increased at each iteration. The figure below illustrate it:

<div>
<img src="img/overlapping-errors.PNG" width="600"/>
<div>

Suppose each iteration moves the threshold line a little bit, and both the blue and green lines represent this evolution. Yellow area represent the marginal error increase. The modifications in **M** will require that the yellow area resulted of each iteration change are equivalent.

Instead of considering the area, is possible to consider only the elements of sample and their prediction. In a binary classification problem, when given 3 elements, there are **2^N** possible scenarios:

<div>
<img src="img/m-as-2-n.PNG" width="600"/>
<div>

Each scenario (which is named as  **dichotomy** in the lecture) above have an associated hypothesis, and it could be used as a substitute for **M** applied in Hoeffding's Inequality. Although **2^N** is still a large number, it tends to be smalled than **M** iterations used to produce the final hypothesis for any model. The maximum number of scenarios used to substitute **M** will be called the **Growth Function**.


## Better M being polynomial
?


## Break Point

**Definition:** 
minimum sample size necessary to generate a dichotomy for a given **Growth Function**. (?)


In practice, **Break Point** (or BP in short) will be used as a measure of the complexity of the learning process. A learning process with BP = 2 will be a simpler one dimensional problem, where a learning process with BP = 4 will be a more complex two dimensional problem. 
(?)

## Puzzle
?

### IN PROGRESS (MUST REVIEW ENTIRE LECTURE. IT IS HARD!)


Video: https://www.youtube.com/watch?v=SEYAnnLazMU
Stopped: https://youtu.be/SEYAnnLazMU?t=2173