#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
counter2=0
domains = {
   "Inter1":[3,4,5,6],
   "Inter2":[3,4,5,6],
   "Inter3":[3,4,5,6],
   "High1":[6,7,8],
   "High2":[6,7,8],
   "High3":[6,7,8]
 }
  


constraints = {

    ("Inter1","High1") : lambda I1,H1 : I1 != H1,
    ("Inter1","High2") : lambda I1,H2 : I1 != H2,
    ("Inter1","High3") : lambda I1,H3 : I1 != H3,
    
    ("High1","Inter1") : lambda H1,I1 : H1 != I1,
    ("High2","Inter1") : lambda H2,I1 : H2 != I1,
    ("High3","Inter1") : lambda H3,I1 : H3 != I1,
    
    ("Inter2","High1") : lambda I2,H1 : I2 != H1,
    ("Inter2","High2") : lambda I2,H2 : I2 != H2,
    ("Inter2","High3") : lambda I2,H3 : I2 != H3,
    
    ("High1","Inter2") : lambda H1,I2 : H1 != I1,
    ("High2","Inter2") : lambda H2,I2 : H2 != I2,
    ("High3","Inter2") : lambda H3,I2 : H3 != H3,
    
    
    ("Inter3","High1") : lambda I3,H1 : I3 != H1,
    ("Inter3","High2") : lambda I3,H2 : I3 != H2,
    ("Inter3","High3") : lambda I3,H3 : I3 != H3,
    
    ("High1","Inter3") : lambda H1,I3 : H1 != I3,
    ("High2","Inter3") : lambda H2,I3 : H2 != I3,
    ("High3","Inter3") : lambda H3,I3 : H3 != I3,
    
    ("Inter1","Fo") : lambda I1,f : I1 != 4,
    ("Inter3", "S") : lambda I3 ,s: I3 != 6,
    ("High2", "Se") : lambda H2,se : H2 != 7,
    
    ("Inter1","Inter2") : lambda I1,I2 : I1 < I2,
    ("Inter2","Inter1") : lambda I2,I1 : I2 > I1,
    ("Inter2","Inter3") : lambda I2,I3 : I2 < I3,
    ("Inter3","Inter2") : lambda I3,I2 : I3 > I2,
    ("Inter3","Inter1") : lambda I3,I1 : I3 > I1,
    
    
    ("High1","High2") : lambda H1,H2 : H1 < H2,
    ("High2","High1") : lambda H2,H1 : H2 > H1,
    ("High2","High3") : lambda H2,H3 : H2 < H3,
    ("High3","High2") : lambda H3,H2 : H3 > H2,
    ("High3","High1") : lambda H3,H1 : H3 > H1,
    ("High3","High2") : lambda H3,H2 : H3 > H2,

    


}



def revise(x, y):
    revised = False

    x_domain = domains[x]
    y_domain = domains[y]

    all_constraints = [
        constraint for constraint in constraints if constraint[0] == x and constraint[1] == y]

    for x_value in x_domain:
        satisfies = False
        for y_value in y_domain:
            for constraint in all_constraints:
                constraint_func = constraints[constraint]
                if constraint_func(x_value, y_value):
                    satisfies = True
        if not satisfies:
            x_domain.remove(x_value)
            revised = True

    return revised


def ac3(arcs):
    """
    Update `domains` such that each variable is arc consistent.
    """
    # Add all the arcs to a queue.
    queue = arcs[:]

    # Repeat until the queue is empty
    while queue:
        # Take the first arc off the queue (dequeue)
        (x, y) = queue.pop(0)

        # Make x arc consistent with y
        revised = revise(x, y)
       
        # If the x domain has changed
        if revised:
            # Add all arcs of the form (k, x) to the queue (enqueue)
            neighbors = [neighbor for neighbor in arcs if neighbor[1] == x]
            queue = queue + neighbors
    if domains["High2"] == [7]:
            domains["High2"]=None
    if domains["Inter1"] == [4]:
            domains["Inter1"]=None
    if domains["Inter3"] == [6]:
            domains["inter3"]=None

#arcs = [('A', 'B'), ('B', 'A'), ('B', 'C'), ('C', 'B')]
#------------------------------------
arcUp = [('Inter1', 'High1'), ('Inter1', 'High2'), ('Inter1', 'High3'), ('Inter2', 'High1'),('Inter2', 'High2'), ('Inter2', 'High3'),
('Inter3', 'High1'),('Inter3', 'High2'), ('Inter3', 'High3'), ("Inter1","Inter2"),
("Inter2","Inter1"),("Inter2","Inter3"),("Inter3","Inter2"),("Inter3","Inter1"),("High1","High2"),("High2","High1"),("High2","High3"),
("High3","High1"),("High3","High2")]

#ac3(arcs)
#------------------------------------
startc=time.time()
ac3(arcUp)
endc=time.time()
delec=endc-startc
delec*=1000000

print("The Arc3 is :")
print(domains)# {'A': [2, 3], 'C': [1, 2], 'B': [1, 2]}
print("the time is",delec,"MicroSecond")

counter = 0

DOMAINS = "DOMAINS"
VARIABLES = "VARIABLES"
CONSTRAINTS = "CONSTRAINTS"
FAILURE = "FAILURE"

def is_complete(assignment):
  return None not in (assignment.values())

def select_unassigned_variable(variables, assignment):
  for var in variables:
    if assignment[var] is None:
      return var

def is_consistent(assignment, constraints):
  global counter
  counter += 1
  for constraint_violated in constraints:
    if constraint_violated(assignment):
      return False
  return True

def init_assignment(csp):
  assignment = {}
  for var in csp[VARIABLES]:
      # dead stat 
      V = select_unassigned_variable(csp[VARIABLES], domains)
      if V is not None:
         assignment[var]=None
      # backtacing without AC-3
      else:
         return domains
  return assignment
  

def recursive_backtracking(assignment, csp):
  if is_complete(assignment):
    return assignment
  var = select_unassigned_variable(csp[VARIABLES], assignment)
  for value in csp[DOMAINS]:
    assignment[var] = value
    if is_consistent(assignment, csp[CONSTRAINTS]):
      result = recursive_backtracking(assignment, csp)
      if result != FAILURE:
        return result
    assignment[var] = None
  return FAILURE
  


counter = 0

def eqN(a, b): return a is not None and b is not None and a == b
def gt(a, b): return a is not None and b is not None and a < b 
def eq4(a): return a is not None and a == 4 
def eq6(a): return a is not None and a == 6
def eq7(a): return a is not None  and a == 7

def wa_nt(asmt): return eqN(asmt["Inter1"], asmt["High1"])
def wa_sa(asmt): return eqN(asmt["Inter1"], asmt["High2"])
def nt_sa(asmt): return eqN(asmt["Inter1"], asmt["High3"])
def nt_q(asmt): return eqN(asmt["Inter2"], asmt["High1"])
def sa_q(asmt): return eqN(asmt["Inter2"], asmt["High2"])
def sa_nsw(asmt): return eqN(asmt["Inter2"],asmt["High3"])
def sa_v(asmt): return eqN(asmt["Inter3"], asmt["High1"])
def q_nsw(asmt): return eqN(asmt["Inter3"], asmt["High2"])
def v_t(asmt): return eqN(asmt["Inter3"], asmt["High3"])

def H1I1(asmt): return eqN(asmt["High1"], asmt["Inter1"])
def H1I2(asmt): return eqN(asmt["High1"], asmt["Inter2"])
def H1I3(asmt): return eqN(asmt["High1"], asmt["Inter3"])
def H2I1(asmt): return eqN(asmt["High2"], asmt["Inter1"])
def H2I2(asmt): return eqN(asmt["High2"], asmt["Inter2"])
def H2I3(asmt): return eqN(asmt["High2"], asmt["Inter3"])
def H3I1(asmt): return eqN(asmt["High3"], asmt["Inter1"])
def H3I2(asmt): return eqN(asmt["High3"], asmt["Inter2"])
def H3I3(asmt): return eqN(asmt["High3"], asmt["Inter3"])

def I1(asmt): return eq4(asmt["Inter1"])
def I3(asmt): return eq6(asmt["Inter3"])
def H2(asmt): return eq7(asmt["High2"])


def I3I2(asmt):return eqN(asmt["Inter3"],asmt["Inter2"])
def I3tI2(asmt):return eqN(asmt["Inter1"],asmt["Inter2"])
def I1I3(asmt):return eqN(asmt["Inter1"],asmt["Inter3"])
def I2nI3(asmt):return eqN(asmt["Inter2"],asmt["Inter3"])

def H2H1(asmt): return eqN(asmt["High2"], asmt["High1"])
def H3H2(asmt): return eqN(asmt["High3"], asmt["High2"])
def H3H1(asmt): return eqN(asmt["High3"], asmt["High1"])

def I3I1(asmt): return gt(asmt["Inter3"], asmt["Inter1"])
def I2I1(asmt): return gt(asmt["Inter2"], asmt["Inter1"])
def I2gI3(asmt): return gt(asmt["Inter2"], asmt["Inter3"])
def I2I3(asmt): return gt(asmt["Inter2"], asmt["High1"])

my_csp = {VARIABLES: ["Inter1","Inter2","Inter3","High1", "High2","High3"],
          DOMAINS: [3,4,5,6,7,8],
          CONSTRAINTS: [wa_nt, wa_sa, nt_sa, nt_q, sa_q, sa_nsw, sa_v,
          q_nsw, v_t, H1I1, H1I2,H1I3,H2I1,H2I2,H2I3,H3I1,H3I2,H3I3,I1,I3,
          H2,I2I1,I2I3,I3I1,H2H1,H3H2,H3H1,I3I2,I1I3,I2gI3,I2nI3,I3tI2]}
          
         
start = time.time()        
result = recursive_backtracking(init_assignment(my_csp), my_csp)
[counter, result]
end=time.time()
dele=end-start
dele*=1000000

print("The Backtacing is :")
print(result)
print(counter)
print("the time is:",dele,"MicroSecond")

