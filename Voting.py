#!/usr/bin/env python3

# ---------------------------
# Voting.py
# Copyright (C) 2014
# John Loftin
# ---------------------------

#-------------
#Ballot(Class)
#-------------

class ballot :
  """
  Ballot class. Holds the preferences of each voter. Can be altered to remove losing candidates by changing index of ballot (initially set to 0)
  """
  def __init__(self, list =[0]):
    """
    Construct a new ballot.
    Data members - votes(list), index(int)
    """
    self.votes = list
    self.index = 0
  def index_up(self):
    """
    Move index up by one. Changes who candidate is voting for
    """
    self.index += 1
  def vote(self):
    """
    Returns who voter is voting for as an index.
    """
    return self.votes[self.index]
  def __str__(self):    
    """
    Return a string of ballot - just a string version of the list of votes
    """   
    return str(self.votes)

#----------------
#Candidate(Class)
#----------------

class candidate :
  """
  Candidate class. Contains a name, number of votes, and a list of sthe ballots of people voting for
  them
  Data members - name(can take in anything, will always output a string), votes(int), ballots(list - instances of ballot)s
  """
  def __init__(self, name, votes = 0):
    """
    Construct a new candidate
    """
    self.name = name
    self.votes = votes
    self.ballots = [] 
    
  def vote_tot(self):
    """
    return number of votes
    """
    return self.votes
    
  def ballot_list(self):
    """
    Return list of ballots attached to each candidate
    """  
    return self.ballots
    
  def add_ballot(self,ballot):
    """
    Add a new ballot to candidate. Increases total votes by 1
    """
    type(ballot) is ballot
    self.votes += 1
    self.ballots.append(ballot)
    
  def __str__(self):
    """
    Returns String of Candidate - Candidate Name.
    """
    return str(self.name)
#-------------
#election_set
#-------------
def election_set(r):
  """
  Reads in from reader (r) to set up the parameters of the election. Creates a dictionary of candidates without ballots and
  their assigned number and creates a list of ballots
  """
  numCandidates = int(r.readline())
  candidate_dict = {}
  all_ballots = []
  for i in range(1,numCandidates + 1):
    candidate_dict[i] = candidate(r.readline().strip())
  
  while True:
    s = r.readline().strip()
   
    if not s:
      break
    else:
      s = s.split()
      t = []
      
      for item in s:
        t.append(int(item))
      b = ballot(t)
      all_ballots.append(b)     
 
  return candidate_dict, all_ballots
 
#------------
#election_run
#------------


def election_solve(r,w):
  """
  Run an austrlian style election. Reads in input from a reader(r) and writes to writer (w) the name of the winning candidate or 
  tied candidates
  """
  num_elections = int(r.readline())
  r.readline()
  j = 0
  
  while(j < num_elections):
    if(j != 0):
      w.write('\n\n')
    j += 1
    
    candidate_dict, all_ballots = election_set(r)
    #run the election according to Australian Voting rules
    #count the initial votes
    
    
    num_votes = len(all_ballots)
    
    for ballot in all_ballots:
      vote = ballot.vote()
      candidate_dict[vote].add_ballot(ballot)

    #keep track of eliminateted candidates    
    eliminated = []
   
    while True:
      max = 0
      winner = None
      min = num_votes + 1
      loser = []
      
      for i in range(1,len(candidate_dict) + 1):
        #ignore eliminated candidates
        if i in eliminated:
          continue
      
        candidate = candidate_dict[i]
        votes = candidate.vote_tot()
        assert type(votes) is int
        
        #note that the first candidate is initially both the loser and the winner. This
        #will either stay the same in the case of a tie/single candidate or will be fixed
        if(votes >= max):
          winner = candidate
          max = votes
        if(votes < min):
          loser = [candidate]
          min = votes
        elif(votes == min):
          loser.append(candidate)
         
      #determine if a tie or if only one candidate
      if(max == min):        
        for i in range(len(loser)-1):
            w.write(str(loser[i]) + '\n')
        w.write(str(loser[-1]))
        break    
      #detrmine if winner 
      if(max / num_votes > 0.5):
        w.write(str(winner))    
        break
      #if not a tie or a winner reassign the votes of the losing candidates
      for i in candidate_dict:
        if(candidate_dict[i] in loser):
          eliminated.append(i)
      
      #run through losing candidates ballots, find first vote in each ballot
      #for non losing candidates
      #we note here: THIS DOES NOT INDEX THROUGH ALL BALLOTS
      for candidate in loser:
        for ballot in candidate.ballot_list():
          while(ballot.vote() in eliminated):
            ballot.index_up()     
          candidate_dict[ballot.vote()].add_ballot(ballot)      
      
    
      
        
  

