import random

class MLModel:
  def __init__(self):
    random.seed(123)
  
  def predict(self, data:list) -> list[float]:
    return [
      random.random() for d in data
    ]
