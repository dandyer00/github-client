import requests
import json

class githubClient:
    
    def __init__(self, user, org):
        self.user = user
        self.org = org
        self.gitHubURL = 'https://api.github.com/'
        
    def requestAndParse(self, url):
        r = requests.get(url)
        if(r.ok):
            result = json.loads(r.text or r.content)
            return result
#=======================================================
#users             
    def getUserRepoList(self):
        url = self.gitHubURL + 'users/' + self.user + '/repos'
        return self.requestAndParse(url)
            
    def getUserProfile(self ):
        url = self.gitHubURL + 'users/' + self.user
        return self.requestAndParse(url)

    
#=======================================================
#orgs
    def getOrgRepoList(self):
        url = self.gitHubURL + 'orgs/' + self.org + '/repos'
        return self.requestAndParse(url)

#================================================
#repos
    def getRepoInfo(self, owner, repo):
        url = self.gitHubURL + 'repos/' + owner + '/' + repo
        return self.requestAndParse(url)

    def getRepoIssues(self, owner, repo):
        url = self.gitHubURL + 'repos/' + owner + '/' + repo + '/issues'
        return self.requestAndParse(url)    

    def getAllRepoEvents(self, owner, repo):
        url = self.gitHubURL + 'repos/' + owner + '/' + repo + '/events'
        return self.requestAndParse(url)