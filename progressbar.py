#!/usr/bin/env python
# script to print a progress bar

import sys

class ProgressBar(object):

  def __init__(self, maximum=100):
    self.position = 0
  
  def set(self, position):
    if position > self.position:
      delta = position - self.position
    else:
      delta = 0
    self._print(delta)
    self.position = position
  
  def _print(self, length):
    sys.stdout.write('#'*length)
    sys.stdout.flush()

if __name__ == '__main__':
  import time
  SIZE = 30
  progress = ProgressBar(SIZE)
  for index in range(SIZE):
    progress.set(index)
    time.sleep(0.2)
