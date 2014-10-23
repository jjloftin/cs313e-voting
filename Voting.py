#VotingPy#
#-------------
#Ballot(Class)
#-------------
#ballot class. Holds the preferences of each voter. Can be altered to remove losing 
#candidates
class ballot :
  def __init__(self):
    self.votes = []
  def add(self, lst):
    self.votes += lst
  def remove(self):
    self.votes = self.votes[1:]
  def __str__(self):    
    return str(self.votes)
#----------------
#Candidate(Class)
#----------------
#candidate contains a name, number of votes, and the ballots of people voting for
#them
class candidate :
  def __init__(self, name, votes = 0):
    self.name = name
    self.votes = votes
    self.ballotList = [] 
  def voteFor (self, newBallot):
    type(newBallot) is ballot
    self.votes += 1
    self.ballotList.append(newBallot)
  def voteTot(self):
    return self.votes
  def ballotList(self):
    return self.ballotList
  def __str__(self):
    return str(self.name)

#---------------
#election_set_up
#---------------
#Sets up the parameters of the election. Creates a dictionary of candidates and
#their assigned number and creates a list of ballots

def election_set_up(r,w):
  
  return {}, []

#------------
#election_run
#------------
#Run an austrlian style election returns the name of the winning candidate or 
#tied candidates

def election_run(r,w):
  
  w.write('')

a = candidate('e')
print(a)
b = ballot()
print(b)
b.add([1,2,3])
print(b)
b.remove()
print(b)
print(type(ballot()) is ballot)