from experta import *
from typing import List, Optional, Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging


class DevelopmentMilestone(Fact):
    """Fact to check if developmental milestones are missed or unusual behaviors are shown"""
    pass

class SocialBehavior(Fact):
    """Fact to check if there are social deficits or repetitive behaviors"""
    pass

class AcademicDifficulties(Fact):
    """Fact to check if there are academic difficulties"""
    pass

class AffectedArea(Fact):
    """Fact to identify affected academic skill area"""
    pass

class SeverityAssessment(Fact):
    """Fact to determine the severity of intellectual disability"""
    pass

class AutismAssessment(Fact):
    """Fact to determine the likelihood of ASD"""
    pass

class SLDReading(Fact):
    """Fact to assess specific learning disorder in reading"""
    pass

class SLDWriting(Fact):
    """Fact to assess specific learning disorder in writing"""
    pass

class SLDMathematics(Fact):
    """Fact to assess specific learning disorder in mathematics"""
    pass

class Question(Fact):
    """Fact to represent a question"""
    pass

class Answer(Fact):
    """Fact to represent an answer"""
    pass


# Define FastAPI input models
class UserResponse(BaseModel):
    answer: str

class QuestionModel(BaseModel):
    question_id: str
    question: str
    type: str
    valid: Optional[List[str]] = None

class RecommendationModel(BaseModel):
    recommendation: str


class MentalHealthExpertSystem(KnowledgeEngine):

    @DefFacts()
    def init(self):
        yield Question(ident="developmental", text="هل لديك تخلف عن معالم التطور أو أنك تظهر سلوكيات غير معتادة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="developmental", text="هل لديك سلوكيات غير معتادة؟", valid=["نعم", "لا"], Type="multi")

        yield Question(ident="social", text="هل لوحظت عيوب اجتماعية أو سلوكيات متكررة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="academic", text="هل تواجه صعوبة في المواد الأكاديمية مثل القراءة أو الرياضيات، وهل يؤثر ذلك على قدرتك على تلبية التوقعات المتعلقة بالعمر؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="reading", text="هل تعاني صعوبات في القراءة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="writing", text="هل تعاني من صعوبات في الكتابة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="math", text="هل تعاني صعوبات في الرياضيات؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="social_interactions", text="هل لديك مشاكل في التفاعلات الاجتماعية؟", valid=["نعم", "لا"], Type="multi")

    def __init__(self):
        super().__init__()
        self.questions = []
        self.recommendations = []
        self.current_question_id = None

    def recommend_action(self, action):
        self.recommendations.append(action)

    def ask_user(self, question, Type, valid=None):
        self.questions.append({
            "question_id": question["ident"],
            "question": question["text"],
            "type": Type,
            "valid": valid
        })

    def is_of_type(self, answer, Type, valid):
        if Type == "multi":
            return answer in valid
        if Type == "number":
            return answer.isdigit()
        return len(answer) > 0

    @Rule(Question(ident=MATCH.id, text=MATCH.text, valid=MATCH.valid, Type=MATCH.Type),
          NOT(Answer(ident=MATCH.id)),
          AS.ask << Fact(ask=MATCH.id))
    def ask_question(self, ask, id, text, valid, Type):
        self.retract(ask)
        self.ask_user({"ident": id, "text": text}, Type, valid)

    @Rule(NOT(Answer(ident="developmental")),
          NOT(Fact(ask="developmental")))
    def ask_developmental(self):
        self.declare(Fact(ask="developmental"))

    @Rule(Answer(ident="developmental", text="نعم"))
    def handle_developmental_yes(self):
        self.declare(SeverityAssessment(needed=True))
        self.declare(Fact(ask="academic_challenges"))

    @Rule(Answer(ident="developmental", text="لا"),
          NOT(Answer(ident="social")),
          NOT(Fact(ask="social")))
    def ask_social(self):
        self.declare(Fact(ask="social"))

    @Rule(Answer(ident="social", text="نعم"))
    def handle_social_yes(self):
        self.declare(AutismAssessment(needed=True))
        self.declare(Fact(ask="social_interactions"))

    @Rule(Answer(ident="social", text="لا"),
          NOT(Answer(ident="academic")),
          NOT(Fact(ask="academic")))
    def ask_academic(self):
        self.declare(Fact(ask="academic"))

    @Rule(Answer(ident="academic", text="نعم"))
    def handle_academic_yes(self):
        self.declare(AffectedArea(identified=True))
        self.declare(Fact(ask="reading"))
        self.declare(Fact(ask="writing"))
        self.declare(Fact(ask="math"))

    @Rule(AffectedArea(identified=True), Answer(ident="reading", text="نعم"))
    def handle_reading_yes(self):
        self.declare(SLDReading(needed=True))
        self.declare(Fact(ask="reading_accuracy"))

    @Rule(AffectedArea(identified=True), Answer(ident="writing", text="نعم"))
    def handle_writing_yes(self):
        self.declare(SLDWriting(needed=True))
        self.declare(Fact(ask="writing_grammar"))

    @Rule(AffectedArea(identified=True), Answer(ident="math", text="نعم"))
    def handle_math_yes(self):
        self.declare(SLDMathematics(needed=True))
        self.declare(Fact(ask="math_understanding"))

    @Rule(Answer(ident="reading", text="لا"), Answer(ident="writing", text="لا"), Answer(ident="math", text="لا"))
    def no_sld_identified(self):
        self.recommend_action("لم يتم تشخيص اضطراب تعلم محدد")
        self.halt()

    @Rule(Answer(ident="academic", text="لا"))
    def handle_academic_no(self):
        self.recommend_action("لم يتم تحديد أي عيوب مفاهيمية كبيرة")
        self.halt()

    @Rule(Fact(ask="academic_challenges"),
          NOT(Answer(ident="academic_challenges")))
    def ask_academic_challenges(self):
        self.declare(Question(ident="academic_challenges", text="هل لديك صعوبة في المواد الدراسية مثل القراءة أو الرياضيات، وهل يؤثر هذا على قدرته على تلبية توقعات العمر؟", valid=["نعم", "لا"], Type="multi"))

    @Rule(Answer(ident="academic_challenges", text="نعم"))
    def handle_academic_challenges_yes(self):
        self.declare(Fact(ask="word_reading"))

    @Rule(Answer(ident="academic_challenges", text="لا"))
    def handle_academic_challenges_no(self):
        self.recommend_action("لا يوجد عجز مفاهيمي كبير.")
        self.halt()

    @Rule(Fact(ask="word_reading"),
          NOT(Answer(ident="word_reading")))
    def ask_word_reading(self):
        self.declare(Question(ident="word_reading", text="هل تعاني من صعوبة في القراءة الدقيقة أو البطيئة والمجهدة؟", valid=["نعم", "لا"], Type="multi"))

    @Rule(Answer(ident="word_reading", text="نعم"))
    def handle_word_reading_yes(self):
        self.recommend_action("تقييم الصعوبات في:\n1. دقة القراءة\n2. معدل أو طلاقة القراءة\n3. فهم القراءة")
        self.recommend_action("الحاجة إلى دعم في مهارات القراءة")

    @Rule(Fact(ask="reading_comprehension"),
          NOT(Answer(ident="reading_comprehension")))
    def ask_reading_comprehension(self):
        self.declare(Question(ident="reading_comprehension", text="هل تعاني من صعوبة في فهم معاني النصوص؟", valid=["نعم", "لا"], Type="multi"))

    @Rule(Answer(ident="reading_comprehension", text="نعم"))
    def handle_reading_comprehension_yes(self):
        self.recommend_action("تقييم الصعوبات في:\n1. التسلسل\n2. العلاقات\n3. الاستنتاجات\n4. المعاني العميقة للنص")
        self.recommend_action("الحاجة إلى دعم في فهم القراءة")

    @Rule(Fact(ask="spelling"),
          NOT(Answer(ident="spelling")))
    def ask_spelling(self):
        self.declare(Question(ident="spelling", text="هل تعاني من صعوبات في التهجئة؟", valid=["نعم", "لا"], Type="multi"))

    @Rule(Answer(ident="spelling", text="نعم"))
    def handle_spelling_yes(self):
        self.recommend_action("تقييم الأخطاء في:\n1. إضافة أو حذف أو استبدال الحروف الصوتية أو الساكنة")
        self.recommend_action("الحاجة إلى دعم في التهجئة")

    @Rule(Fact(ask="written_expression"),
          NOT(Answer(ident="written_expression")))
    def ask_written_expression(self):
        self.declare(Question(ident="written_expression", text="هل تعاني من صعوبات في التعبير الكتابي؟", valid=["نعم", "لا"], Type="multi"))

    @Rule(Answer(ident="written_expression", text="نعم"))
    def handle_written_expression_yes(self):
        self.recommend_action("تقييم الصعوبات في:\n1. الأخطاء النحوية\n2. تنظيم الفقرات\n3. وضوح التعبير")
        self.recommend_action("الحاجة إلى دعم في التعبير الكتابي")

    @Rule(Fact(ask="number_sense"),
          NOT(Answer(ident="number_sense")))
    def ask_number_sense(self):
        self.declare(Question(ident="number_sense", text="هل يعاني تعاني من صعوبات في فهم الأرقام أو العمليات الحسابية؟", valid=["نعم", "لا"], Type="multi"))

    @Rule(Answer(ident="number_sense", text="نعم"))
    def handle_number_sense_yes(self):
        self.recommend_action("تقييم الصعوبات في:\n1. فهم الأرقام\n2. استخدام الأصابع للحساب\n3. الضياع في العمليات الحسابية")
        self.recommend_action("الحاجة إلى دعم في مهارات الرياضيات")

    @Rule(Fact(ask="math_reasoning"),
          NOT(Answer(ident="math_reasoning")))
    def ask_math_reasoning(self):
        self.declare(Question(ident="math_reasoning", text="هل تعاني من صعوبات في التفكير الرياضي؟", valid=["نعم", "لا"], Type="multi"))

    @Rule(Answer(ident="math_reasoning", text="نعم"))
    def handle_math_reasoning_yes(self):
        self.recommend_action("تقييم الصعوبات في:\n1. صعوبة تطبيق المفاهيم الرياضية\n2. حل المشاكل الكمية")
        self.recommend_action("الحاجة إلى دعم في التفكير الرياضي")

    @Rule(Fact(ask="problem_solving"),
          NOT(Answer(ident="problem_solving")))
    def ask_problem_solving(self):
        self.declare(Question(ident="problem_solving", text="هل تحتاج إلى دعم في مهام حل المشكلات في الحياة اليومية، مثل إدارة المواعيد أو التعامل مع المال؟", valid=["نعم", "لا"], Type="multi"))

    @Rule(Answer(ident="problem_solving", text="نعم"))
    def handle_problem_solving_yes(self):
        self.recommend_action("تحديد العجز المفاهيمي الكبير")
        self.recommend_action("الحاجة إلى دعم في المهام الأكاديمية وحل المشكلات اليومية")

    @Rule(Answer(ident="problem_solving", text="لا"))
    def handle_problem_solving_no(self):
        self.recommend_action("تحديد العجز المفاهيمي البسيط")
        self.recommend_action("الحاجة إلى دعم في المجالات الأكاديمية فقط")

    @Rule(Fact(ask="social_communication"),
          NOT(Answer(ident="social_communication")))
    def ask_social_communication(self):
        self.declare(Question(ident="social_communication", text="هل لديك نقصات مستمرة في التواصل الاجتماعي عبر سياقات متعددة؟", valid=["نعم", "لا"], Type="multi"))

    @Rule(Answer(ident="social_communication", text="نعم"))
    def handle_social_communication_yes(self):
        self.declare(Fact(ask="social_emotional_reciprocity"))

    @Rule(Answer(ident="social_communication", text="لا"))
    def handle_social_communication_no(self):
        self.recommend_action("لا توجد نقصات مهمة في التواصل الاجتماعي")

    @Rule(Fact(ask="social_emotional_reciprocity"),
          NOT(Answer(ident="social_emotional_reciprocity")))
    def ask_social_emotional_reciprocity(self):
        self.declare(Question(ident="social_emotional_reciprocity", text="تقييم النقصانات في التبادل الاجتماعي العاطفي", valid=["ضعيف", "متوسط", "لا شيء"], Type="multi"))

    @Rule(Answer(ident="social_emotional_reciprocity", text="ضعيف"))
    def handle_social_emotional_reciprocity_weak(self):
        self.recommend_action("تحديد القضايا المحددة:\n1. النهج الاجتماعي غير الطبيعي\n2. فشل المحادثة الطبيعية ذهابًا وإيابًا\n3. تقليل مشاركة الاهتمامات أو العواطف أو التأثيرات")

    @Rule(Answer(ident="social_emotional_reciprocity", text="متوسط"), Answer(ident="social_emotional_reciprocity", text="لا شيء"))
    def handle_social_emotional_reciprocity_moderate_none(self):
        self.recommend_action("عدم وجود نقص كبير في التبادل الاجتماعي العاطفي")

    @Rule(Fact(ask="nonverbal_communication"),
          NOT(Answer(ident="nonverbal_communication")))
    def ask_nonverbal_communication(self):
        self.declare(Question(ident="nonverbal_communication", text="تقييم السلوكيات التواصلية غير اللفظية", valid=["ضعيف", "متوسط", "لا شيء"], Type="multi"))

    @Rule(Answer(ident="nonverbal_communication", text="ضعيف"))
    def handle_nonverbal_communication_weak(self):
        self.recommend_action("تحديد القضايا المحددة:\n1. التواصل اللفظي وغير اللفظي غير متكامل بشكل جيد\n2. شذوذات في الاتصال بالعين ولغة الجسم\n3. عدم وجود تعابير وتواصل غير لفظي")

    @Rule(Answer(ident="nonverbal_communication", text="متوسط"), Answer(ident="nonverbal_communication", text="لا شيء"))
    def handle_nonverbal_communication_moderate_none(self):
        self.recommend_action("عدم وجود نقص كبير في السلوكيات التواصلية غير اللفظية")

    @Rule(Fact(ask="relationships"),
          NOT(Answer(ident="relationships")))
    def ask_relationships(self):
        self.declare(Question(ident="relationships", text="تقييم القدرة على تطوير والحفاظ على وفهم العلاقات", valid=["ضعيف", "متوسط", "لا شيء"], Type="multi"))

    @Rule(Answer(ident="relationships", text="ضعيف"))
    def handle_relationships_weak(self):
        self.recommend_action("تحديد القضايا المحددة:\n1. صعوبات في ضبط السلوك ليتناسب مع السياقات الاجتماعية\n2. صعوبات في مشاركة اللعب الخيالي أو التعرف على الأصدقاء\n3. عدم وجود اهتمام بالأقران")

    @Rule(Answer(ident="relationships", text="متوسط"), Answer(ident="relationships", text="لا شيء"))
    def handle_relationships_moderate_none(self):
        self.recommend_action("عدم وجود نقص كبير في القدرة على تطوير والحفاظ على وفهم العلاقات")


engine = MentalHealthExpertSystem()
