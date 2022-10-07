from GitHubApi import ListRepo, NumCommits

def runSelfTest():
    ID = input("Input user ID to check repos\n")
    print(ListRepo(ID))
    REPO = input("Input a Repo from the same user to check num commits of that repo\n")
    print(NumCommits(ID, REPO))

def runSelfTestNumCommitsOnly():
    ID = input("Input user ID to check repos\n")
    REPO = input("Input a Repo from the same user to check num commits of that repo\n")
    print(NumCommits(ID, REPO))

def runSelfTestListRepoOnly():
    ID = input("Input user ID to check repos\n")
    print(ListRepo(ID))

runSelfTest()