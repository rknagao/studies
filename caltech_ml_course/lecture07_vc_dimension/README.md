# Lecture 07 - The VC dimension

## Objective
1. Introduce the main concepts of VC dimension.
2. Demonstrate the Growth Function with Break Point leads to a polynomial equation.
3. Demonstrate the Growth Function with Break Point can replace **M** in Hoeffding Inequality.

## Definition
VC dimensions it is the most points of a subsample that a specific hypothesis family (i.e. learning algorithm) can shatter.

**Remember**: to shatter a sample means that using only a specific hypothesis family (e.g. straight lines with different starting points and/or angles) it should be possible to reproduce all possible labels for every element.


### Perk 1: Generalization
Given (1) a dataset and (2) a hypothesis set, the VC dimension varies from 1 to infinite. What we are looking for is a finite VC dimension, for it allows us to achieve a polynomial version of the Hoeffding Inequality. In addition, as the VC dimensions is finite, we can be sure (how?) the results can be generalized by any learning algorithm (i.e. hypothesis set). In other words, once a finite VC dimension is achieved by a specific learning algorithm, all other algorithm can be used (why?). 

### Perk 2: Probability distribution
As VC dimensions is finite, the second perk of it is to disregard the probabilty distribution of both population and sample. The logic is:

- a dichotomiy is obtained by organizing a subsample in a specific way that allows it to be shatterd by a hypothesis set;
- the specific configuration of the subset in theory could be obtained from any probability distribution, being that probable or improbable;
- Hoeffding Inequality specify the condition for the worse case cenario, so it does not concern how probable or improbable that cenario is.

In conclusion, since any subsample is sortable from all distributions, given plenty of tries, it is possible to get the very specific subsample used in the VC as our worse case cenario.


**Disclaimer:**
all the guarantees above are based on the probability of the sample sharing the same characteristics of the population, so it is not 100% guarantee.

## VC Dimension of Perceptrons

For perceptrons:

$$d_{vc} = dimension + 1$$

The proof is complex, and the train thought is:
- We will prove that $d_{vc} \leq d + 1$ and $d_{vc} \geq d + 1$
- Let's start with (...)
- Pick a set of $N = d + 1$ shattered points

## Interpreting the VC dimension

## Generalization bounds


Video: https://www.youtube.com/watch?v=Dc0sr0kdBVI&t=2897s
stopped at: https://youtu.be/Dc0sr0kdBVI?t=969