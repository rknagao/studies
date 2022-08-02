# Lecture 02 - Is Learning Feasible?

## Lecture

- ML models create hypothesis based on the sample data. However, how can we be sure that the sample data is not very different from the population sample? Ex.: a model is tryng to classify the fish species in the world, but as the sample is collected from caribean waters, the model is strongly biased and assumes high concentration of caribean fish species in every prediction.the whole world.
- Hoeffding's Inequality minimizes the risk of using the sample even though it can be imperfect. The idea is to present a maximum probability threshold in which the difference between the sample and population mean will be relevantly big, given (1) the tolerance of the difference and (2) the sample size.
- Hoeffding's Inequality has the advantage of not requiring assumptions about the sample and population distribution, which is unknown for most cases.
- Hoeffding's Inequality can be applied to performance and hypothesis (or variables coefficients estimators). Just substitute the mean for the performance or hypothesis for comparison.
- The catch is that the original Hoeffding's Inequality does not apply for a multiple variable model. For such, a modification is necessary, the threshold is multiplied for the number of features.
- The problem with the adapted Hoeffding's Inequality is that the more variables in the model, the higher the threshold become.
- An interesting question about the hypothesis appeared in the Q&A section: "they though each H was a model". This is true when facing simple models like Linear Regression, in which the set of estimators result in the hypothesis function, but not anymore we use more complexes model, like ensemble models. Since ensemble models are an aggregated of smallers models, the main model will require multiple hyphesis.
- The Hoeffding Inequation will be further explored in lecture 05.

Lecture: https://youtu.be/FIbVs5GbBlQ?t=1572

## Homework

1. **D**: Not learning, supervised learning and reinforcement learning. 
2. **A**: potencial fraud and traffic lights cycle. 
3. **D**: $2/3$ using Bayes Theorem $P(A|B) = \frac{P(B|A) * P(A)}{P(B)}$.
4. **B**: $0.45^{10}$
5. **C**: $1 - P({only \, green \, marbles})^{1000}$
2. ****:
2. ****:

2. ****:
2. ****:
2. ****:



Homework: https://work.caltech.edu/homework/hw1.pdf