# Model Interpretability

## SHAP

### Q&A

**What are SHAP values?**

They are the average marginal effect of the feature into the final outcome.


**What is the difference between SHAP and Shapley values?**

SHAP values are calculated in a python library and consists in an **approximation** of the original Shapley values. Since Shapley values require a lot of mathematical calculations, SHAP values allows a similar number in a simpler way. In other words, SHAP values is a more cost-efficient approach. 


**How Shapley values are calculated?**

The algorithm require (1) the model and (2) the train data, and then it retrains the original model with a differente set of features. This process is extensive and time consumming, since a total of $(sample size)^{number of features}$ models are being trained. After all this, the marginal effect of each feature is resulted from a weighted average marginal effect of the feature on the models in which it appeared.


**What is local and global interpretability?**

Local interpretability means the impact of each variable to the predicted outcome of a specific observation. On the other hand, global interpretability represents the average effect of each feature in all predicted observations. 


**Global interpretability is equivalent to causation?**

No, because SHAP are measuring the impact of each feature into the *predicted* outcome, but not the **real** outcome. This difference is crucial, since SHAP cannot simulate different cenarios of a single observation.


### Sources

- https://shap.readthedocs.io/en/latest/index.html
- https://towardsdatascience.com/shap-explained-the-way-i-wish-someone-explained-it-to-me-ab81cc69ef30
- https://christophm.github.io/interpretable-ml-book/shap.html
- https://towardsdatascience.com/introduction-to-shap-values-and-their-application-in-machine-learning-8003718e6827