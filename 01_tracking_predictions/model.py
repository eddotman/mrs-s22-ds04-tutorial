import random

class SynthesizabilityModel:
  def __init__(self):
    random.seed(123)
  
  def predict_single(self, data_pt) -> float:
    return random.random()
