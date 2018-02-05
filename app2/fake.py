# -*- coding: utf-8 -*-
import random



def fakeUserHomeInfo(req):
    context = {'username': 'user1', 'userInfo': 'this is userInfo', 'online_user_list': ['user1', 'user2'], }
    return context

def fakeGameInfo(req):

    context = {'from_user': req.GET['from'], 'to_user': req.GET.get('to')}
    return context

def fakeUserlist(req):
    userlist = ['不是ajax']
    if req.is_ajax():
        tmp = random.sample(range(1, 100), 3)
        userlist = ['user' + str(tmp[0]), 'user' + str(tmp[1]), 'user' + str(tmp[2])]
        # return HttpResponse(content=json.dumps(userlist), content_type='application/json')
    content = {'userlist': userlist}
    return content

def fakeInvitation(req):
    content = {'invitation_from':'user'+str(random.randint(1,100))}
    return content