import requests
import json

class githubClient:
    
    def __init__(self, user):
        self.user = user
        self.gitHubURL = 'https://api.github.com/'
        
    def requestAndParse(self, url):
        r = requests.get(url)
        if(r.ok):
            self.repoInfo = json.loads(r.text or r.content)
            return self.repoInfo
    
    def getOrgRepoList(self, org):
        url = self.gitHubURL + 'orgs/' + org + '/repos'
        return self.requestAndParse(url)
             
    def getUserRepoList(self):
        url = self.gitHubURL + 'users/' + self.user + '/repos'
        return self.requestAndParse(url)
        
    def getRepoInfo(self, repo):
        url = self.gitHubURL + 'repos/' + self.user + '/' + repo
        return self.requestAndParse(url)
    
    def getUserProfile(self ):
        url = self.gitHubURL + 'users/' + self.user
        return self.requestAndParse(url)

    def getRepoIssues(self, repo):
        url = self.gitHubURL + 'repos/' + self.user + '/' + repo + '/issues/'
        return self.requestAndParse(url)