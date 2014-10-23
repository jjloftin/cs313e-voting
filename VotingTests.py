# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Voting import ballot, candidate, election_set_up, election_run

class VotingTests(TestCase):
  def test_ballot1(self):
    a = ballot()
    a.add([1,2,3])
    print(a)
    assert(str(a)) == str([1,2,3])
    
  def test_ballot2(self):
    a = ballot()
    a.add([1,2,3])
    print(a)
    a.remove()
    assert(str(a)) == str([2,3])
   
  def test_ballot3(self):
    a = ballot()
    a.add([1,2,3])
    a.remove()
    a.add([4,5,6])
    print(a)
    assert(str(a)) == str([2,3,4,5,6])
    
  def test_candidate1(self):
    a = candidate('Adam')
    a.voteFor(ballot())
      
    assert(a.voteTot() == 1)
      
  def test_candidate2(self):
    a = candidate('Branfordington')
    a.voteFor(ballot())
    a.voteFor(ballot())
    a.voteFor(ballot()) 
    
    assert(a.voteTot() == 3)    
  
  def test_candidate3(self):
    a= candidate('Bashmanogan')
    assert(str(a) == 'Bashmanogan')
    
#----
#main
#----
main()