import random

class SynthesizabilityModel:
  def __init__(self):
    random.seed(123)
  
  def predict_single(self, material:str) -> float:

    if type(material) is not str:
      raise TypeError("Materials must be string-based formulas!")

    return random.random()
