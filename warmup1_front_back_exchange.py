#Problem Name: Front and back charecter exchange
#Given a string, return a new string where the first and last chars have been exchanged.

#front_back('code') → 'eodc'
#front_back('a') → 'a'
#front_back('ab') → 'ba'

#Soultions:

def front_back(str):
  if len(str) <=1:
    return str
  mid= str[1:-1]
  
  return str[-1]+mid+str[0]
