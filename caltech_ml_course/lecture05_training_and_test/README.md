# Lecture 05 - Training versus Test

## Objective
Introduce practical mathematical ways of distinguish training error and test error.

## Hoeffding Inequality
Revisiting Hoeffding Inequality introduced in lecture 02, it is possible to establish a theoretically probability for in sample error and out of sample error to be acceptable:


<div>
<img src="img/hoeffding-train-test.PNG" width="500"/>
<div>

For the training equation **M** accounts for the iterations necessary to train the model, and the catch is: in practice this number is big and the final probability becomes 1.

> **Q**: *"M indicates the errors of each iteration sums to the others. Shouldn't we pick the error exclusively of the final and better model?"*

> **A**: No, with each iteration the model learn more from the sample, resulting in a smaller in sample error and consequently a smaller probability. Therefore, M constitutes a penalty element for the training process.

The next step is to rework M to better suit us.


## Finding a better **M**

Theoretically, **M** being the sum of all errors is a **conservative** approach since it carries the maximum error during all iterations. It means also that a element that qualifies as a error will be accounted at every single iteration the error persists. It is not a efficient and it may invalidate needlessly a model.





### IN PROGRESS


Video: https://www.youtube.com/watch?v=SEYAnnLazMU
Stopped: https://youtu.be/SEYAnnLazMU?t=899