# Model Interpretability

## SHAP

### Q&A

**What are SHAP values?**
They are the average marginal effect of the feature into the final outcome.

**What is the difference between SHAP and Shapley values?**
SHAP values are calculated in a python library and consists in an **approximation** of the original Shapley values. Since Shapley values require dificult mathematical calculations, SHAP values allows a similar number in a simpler way. In other words, SHAP values is a more cost-efficient approach. 

**How SHAP values are calculated?**
The algorithm require (1) the model and (2) the train data, and then it retrain the model adding each variable. It is a extensive process, and in the end a total of $sample size^(number of features)$.   

**What is local and global interpretability?**
Local interpretability means the impact of each variable to the outcome of a specific observation. It does not mean the impact of each variable in general for the model, but only for that single observation. On the other hand, global interpretability means the effect of each feature in all observations. 

**Global interpretability is equivalent to causation?**
No. 

### Sources

- https://shap.readthedocs.io/en/latest/index.html
- https://towardsdatascience.com/shap-explained-the-way-i-wish-someone-explained-it-to-me-ab81cc69ef30