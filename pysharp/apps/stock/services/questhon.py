# coding:utf-8
from pvplus_common.serviceresult import RuleViolation, ServiceResult
from pvplus_model.models.question import AppQuestions
from pvplus_webapi.services.user_service import UserService


class QuestionService:
    def create_question(self, userid, content, questionmode, questionrelate, respondentid, question_price):
        '''创建提问'''
        result = ServiceResult()

        user = UserService().get_user(userid)
        if not user:
            result.ruleviolations.append(RuleViolation('userid', '用户不存在'))
            return result

        # 提问价格
        questionmode_price = {'free': 0, 'push': question_price, 'onetoone': user.price}
        price = questionmode_price.get(questionmode, '')

        question = AppQuestions(pk_user=userid,
                                content=content,
                                questionmode=questionmode,
                                questionrelate=questionrelate,
                                pk_respondent=respondentid,
                                question_price=price,
                                isaudited=True
                                )
        question.save(force_insert=True)
        result.data = question.pk_question

        return result
