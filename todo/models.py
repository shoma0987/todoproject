from django.db import models

# 大抵models.Modelを継承してDBをスタートする
# そして必要なFieldを呼び出す
PRIORITY=(("danger","high"),("info","normal"),("success","low"))
class  TodoModel(models.Model):
    title = models.CharField(max_length = 100)
    memo = models.TextField()
    priority = models.CharField(max_length = 50, choices =PRIORITY )
    # TextFieldはCharFieldよりも長い文章を記述する時に使う
    duedate = models.DateField(null=True)
    # 

    #todo管理画面で生成された各オブジェクトの名前はtitleの名前を返すように設定
    def __str__(self):
        return self.title