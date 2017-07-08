#Created on Tue Jun 13 12:11:11 2017
#@author: Ultimate Pro
#See twitter activity after airing of TV show
#from politician and non-politician accounts


##Variables that contains the user credentials to access Twitter API 
access_token = "Use Yours"
access_token_secret = "Use Yours"
consumer_key = "Use Yours"
consumer_secret = "Use Yours"

import twitter

api = twitter.Api(consumer_key,consumer_secret,access_token,access_token_secret)

'''friends = api.GetFriends()
for f in friends:
    print(f.name+","+str(f.id)+","+f.screen_name)

#statuses = api.GetUserTimeline(970207298,count=200)
statuses = api.GetHomeTimeline(count=200)
print(len(statuses))
for s in statuses:
    print(s.text+"\n")
#print(twitter.Api().GetUserTimeline(screen_name='AtheistRepublic'))


cspanLists = api.GetLists(screen_name='cspan')
congressListID = 0
for lst in cspanLists:
    if(lst.full_name == '@cspan/members-of-congress'):
        congressListID = lst.id
        
membersOfCongress = api.GetListMembers(congressListID)
for moc in membersOfCongress:
    print(moc)
    #print(moc.screen_name+", ID: "+str(moc.id))

myRTs = api.GetRetweetsOfMe(count=100)
for rt in myRTs:
    print(rt.text+"\n")
    

termName = ' #IslamsNonBelievers'
isNoB= api.GetSearch(term=termName)
#print(len('IfAlcoholDidntExist'))
#print(len('IslamsNonBelievers'))

for s in isNoB:
    print(s.text+" - "+ s.user.screen_name+","+s.user.name+"\n")
    
#print(api.GetTrendsCurrent())
'''
userTimeLine = api.GetUserTimeline(screen_name='ikhlasikhan1993',
                                   count='200',
                                   include_rts=True)
for tweets in userTimeLine:
    txt = tweets.text
    if "punish" in txt:
        print(txt+"\n")
    if "kill" in txt:
        print(txt+"\n")