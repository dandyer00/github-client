
import clients

if __name__ == '__main__':
    user =  'dandyer00'   
    repo = 'github-client'
    org = 'SUSE'

    g = clients.githubClient(user, org)
      
     
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
#         print '\n'
#  
#     print '\nRepoInfo for %s/%s' % (user, repo)
#     d= g.getRepoInfo(user, repo)
#     print "RepoInfo for %s/%s" % (user, repo)
#     for k in d:
#         print '%s: %s' % (k, d[k])
#            
#     print '\n Issues for %s/%s' % (user, repo)
#     l = g.getRepoIssues(user, repo)
#     for d in l:
#         for k in d:
#             print '%s: %s' % (k, d[k])        
#         print '\n'
#      
#     print '\n Events for %s/%s\n' % (user, repo)
#     l = g.getAllRepoEvents(user, repo)
#     for d in l:
#         for k in d:
#             print '%s: %s' % (k, d[k])
#         print '\n'        

#by org
    repo = 'auditlog-keeper'    
       
    print '\nRepos for %s' % org
    l = g.getOrgRepoList()
    for d in l:
        for k in d:
            print '%s: %s' % (k, d[k])        
        print '\n'

    print '\nRepoInfo for %s/%s' % (org, repo)
    d= g.getRepoInfo(org, repo)
    print "RepoInfo for %s/%s" % (org, repo)
    for k in d:
        print '%s: %s' % (k, d[k])
    
    print '\n Events for %s/%s\n' % (org, repo)
    l = g.getAllRepoEvents(org, repo)
    for d in l:
        for k in d:
            print '%s: %s' % (k, d[k])
        print '\n'    
        
    print '\n Issues for %s/%s\n' % (org, repo)
    l = g.getRepoIssues(org, repo)
    for d in l:
        for k in d:
            print '%s: %s' % (k, d[k])
        print '\n'  