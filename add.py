from app2.models import *
# for i in range(1,10):
#     user=UserInfo()
#     user.username='user'+str(i)
#     user.strength='18k'
#     user.description=''
#     user.email=''
#     user.password='123'
#     user.age=i+10
#     user.save()
for i in range(1,5):
    g=GameInfo()
    g.steps=range(1, i + 4)
    g.player1=UserInfo.objects.get(id=i)
    g.player2=UserInfo.objects.get(id=9-i)
    g.save()
