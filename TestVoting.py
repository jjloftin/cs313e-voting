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
    a = ballot([1])
    assert str(a) == str([1])
  def test_ballot3(self):
    a = ballot([])
    assert str(a) == str([])
    
  def test_ballot4(self):
    a = ballot([1,2,3,4,5,6])
    a.index_up()
    assert a.vote() == 2
  def test_ballot5(self):
    a = ballot([1,2,3])
    a.index_up()
    a.index_up()
    assert a.vote() == 3
  def tests_ballot6(self):
    a = ballot()
    assert a.vote() == 0 
    
  def test_ballot7(self):
    a = ballot([1,2,3,4,5,6])
    a.index_up()
    assert a.index == 1
  def test_ballot8(self):
    a = ballot([1,2,3])
    a.index_up()
    a.index_up()
    assert a.index == 2
  def tests_ballot9(self):
    a = ballot([1,2,3,4,5,6])
    a.index_up()
    a.index_up()
    a.index_up()
    a.index_up()
    assert a.index == 4
    
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
    a = candidate('Snoopy')
    assert(a.vote_tot() == 0)    
  
  def test_candidate4(self):
    a= candidate('Bashmanogan')
    assert(str(a) == 'Bashmanogan')
  def test_candidate5(self):
    a = candidate(9)
    assert(str(a) == '9')
  def test_candidate6(self):
    a = candidate([])
    assert(str(a) == '[]')
    
  def test_candidate7(self):
    a = candidate('Lando Calrissiam')
    b = ballot([1])
    for i in range(5):
      a.add_ballot(b)
    for item in a.ballot_list():
      assert str(item) == str([1])
  def test_candidate8(self):  
    a = candidate('m')
    b = [ballot([1,2,3]),ballot([2,1,3]),ballot([2,1,4])]
    for i in range(3):
      a.add_ballot(b[i])
    for i in range(len(a.ballot_list())):
      assert str(b[i]) == str(a.ballot_list()[i])
  def test_candidate9(self):
    a = candidate('Lock')
    str(a.ballot_list()) == str([])   
    
  #---
  #set
  #---  
  def test_election_set1(self):
    r = StringIO('3\nJohn Doe \n Jane Smith \n Sirhan Sirhan \n 1 2 3 \n 1 2 3 \n 2 1 3\n 2 3 1 \n 1 2 3 \n 3 1 2') 
    dict, lst = election_set(r)
    
    assert(str(dict[1]) == 'John Doe')
    assert(str(dict[2]) == 'Jane Smith')
    assert(str(dict[3]) == 'Sirhan Sirhan')
    
  def test_election_set2(self):
    r = StringIO('3\nJohn Doe\nJane Smith\nSirhan Sirhan\n1 2 3\n1 2 3\n2 1 3 \n 2 3 1\n 1 2 3 \n 3 1 2') 
    dict, lst =  election_set(r)
    a = zip(lst,[[1,2,3], [1,2,3], [2,1,3], [2,3,1], [1,2,3], [3,1,2]])
    for u, v in a:
      assert(str(u) == str(v))
    assert True
    
  def test_election_set3(self):
    r = StringIO('1\nLando PandaBears\n1\n1\n1\n1')
    dict, lst = election_set(r)
    for object in lst:
      assert str(object) == str([1])
    assert True
    
  def test_election_set4(self):
    r = StringIO('1\nLando PandaBears\n1\n1\n1\n1')
    dict,lst = election_set(r)
    
    assert 'Lando PandaBears' == str(dict[1]) 
    
   #-----
   #Solve
   #-----
  def test_electiion_aolve1(self):
    r = StringIO('1\n\n1\nLando PandaBears\n1\n1\n1\n1')
    w = StringIO()
    election_solve(r,w)
    
    assert w.getvalue() == 'Lando PandaBears'
  def test_election_solve2(self):
    r = StringIO('1\n\n3\nJohn Doe\nJane\nSirhan\n1 2 3\n 2 1 3\n 2 3 1\n 1 2 3\n 3 1 2\n')
    w = StringIO()
    election_solve(r,w)
    
    assert w.getvalue() == 'John Doe'
  def test_election_solve3(self):
    r = StringIO('2\n\n3\nJohn Doe\nJane\nSirhan\n1 2 3\n 2 1 3\n 2 3 1\n 1 2 3\n 3 1 2\n\n1\nLando PandaBears\n1\n1\n1\n1')
    w = StringIO()
   
    election_solve(r,w)
    
    assert w.getvalue() == 'John Doe\n\nLando PandaBears'
    
    
    
    
   
#----
#main
#----
main()