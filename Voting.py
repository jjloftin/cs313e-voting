#VotingPy#
#-------------
#Ballot(Class)
#-------------
#ballot class. Holds the preferences of each voter. Can be altered to remove losing 
#candidates
class ballot :
  def __init__(self, list =[0]):
    self.votes = list
    self.index = 0
  #allows index to be moved up by one
  def index_up(self):
    assert self.index < len(self.votes) - 1
    self.index += 1
  def set_index(self, n):
    assert n < len(self.votes) 
    assert type(n) == int    
    self.index = n
    
  def vote(self):
    return self.votes[self.index]
  def index(self):
    return self.index
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
    self.ballot_list = [] 
    
  def vote_for (self, newBallot):
    type(newBallot) is ballot
    self.votes += 1
    self.ballot_list.append(newBallot)
  def vote_tot(self):
    return self.votes
  def ballot_list(self):
    return self.ballot_list
  def __str__(self):
    return str(self.name)

#-------------
#election_set
#-------------
#Sets up the parameters of the election. Creates a dictionary of candidates and
#their assigned number and creates a list of ballots

def election_set(r):
  
  return {}, []

#------------
#election_run
#------------
#Run an austrlian style election returns the name of the winning candidate or 
#tied candidates

def election_solve(r,w):
  
  w.write('')

  

