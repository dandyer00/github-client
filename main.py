
import clients

if __name__ == '__main__':
    user =  'dandyer00'   
    repo = 'github-client'
    org = 'SUSE'

    g = clients.githubClient(user)
      
#     d= g.getRepoInfo(repo)
#     print "RepoInfo for %s/%s" % (user, repo)
#     for k in d:
#         print '%s: %s' % (k, d[k])
#     
#     print '\nUser Profile for %s' % user
#     d = g.getUserProfile()
#     for k in d:
#         print '%s: %s' % (k, d[k])    
#         
#     print '\nRepos for %s' % user
#     l = g.getUserRepoList()
#     for d in l:
#         for k in d:
#             print '%s: %s' % (k, d[k])    
# 
#     print '\nRepos for %s' % org
#     l = g.getOrgRepoList(org)
#     for d in l:
#         for k in d:
#             print '%s: %s' % (k, d[k])        
            
    print '\n Issues for %s/%s' % (user, repo)
    l = g.getRepoIssues(repo)
    for d in l:
        for k in d:
            print '%s: %s' % (k, d[k])        
    