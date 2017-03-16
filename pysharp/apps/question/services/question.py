# coding:utf-8
from question.models import AppQuestions


class QuestionService:
    def get_questions(self):
        questionDtos = AppQuestions.objects.raw(
            """
           select * from(select q.pk_question as questionid, q.pk_user as userid, content, re_content, questionmode, questionrelate, listennum, isaudited, isopen, iscommented, question_price, listen_price, goodnum, status, re_status, q.createtime as question_createtime, re_createtime as question_re_createtime, updatetime as question_updatetime, commentnum,opentime as question_opentime,race_endtime as question_race_endtime,
            t. * from app_questions as q
            left join  (select  pk_answer as answerid, pk_question, pk_user as respondentid, voice, duration, picture, content as text, is_reanswered, createtime as anwser_createtime, ROW_NUMBER()
            over(partition  by pk_question  order  by createtime desc) as rows from app_answers where (is_reanswered is null or is_reanswered = 0)) as t
            on q.pk_question = t.pk_question where exists(select * from app_answers as a
            where q.pk_question = a.pk_question and isaudited = 1 and opentime is not null and isopen is not null and status != 0) and rows = 1 ) as question
            """
        )

        return questionDtos
