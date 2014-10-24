# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Voting import ballot, candidate, election_set, election_solve

class VotingTests(TestCase):
  #------
  #ballot
  #------
  def test_ballot1(self):
    a = ballot([1,2,3])
    assert str(a) == str([1,2,3])
   
  def test_ballot2(self):
    a = ballot([1,2,3,4,5,6])
    a.index_up()
 
    assert a.vote() == 2
    
  def test_ballot3(self):
    a = ballot([1,2,3,4,5,6])
    a.set_index(5)
   
    assert a.vote() == 6
  
  #---------
  #candidate  
  #---------
  def test_candidate1(self):
    a = candidate('Adam')
    a.add_ballot(ballot())
      
    assert(a.vote_tot() == 1)
      
  def test_candidate2(self):
    a = candidate('Branfordington')
    a.add_ballot(ballot())
    a.add_ballot(ballot())
    a.add_ballot(ballot()) 
    
    assert(a.vote_tot() == 3)    
  
  def test_candidate3(self):
    a= candidate('Bashmanogan')
    assert(str(a) == 'Bashmanogan')
    
  def test_candidates4(self):
    a = candidate('Lando Calrissian')
    b = ballot([1])
    
    for i in range(5):
      a.add_ballot(b)

    for item in a.ballot_list():
      assert str(item) == str([1])
  
  #---
  #set
  #---  
  def test_election_set1(self):
    r = StringIO('3\nJohn Doe \n Jane Smith \n Sirhan Sirhan \n 1 2 3 \n 1 2 3 \n 2 1 3\n 2 3 1 \n 1 2 3 \n 3 1 2') 
    dict, lst = election_set(r)
    
    assert {1:candidate('John Doe'), 2: candidate('Jane Smith'), 3: candidate('Sirhan Sirhan')} == dict
    
  def test_election_set2(self):
    r = StringIO('1\n\n3\nJohn Doe\nJane Smith\nSirhan Sirhan\n1 2 3\n1 2 3\n2 1 3 \n 2 3 1\n 1 2 3 \n 3 1 2') 
    dict, lst =  election_set(r)
    
    assert [[1,2,3], [1,2,3], [2,1,3], [2,3,1], [1,2,3], [3,1,2]] == lst
  def test_election_set3(self):

    dict, lst = election_set(r)
    
    assert [[1],[1],[1],[1]] == lst 
    
  def test_election_set4(self):
    r = StringIO('1\n\n1\nLando PandaBears\n1\n1\n1\n1')
    dict,lst = election_set(r)
    
    assert {1: candidate('Lando PandaBears')} == dict 
    
   #-----
   #Solve
   #-----
  def test_electiion_aolve1(self):
    r = StringIO('1\n\n1\nLando PandaBears\n1\n1\n1\n1')
    w = StringIO()
    
    assert w.getvalue() == 'Lando PandaBears'
  def test_election_solve2(self):
    r = StringIO('1\n\n3\nJohn Doe \n Jane Smith \n Sirhan Sirhan \n 1 2 3 \n 1 2 3 \n 2 1 3\n 2 3 1 \n 1 2 3 \n 3 1 2')
    w = StringIO()
    
    assert w.getvalue() == 'John Doe'
  
  def test_election_solve3(self):
    r = StringIO('2\n\n3\nJohn Doe \n Jane Smith \n Sirhan Sirhan \n 1 2 3 \n 1 2 3 \n 2 1 3\n 2 3 1 \n 1 2 3 \n 3 1 2\n\n1\nLando PandaBears\n1\n1\n1\n1')
    w = StringIO()
    
    assert w.getvalue() == 'John Doe\n\nLando PandaBears'
    
    
    
    
   
#----
#main
#----
main()