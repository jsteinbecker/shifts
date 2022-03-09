import numpy as np

def a_n ():
  """fx: returns a list of ints"""
  
  # values:
  oct1 = 440    #hz
  oct2 = oct1 * 2
    # 880
  steps = 12

  n = np.linspace(oct1, oct2, steps)
  return print(list(n))

if __name__ == "__main__":
   a_n()
