import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

model = BayesianNetwork([('age', 'heartdisease'), 
                         ('gender', 'heartdisease'), 
                         ('family', 'heartdisease'), 
                         ('diet', 'heartdisease'), 
                         ('lifestyle', 'heartdisease'), 
                         ('cholestrol', 'heartdisease')])
model.fit(pd.read_csv('heart1.csv'), estimator=MaximumLikelihoodEstimator)

infer = VariableElimination(model)
print(infer.query(['heartdisease'], {'cholestrol': 2}))
print(infer.query(['heartdisease'], {'diet': 1}))
