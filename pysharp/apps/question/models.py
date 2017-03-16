from django.db import models
from utils.string_extension import get_uuid

# Create your models here.

QUESTION_MODE = (
    ('free', '免费提问'),
    ('push', '付费提问'),
    ('onetoone', '一对一提问')
)


class AppQuestions(models.Model):
    pk_question = models.CharField('问答id', primary_key=True, default=get_uuid(), max_length=40)
    pk_user = models.CharField('用户id', max_length=40, blank=True, null=True)
    content = models.TextField('提问内容', null=True)
    questionmode = models.CharField('提问方式', choices=QUESTION_MODE, max_length=20, null=True)
    questionrelate = models.CharField('提问相关', max_length=20, blank=True, null=True)
    pk_respondent = models.CharField('回复者id', max_length=40, blank=True, null=True)
    listennum = models.IntegerField('偷听人数', null=True, default=0)
    isopen = models.NullBooleanField('是否公开', null=True)
    iscommented = models.NullBooleanField('是否已评论', blank=True, null=True)
    question_price = models.DecimalField('提问价格', max_digits=18, decimal_places=4, null=True)
    listen_price = models.DecimalField('偷听价格', max_digits=18, decimal_places=4, null=True)
    isaudited = models.NullBooleanField('是否审核', null=True)
    goodnum = models.IntegerField('点赞数', null=True, default=0)
    commentnum = models.IntegerField('评论数', null=True, default=0)
    status = models.IntegerField('状态', blank=True, null=True)
    re_status = models.IntegerField('状态', blank=True, null=True)
    createtime = models.DateTimeField('创建时间', blank=True, null=True, auto_now_add=True)
    re_createtime = models.DateTimeField('追问创建时间', blank=True, null=True)
    race_endtime = models.DateTimeField('悬赏结束时间', blank=True, null=True)
    opentime = models.DateTimeField('公开时间', blank=True, null=True)
    updatetime = models.DateTimeField('更新时间', blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'app_questions'
        verbose_name = '提问'
        verbose_name_plural = '提问列表'

    def __str__(self):
        return self.content


class AppAnswers(models.Model):
    pk_answer = models.CharField('回答id', primary_key=True, default=get_uuid(), max_length=40)
    pk_question = models.CharField('提问id', max_length=40, blank=True, null=True)
    pk_user = models.CharField('用户id', max_length=40, blank=True, null=True)
    voice = models.CharField('音频路径', max_length=200, blank=True, null=True)
    duration = models.IntegerField('时长', blank=True, null=True)
    picture = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField('文本内容', blank=True, null=True)
    isbest = models.NullBooleanField('是否最佳', null=True)
    createtime = models.DateTimeField('创建时间', blank=True, auto_now_add=True, null=True)
    updatetime = models.DateTimeField('更新时间', blank=True, auto_now=True, null=True)

    class Meta:
        db_table = 'app_answers'
        verbose_name = '回答'
        verbose_name_plural = '回答列表'


class AppListens(models.Model):
    pk_listen = models.CharField('id', primary_key=True, default=get_uuid(), max_length=40)
    pk_question = models.CharField('提问id', max_length=40, blank=True, null=True)
    pk_respondent=models.CharField('回答者',max_length=40, blank=True, null=True)
    pk_user = models.CharField('用户', max_length=40, blank=True, null=True)
    iscommented = models.NullBooleanField('是否已评论', null=True)
    ispaid = models.NullBooleanField('是否已支付', null=True)
    createtime = models.DateTimeField('创建时间', auto_now_add=True, blank=True, null=True)
    upatetime = models.DateTimeField('更新时间', auto_now_add=True, blank=True, null=True)

    class Meta:
        db_table = 'app_listens'
        verbose_name = '偷听'
        verbose_name_plural = '偷听列表'


class AppQuestionComments(models.Model):
    pk_comment = models.CharField(primary_key=True, default=get_uuid(), max_length=40)
    pk_question = models.CharField(max_length=40, blank=True, null=True)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'app_question_comments'


class AppQuestionGoods(models.Model):
    pk_key = models.CharField(primary_key=True, default=get_uuid(), max_length=40)
    pk_question = models.CharField(max_length=40, blank=True, null=True)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'app_question_goods'