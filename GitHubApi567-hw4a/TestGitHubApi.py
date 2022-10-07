import unittest
from GitHubApi import ListRepo, NumCommits

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testListRepo(self): 
        self.assertEqual(ListRepo('richkempinski'),['csp', 'hellogitworld', 'helloworld', 'Mocks', 'Project1', 'richkempinski.github.io', 'threads-of-life', 'try_nbdev', 'try_nbdev2'],'Should show 9 repos')
    def testNumCommits(self): 
        self.assertEqual(NumCommits('richkempinski', 'hellogitworld'), 30, 'Should be 30')
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
