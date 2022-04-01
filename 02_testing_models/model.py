import random

class SynthesizabilityModel:
  def __init__(self):
    random.seed(123)
  
  def predict_single(self, material:str) -> float:

    if type(material) is not str:
      raise TypeError("Materials must be string-based formulas!")
    
    # A "real" model would return a prediction from a trained model
    # But this is a placeholder for a binary classifier, 
    # because random.random will still return results on the interval [0,1]
    return random.random()
