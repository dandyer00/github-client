import requests
import json

class githubClient:
    
    def requestAndParse(self, url):
        r = requests.get(url)
        if(r.ok):
            self.repoInfo = json.loads(r.text or r.content)
            return self.repoInfo
    
    def getOrgRepoList(self, org):
        url = 'https://api.github.com/orgs/' + org + '/repos'
        return self.requestAndParse(url)
             
    def getUserRepoList(self, user):
        url = 'https://api.github.com/users/' + user + '/repos'
        return self.requestAndParse(url)
        
    def getRepoInfo(self, url):
        return self.requestAndParse(url)
    
    def getUserProfile(self, user):
        url = 'https://api.github.com/users/' + user
        return self.requestAndParse(url)
