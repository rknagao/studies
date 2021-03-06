# Classification Models

## Generative Model

#### What is a Generative Model (GM)?

~Essentially, model that use conditional probabilities (e.g. given that we know the variable X, what is the probability of output Y).~ 

Generative Models tries to understand all features that results in each target, instead just finding the variables that are most differentiate the targets, which is the Discrimatory approach.


#### Why should I use it?

Pros:
- produces more consistent estimates if "there is a substantial separation between the two classes" (extracted directly from ISL and it is unclear what is a substantial separation);
- can be used in multiclass classifications;

Cons:
- all features must have normal distributions;
- lacks numerical metrics (e.g. accuracy, F2 Score);


#### How to use it?

Since the classification problem envolves conditional probability (i.e. probability of Y given a specific feature X), one crucial step is to identify what is the probability of the specific condition happens (i.e. probability of X). While in the discriminatory approach we would draw a probability exclusively from the sample, in the generative approach we would first identify the features's populational distribution, which would in turn provide a much more accurate probability.


## Notebooks

- **`linear_discriminant_analysis.ipynb`**: study on Linear Discriminant Analysis (LDA) with univariate feature.



#### Sources
- https://www.statlearning.com/
- https://towardsdatascience.com/a-generative-approach-to-classification-17a0b5876729
- https://medium.com/data-science-in-your-pocket/generative-modeling-the-overview-e4c60a5b4873
- https://arxiv.org/pdf/1906.02590.pdf
- https://towardsdatascience.com/linear-discriminant-analysis-explained-f88be6c1e00b