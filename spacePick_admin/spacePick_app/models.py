from django.db import models
from django.utils import timezone
import uuid

class Users(models.Model):
  user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  user_name = models.CharField(verbose_name='ユーザー名', max_length=20)
  delete_flg = models.BooleanField(verbose_name='論理削除', default=False)
  created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)
  updated_at = models.DateTimeField(verbose_name='更新日時', blank=True, null=True)

  def __str__(self):
    return self.user_name

class Apod(models.Model):
  apod_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(verbose_name='APODタイトル', max_length=255)
  explanation = models.TextField(verbose_name='APOD説明', blank=True)
  date = models.DateField(verbose_name='APODリクエスト日')
  url = models.URLField(verbose_name='APODURL', blank=True)
  delete_flg = models.BooleanField(verbose_name='論理削除', default=False)
  created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)
  updated_at = models.DateTimeField(verbose_name='更新日時', blank=True, null=True)

  def __str__(self):
    return self.title

class Likes(models.Model):
  like_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  user_id = models.ForeignKey("Users", verbose_name='ユーザーID', on_delete=models.CASCADE)
  apod_id = models.ForeignKey("Apod", verbose_name='APODID', on_delete=models.CASCADE)
  delete_flg = models.BooleanField(verbose_name='論理削除', default=False)
  created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)
  updated_at = models.DateTimeField(verbose_name='更新日時', blank=True, null=True)

class Apod_vote(models.Model):
  apod_vote_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  user_id = models.ForeignKey("Users", verbose_name='ユーザーID', on_delete=models.CASCADE)
  apod_id = models.ForeignKey("Apod", verbose_name='APODID', on_delete=models.CASCADE)
  vote_flg = models.BooleanField(verbose_name='投票フラグ', default=False)
  vote_date = models.DateTimeField(verbose_name='投票日時')
  created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)
  updated_at = models.DateTimeField(verbose_name='更新日時', blank=True, null=True)