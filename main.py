
import clients

if __name__ == '__main__':
    g = clients.githubClient()
    
    url = 'https://api.github.com/repos/dandyer00/test1'
    d= g.getRepoInfo(url)
    print "RepoInfo for %s" % url
    for k in d:
        print '%s: %s' % (k, d[k])
    
    user =  'dandyer00'   
    print '\nUser Profile for %s' % user
    d = g.getUserProfile(user)
    for k in d:
        print '%s: %s' % (k, d[k])    
        
    print '\nRepos for %s' % user
    l = g.getUserRepoList(user)
    for d in l:
        for k in d:
            print '%s: %s' % (k, d[k])    

    org = 'SUSE'
    print '\nRepos for %s' % org
    l = g.getOrgRepoList(org)
    for d in l:
        for k in d:
            print '%s: %s' % (k, d[k])        