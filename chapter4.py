from experta import *

class PersistentDepressiveDisorder(Fact):
    """Fact to check if Persistent Depressive Disorder is present"""
    pass

class SubstanceInducedDepressiveDisorder(Fact):
    """Fact to check if the symptoms are Substance-Induced Depressive Disorder"""
    pass

class MajorDepressiveDisorder(Fact):
    """Fact to check if Major Depressive Disorder is present"""
    pass

class DepressiveDisorderDueToMedicalCondition(Fact):
    """Fact to check if Depressive Disorder is due to a Medical Condition"""
    pass

class Question(Fact):
    """Fact to represent a question"""
    pass

class Answer(Fact):
    """Fact to represent an answer"""
    pass

class DepressiveDisordersExpertSystem(KnowledgeEngine):

    @DefFacts()
    def init(self):
        yield Question(ident="main_event_related", text="هل الأعراض تتعلق بحدث حياتي كبير أو خسارة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="substance_use_related", text="هل هناك استخدام مواد يمكن أن يفسر الأعراض؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="persistent_depressive_mood", text="هل الأعراض شديدة ومستمرة لأكثر من سنتين؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="premenstrual_related", text="هل الأعراض تتفاقم خلال فترة ما قبل الحيض؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="major_depressive_mood", text="هل تعاني من مزاج مكتئب معظم اليوم، تقريبا كل يوم، لمدة أسبوعين على الأقل؟", valid=["نعم", "لا"], Type="multi")
        
        yield Question(ident="depressive_mood", text="هل يعاني الشخص من مزاج مكتئب لمدة سنتين أو أكثر؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="symptom_free_periods", text="هل توجد فترات خالية من الأعراض لأكثر من شهرين خلال فترة السنتين؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="other_symptoms", text="هل توجد أعراض أخرى مثل فقدان الشهية، الأرق، فرط النوم، انخفاض الطاقة، انخفاض احترام الذات، ضعف التركيز، أو اليأس؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="significant_distress", text="هل تسبب هذه الأعراض ضائقة سريرية كبيرة أو ضعف في الوظائف الاجتماعية، أو المهنية أو في مجالات هامة أخرى؟", valid=["نعم", "لا"], Type="multi")
        
        yield Question(ident="substance_use", text="هل تستخدم المواد المخدرة أو الأدوية؟", valid=[], Type="text")
        yield Question(ident="symptom_onset", text="هل بدأت الأعراض الاكتئابية خلال أو بعد فترة استخدام المادة أو الانسحاب منها؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="known_depressive_substance", text="هل المادة معروفة بأنها تحدث أعراض اكتئابية؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="symptom_duration", text="هل تستمر الأعراض لفترة كبيرة بعد التوقف عن استخدام المادة؟", valid=["نعم", "لا"], Type="multi")
        
        yield Question(ident="depressive_mood_major", text="هل تعاني من مزاج مكتئب معظم اليوم، تقريبا كل يوم، لمدة أسبوعين على الأقل؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="interest_loss", text="هل يوجد انخفاض ملحوظ في الاهتمام أو المتعة في جميع الأنشطة أو معظمها؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="additional_symptoms", text="هل توجد أربعة أو أكثر من الأعراض التالية موجودة خلال نفس الفترة الزمنية؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="symptom_distress", text="هل تسبب هذه الأعراض ضائقة سريرية كبيرة أو تعيق الأداء الاجتماعي، المهني، أو غيره من المجالات الهامة؟", valid=["نعم", "لا"], Type="multi")

        yield Question(ident="medical_condition", text="ما هي الحالة الطبية الأساسية؟", valid=[], Type="text")
        yield Question(ident="depressive_due_to_medical", text="هل توجد أدلة على أن الاضطراب الاكتئابي هو نتيجة مباشرة للعواقب الفسيولوجية المرضية للحالة الطبية؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="prominent_depressive_symptoms", text="هل توجد أعراض الاكتئاب الرئيسية مثل الحزن المستمر أو انخفاض الاهتمام بشكل ملحوظ؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="severe_symptoms", text="هل تسبب الأعراض ضائقة كبيرة سريرياً أو تعيق الأداء الاجتماعي أو المهني أو غيره من المجالات الهامة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="independent_depressive_disorder", text="هل كانت الأعراض الاكتئابية موجودة قبل الحالة الطبية؟", valid=["نعم", "لا"], Type="multi")

    def recommend_action(self, action):
        print("أوصي بأن تقوم بـ " + action + "\n")

    # Main Chart
    @Rule(NOT(Answer(ident="main_event_related")),
          NOT(Fact(ask="main_event_related")))
    def ask_main_event_related(self):
        self.declare(Fact(ask="main_event_related"))

    @Rule(Answer(ident="main_event_related", text="نعم"))
    def handle_main_event_related_yes(self):
        self.recommend_action("تقييم الحزن الطبيعي مقابل نوبة الاكتئاب الرئيسية")
        self.declare(Fact(ask="major_depressive_mood"))

    @Rule(Answer(ident="main_event_related", text="لا"))
    def handle_main_event_related_no(self):
        self.declare(Fact(ask="substance_use_related"))

    @Rule(Answer(ident="substance_use_related", text="نعم"))
    def handle_substance_use_related_yes(self):
        self.declare(Fact(ask="substance_use"))

    @Rule(Answer(ident="substance_use_related", text="لا"))
    def handle_substance_use_related_no(self):
        self.declare(Fact(ask="persistent_depressive_mood"))

    @Rule(Answer(ident="persistent_depressive_mood", text="نعم"))
    def handle_persistent_depressive_mood_yes(self):
        self.declare(Fact(ask="depressive_mood"))

    @Rule(Answer(ident="persistent_depressive_mood", text="لا"))
    def handle_persistent_depressive_mood_no(self):
        self.declare(Fact(ask="premenstrual_related"))

    @Rule(Answer(ident="premenstrual_related", text="نعم"))
    def handle_premenstrual_related_yes(self):
        self.recommend_action("تقييم اضطراب ما قبل الحيض الاكتئابي")
        self.halt()

    @Rule(Answer(ident="premenstrual_related", text="لا"))
    def handle_premenstrual_related_no(self):
        self.declare(Fact(ask="major_depressive_mood"))

    @Rule(Answer(ident="depressive_mood", text="نعم"))
    def handle_depressive_mood_yes(self):
        self.declare(Fact(ask="symptom_free_periods"))

    @Rule(Answer(ident="depressive_mood", text="لا"))
    def handle_depressive_mood_no(self):
        self.recommend_action("استبعاد الاضطراب الاكتئابي المستمر")
        self.halt()

    @Rule(Answer(ident="symptom_free_periods", text="لا"))
    def handle_symptom_free_periods_no(self):
        self.declare(Fact(ask="other_symptoms"))

    @Rule(Answer(ident="symptom_free_periods", text="نعم"))
    def handle_symptom_free_periods_yes(self):
        self.recommend_action("استبعاد الاضطراب الاكتئابي المستمر بسبب فترات خالية من الأعراض لأكثر من شهرين")
        self.halt()

    @Rule(Answer(ident="other_symptoms", text="نعم"))
    def handle_other_symptoms_yes(self):
        self.declare(Fact(ask="significant_distress"))

    @Rule(Answer(ident="other_symptoms", text="لا"))
    def handle_other_symptoms_no(self):
        self.recommend_action("استبعاد الاضطراب الاكتئابي المستمر")
        self.halt()

    @Rule(Answer(ident="significant_distress", text="نعم"))
    def handle_significant_distress_yes(self):
        self.recommend_action("تشخيص الاضطراب الاكتئابي المستمر")

    @Rule(Answer(ident="significant_distress", text="لا"))
    def handle_significant_distress_no(self):
        self.recommend_action("تقييم لأسباب بديلة")
        self.halt()

    # Major Depressive Disorder Detailed Sub-chart
    @Rule(Fact(ask="major_depressive_mood"),
          NOT(Answer(ident="major_depressive_mood")))
    def ask_major_depressive_mood(self):
        self.declare(Fact(ask="major_depressive_mood"))

    @Rule(Answer(ident="major_depressive_mood", text="نعم"))
    def handle_major_depressive_mood_yes(self):
        self.declare(Fact(ask="interest_loss"))

    @Rule(Answer(ident="major_depressive_mood", text="لا"))
    def handle_major_depressive_mood_no(self):
        self.recommend_action("استبعاد الاضطراب الاكتئابي الرئيسي؛ النظر في أسباب أخرى للأعراض")
        self.halt()

    @Rule(Fact(ask="interest_loss"),
          NOT(Answer(ident="interest_loss")))
    def ask_interest_loss(self):
        self.declare(Fact(ask="interest_loss"))

    @Rule(Answer(ident="interest_loss", text="نعم"))
    def handle_interest_loss_yes(self):
        self.declare(Fact(ask="additional_symptoms"))

    @Rule(Answer(ident="interest_loss", text="لا"))
    def handle_interest_loss_no(self):
        self.recommend_action("استمرار التقييم للتحقق من أعراض أخرى")
        self.halt()

    @Rule(Fact(ask="additional_symptoms"),
          NOT(Answer(ident="additional_symptoms")))
    def ask_additional_symptoms(self):
        self.declare(Fact(ask="additional_symptoms"))

    @Rule(Answer(ident="additional_symptoms", text="نعم"))
    def handle_additional_symptoms_yes(self):
        self.declare(Fact(ask="symptom_distress"))

    @Rule(Answer(ident="additional_symptoms", text="لا"))
    def handle_additional_symptoms_no(self):
        self.recommend_action("لا يوجد عدد كاف من الأعراض لتشخيص الاكتئاب الرئيسي")
        self.halt()

    @Rule(Fact(ask="symptom_distress"),
          NOT(Answer(ident="symptom_distress")))
    def ask_symptom_distress(self):
        self.declare(Fact(ask="symptom_distress"))

    @Rule(Answer(ident="symptom_distress", text="نعم"))
    def handle_symptom_distress_yes(self):
        self.recommend_action("تشخيص الاضطراب الاكتئابي الرئيسي")

    @Rule(Answer(ident="symptom_distress", text="لا"))
    def handle_symptom_distress_no(self):
        self.recommend_action("التشخيص غير مؤكد؛ تقييم الضائقة والتأثير الوظيفي")
        self.halt()

    # Substance-Induced Depressive Disorder Sub-chart
    @Rule(Fact(ask="substance_use"),
          NOT(Answer(ident="substance_use")))
    def ask_substance_use(self):
        self.declare(Fact(ask="substance_use"))

    @Rule(Answer(ident="substance_use", text=MATCH.text))
    def handle_substance_use(self, text):
        self.declare(Fact(ask="symptom_onset"))

    @Rule(Answer(ident="symptom_onset", text="نعم"))
    def handle_symptom_onset_yes(self):
        self.declare(Fact(ask="known_depressive_substance"))

    @Rule(Answer(ident="symptom_onset", text="لا"))
    def handle_symptom_onset_no(self):
        self.recommend_action("النظر في الاضطرابات الاكتئابية الأولية أو التشخيصات الأخرى")
        self.halt()

    @Rule(Fact(ask="known_depressive_substance"),
          NOT(Answer(ident="known_depressive_substance")))
    def ask_known_depressive_substance(self):
        self.declare(Fact(ask="known_depressive_substance"))

    @Rule(Answer(ident="known_depressive_substance", text="نعم"))
    def handle_known_depressive_substance_yes(self):
        self.declare(Fact(ask="symptom_duration"))

    @Rule(Answer(ident="known_depressive_substance", text="لا"))
    def handle_known_depressive_substance_no(self):
        self.recommend_action("استبعاد الاضطراب الاكتئابي المستحث بالمواد")
        self.halt()

    @Rule(Fact(ask="symptom_duration"),
          NOT(Answer(ident="symptom_duration")))
    def ask_symptom_duration(self):
        self.declare(Fact(ask="symptom_duration"))

    @Rule(Answer(ident="symptom_duration", text="نعم"))
    def handle_symptom_duration_yes(self):
        self.recommend_action("تشخيص الاضطراب الاكتئابي المستحث بالمواد")

    @Rule(Answer(ident="symptom_duration", text="لا"))
    def handle_symptom_duration_no(self):
        self.recommend_action("تقييم الآثار المتبقية والنظر في أسباب أخرى")
        self.halt()

    def ask_user(self, question, Type, valid=None):
        answer = ""
        while not self.is_of_type(answer, Type, valid):
            print(question)
            if Type == "multi":
                print("الإجابات الصالحة هي: ")
                for item in valid:
                    print(str(item) + " ")
                print("\n")
            answer = input().strip()
        return answer

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
        answer = self.ask_user(text, Type, valid)
        self.declare(Answer(ident=id, text=answer))

if __name__ == "__main__":
    engine = DepressiveDisordersExpertSystem()
    engine.reset()
    engine.run()
