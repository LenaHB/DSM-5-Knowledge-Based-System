from experta import *

class SchizophreniaSpectrumDisorder(Fact):
    """Fact to check for Schizophrenia Spectrum Disorders"""
    pass

class Question(Fact):
    """Fact to represent a question"""
    pass

class Answer(Fact):
    """Fact to represent an answer"""
    pass

class SchizophreniaSpectrumExpertSystem(KnowledgeEngine):

    @DefFacts()
    def init(self):
        # Main chart questions
        yield Question(ident="psychotic_symptoms", text="هل توجد أعراض ذهانية؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="duration_of_symptoms", text="ما هي مدة الأعراض الذهانية؟", valid=["أقل من شهر", "1-6 أشهر", "أكثر من 6 أشهر"], Type="multi")
        yield Question(ident="mood_symptoms", text="هل توجد أعراض مزاجية متزامنة؟", valid=["نعم", "لا"], Type="multi")

        # Brief Psychotic Disorder sub-chart questions
        yield Question(ident="brief_psychotic_sudden", text="هل الأعراض بدأت بشكل مفاجئ؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="brief_psychotic_delusions", text="هل توجد أوهام؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="brief_psychotic_hallucinations", text="هل توجد هلوسات؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="brief_psychotic_disorganized_speech", text="هل يوجد كلام غير منظم؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="brief_psychotic_disorganized_behavior", text="هل يوجد سلوك غير منظم أو كاتاتوني؟", valid=["نعم", "لا"], Type="multi")

        # Schizophreniform Disorder sub-chart questions
        yield Question(ident="schizophreniform_delusions", text="هل توجد أوهام؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="schizophreniform_hallucinations", text="هل توجد هلوسات؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="schizophreniform_disorganized_speech", text="هل يوجد كلام غير منظم؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="schizophreniform_disorganized_behavior", text="هل يوجد سلوك غير منظم أو كاتاتوني؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="schizophreniform_functional_impact", text="هل تسبب الأعراض تأثيراً كبيراً على الحياة الاجتماعية أو المهنية؟", valid=["نعم", "لا"], Type="multi")

        # Schizophrenia sub-chart questions
        yield Question(ident="schizophrenia_delusions", text="هل توجد أوهام؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="schizophrenia_hallucinations", text="هل توجد هلوسات؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="schizophrenia_disorganized_speech", text="هل يوجد كلام غير منظم؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="schizophrenia_disorganized_behavior", text="هل يوجد سلوك غير منظم أو كاتاتوني؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="schizophrenia_negative_symptoms", text="هل توجد أعراض سلبية مثل التسطح العاطفي، انعدام الإرادة، انعدام الكلام؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="schizophrenia_functional_impact", text="هل تسبب الأعراض تأثيراً كبيراً على الحياة الاجتماعية أو المهنية؟", valid=["نعم", "لا"], Type="multi")

        # Schizoaffective Disorder sub-chart questions
        yield Question(ident="schizoaffective_psychotic_mood_symptoms", text="هل توجد أعراض ذهانية ومزاجية متزامنة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="schizoaffective_psychotic_duration", text="هل تستمر الأعراض الذهانية لمدة أسبوعين على الأقل بدون أعراض مزاجية بارزة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="schizoaffective_mood_duration", text="هل تستمر نوبات المزاج طوال مدة المرض؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="schizoaffective_functional_impact", text="هل تسبب الأعراض تأثيراً كبيراً على الحياة الاجتماعية أو المهنية؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="schizoaffective_no_other_causes", text="هل توجد أسباب أخرى مثل تعاطي المخدرات أو الحالات الطبية؟", valid=["نعم", "لا"], Type="multi")

    def recommend_action(self, action):
        print("أوصي بأن تقوم بـ " + action + "\n")

    # Main Chart Rules
    @Rule(NOT(Answer(ident="psychotic_symptoms")),
          NOT(Fact(ask="psychotic_symptoms")))
    def ask_psychotic_symptoms(self):
        self.declare(Fact(ask="psychotic_symptoms"))

    @Rule(Answer(ident="psychotic_symptoms", text="نعم"))
    def handle_psychotic_symptoms_yes(self):
        self.declare(Fact(ask="duration_of_symptoms"))

    @Rule(Answer(ident="psychotic_symptoms", text="لا"))
    def handle_psychotic_symptoms_no(self):
        self.recommend_action("تقييم للأمراض الأخرى")
        self.halt()

    @Rule(Answer(ident="duration_of_symptoms", text="أقل من شهر"))
    def handle_duration_less_than_month(self):
        self.declare(Fact(ask="brief_psychotic_sudden"))

    @Rule(Answer(ident="duration_of_symptoms", text="1-6 أشهر"))
    def handle_duration_1_to_6_months(self):
        self.declare(Fact(ask="schizophreniform_delusions"))

    @Rule(Answer(ident="duration_of_symptoms", text="أكثر من 6 أشهر"))
    def handle_duration_more_than_6_months(self):
        self.declare(Fact(ask="schizophrenia_delusions"))

    @Rule(Answer(ident="mood_symptoms", text="نعم"))
    def handle_mood_symptoms_yes(self):
        self.declare(Fact(ask="schizoaffective_psychotic_mood_symptoms"))

    @Rule(Answer(ident="mood_symptoms", text="لا"))
    def handle_mood_symptoms_no(self):
        self.recommend_action("اضطرابات ذهانية أخرى")
        self.halt()

    # Brief Psychotic Disorder Rules
    @Rule(Fact(ask="brief_psychotic_sudden"),
          NOT(Answer(ident="brief_psychotic_sudden")))
    def ask_brief_psychotic_sudden(self):
        self.declare(Fact(ask="brief_psychotic_sudden"))

    @Rule(Answer(ident="brief_psychotic_sudden", text="نعم"))
    def handle_brief_psychotic_sudden_yes(self):
        self.declare(Fact(ask="brief_psychotic_delusions"))

    @Rule(Answer(ident="brief_psychotic_sudden", text="لا"))
    def handle_brief_psychotic_sudden_no(self):
        self.recommend_action("استبعاد الاضطراب الذهاني القصير")
        self.halt()

    @Rule(Answer(ident="brief_psychotic_delusions", text="نعم"))
    def handle_brief_psychotic_delusions_yes(self):
        self.recommend_action("تشخيص الاضطراب الذهاني القصير")

    @Rule(Answer(ident="brief_psychotic_delusions", text="لا"))
    def handle_brief_psychotic_delusions_no(self):
        self.declare(Fact(ask="brief_psychotic_hallucinations"))

    @Rule(Answer(ident="brief_psychotic_hallucinations", text="نعم"))
    def handle_brief_psychotic_hallucinations_yes(self):
        self.recommend_action("تشخيص الاضطراب الذهاني القصير")

    @Rule(Answer(ident="brief_psychotic_hallucinations", text="لا"))
    def handle_brief_psychotic_hallucinations_no(self):
        self.declare(Fact(ask="brief_psychotic_disorganized_speech"))

    @Rule(Answer(ident="brief_psychotic_disorganized_speech",text="نعم"))
    def handle_brief_psychotic_disorganized_speech_yes(self):
        self.recommend_action("تشخيص الاضطراب الذهاني القصير")

    @Rule(Answer(ident="brief_psychotic_disorganized_speech", text="لا"))
    def handle_brief_psychotic_disorganized_speech_no(self):
        self.declare(Fact(ask="brief_psychotic_disorganized_behavior"))

    @Rule(Answer(ident="brief_psychotic_disorganized_behavior", text="نعم"))
    def handle_brief_psychotic_disorganized_behavior_yes(self):
        self.recommend_action("تشخيص الاضطراب الذهاني القصير")

    @Rule(Answer(ident="brief_psychotic_disorganized_behavior", text="لا"))
    def handle_brief_psychotic_disorganized_behavior_no(self):
        self.recommend_action("استبعاد الاضطراب الذهاني القصير")
        self.halt()

    # Schizophreniform Disorder Rules
    @Rule(Fact(ask="schizophreniform_delusions"),
          NOT(Answer(ident="schizophreniform_delusions")))
    def ask_schizophreniform_delusions(self):
        self.declare(Fact(ask="schizophreniform_delusions"))

    @Rule(Answer(ident="schizophreniform_delusions", text="نعم"))
    def handle_schizophreniform_delusions_yes(self):
        self.declare(Fact(ask="schizophreniform_functional_impact"))

    @Rule(Answer(ident="schizophreniform_delusions", text="لا"))
    def handle_schizophreniform_delusions_no(self):
        self.declare(Fact(ask="schizophreniform_hallucinations"))

    @Rule(Fact(ask="schizophreniform_hallucinations"),
          NOT(Answer(ident="schizophreniform_hallucinations")))
    def ask_schizophreniform_hallucinations(self):
        self.declare(Fact(ask="schizophreniform_hallucinations"))

    @Rule(Answer(ident="schizophreniform_hallucinations", text="نعم"))
    def handle_schizophreniform_hallucinations_yes(self):
        self.declare(Fact(ask="schizophreniform_functional_impact"))

    @Rule(Answer(ident="schizophreniform_hallucinations", text="لا"))
    def handle_schizophreniform_hallucinations_no(self):
        self.declare(Fact(ask="schizophreniform_disorganized_speech"))

    @Rule(Fact(ask="schizophreniform_disorganized_speech"),
          NOT(Answer(ident="schizophreniform_disorganized_speech")))
    def ask_schizophreniform_disorganized_speech(self):
        self.declare(Fact(ask="schizophreniform_disorganized_speech"))

    @Rule(Answer(ident="schizophreniform_disorganized_speech", text="نعم"))
    def handle_schizophreniform_disorganized_speech_yes(self):
        self.declare(Fact(ask="schizophreniform_functional_impact"))

    @Rule(Answer(ident="schizophreniform_disorganized_speech", text="لا"))
    def handle_schizophreniform_disorganized_speech_no(self):
        self.declare(Fact(ask="schizophreniform_disorganized_behavior"))

    @Rule(Fact(ask="schizophreniform_disorganized_behavior"),
          NOT(Answer(ident="schizophreniform_disorganized_behavior")))
    def ask_schizophreniform_disorganized_behavior(self):
        self.declare(Fact(ask="schizophreniform_disorganized_behavior"))

    @Rule(Answer(ident="schizophreniform_disorganized_behavior", text="نعم"))
    def handle_schizophreniform_disorganized_behavior_yes(self):
        self.declare(Fact(ask="schizophreniform_functional_impact"))

    @Rule(Answer(ident="schizophreniform_disorganized_behavior", text="لا"))
    def handle_schizophreniform_disorganized_behavior_no(self):
        self.recommend_action("استبعاد الاضطراب الفصامي الشكل")
        self.halt()

    @Rule(Answer(ident="schizophreniform_functional_impact", text="نعم"))
    def handle_schizophreniform_functional_impact_yes(self):
        self.recommend_action("تشخيص الاضطراب الفصامي الشكل")

    @Rule(Answer(ident="schizophreniform_functional_impact", text="لا"))
    def handle_schizophreniform_functional_impact_no(self):
        self.recommend_action("استبعاد الاضطراب الفصامي الشكل")
        self.halt()

    # Schizophrenia Disorder Rules
    @Rule(Fact(ask="schizophrenia_delusions"),
          NOT(Answer(ident="schizophrenia_delusions")))
    def ask_schizophrenia_delusions(self):
        self.declare(Fact(ask="schizophrenia_delusions"))

    @Rule(Answer(ident="schizophrenia_delusions", text="نعم"))
    def handle_schizophrenia_delusions_yes(self):
        self.declare(Fact(ask="schizophrenia_functional_impact"))

    @Rule(Answer(ident="schizophrenia_delusions", text="لا"))
    def handle_schizophrenia_delusions_no(self):
        self.declare(Fact(ask="schizophrenia_hallucinations"))

    @Rule(Fact(ask="schizophrenia_hallucinations"),
          NOT(Answer(ident="schizophrenia_hallucinations")))
    def ask_schizophrenia_hallucinations(self):
        self.declare(Fact(ask="schizophrenia_hallucinations"))

    @Rule(Answer(ident="schizophrenia_hallucinations", text="نعم"))
    def handle_schizophrenia_hallucinations_yes(self):
        self.declare(Fact(ask="schizophrenia_functional_impact"))

    @Rule(Answer(ident="schizophrenia_hallucinations", text="لا"))
    def handle_schizophrenia_hallucinations_no(self):
        self.declare(Fact(ask="schizophrenia_disorganized_speech"))

    @Rule(Fact(ask="schizophrenia_disorganized_speech"),
          NOT(Answer(ident="schizophrenia_disorganized_speech")))
    def ask_schizophrenia_disorganized_speech(self):
        self.declare(Fact(ask="schizophrenia_disorganized_speech"))

    @Rule(Answer(ident="schizophrenia_disorganized_speech", text="نعم"))
    def handle_schizophrenia_disorganized_speech_yes(self):
        self.declare(Fact(ask="schizophrenia_functional_impact"))

    @Rule(Answer(ident="schizophrenia_disorganized_speech", text="لا"))
    def handle_schizophrenia_disorganized_speech_no(self):
        self.declare(Fact(ask="schizophrenia_disorganized_behavior"))

    @Rule(Fact(ask="schizophrenia_disorganized_behavior"),
          NOT(Answer(ident="schizophrenia_disorganized_behavior")))
    def ask_schizophrenia_disorganized_behavior(self):
        self.declare(Fact(ask="schizophrenia_disorganized_behavior"))

    @Rule(Answer(ident="schizophrenia_disorganized_behavior", text="نعم"))
    def handle_schizophrenia_disorganized_behavior_yes(self):
        self.declare(Fact(ask="schizophrenia_functional_impact"))

    @Rule(Answer(ident="schizophrenia_disorganized_behavior", text="لا"))
    def handle_schizophrenia_disorganized_behavior_no(self):
        self.declare(Fact(ask="schizophrenia_negative_symptoms"))

    @Rule(Fact(ask="schizophrenia_negative_symptoms"),
          NOT(Answer(ident="schizophrenia_negative_symptoms")))
    def ask_schizophrenia_negative_symptoms(self):
        self.declare(Fact(ask="schizophrenia_negative_symptoms"))

    @Rule(Answer(ident="schizophrenia_negative_symptoms", text="نعم"))
    def handle_schizophrenia_negative_symptoms_yes(self):
        self.declare(Fact(ask="schizophrenia_functional_impact"))

    @Rule(Answer(ident="schizophrenia_negative_symptoms", text="لا"))
    def handle_schizophrenia_negative_symptoms_no(self):
        self.recommend_action("استبعاد الفصام")
        self.halt()

    @Rule(Answer(ident="schizophrenia_functional_impact", text="نعم"))
    def handle_schizophrenia_functional_impact_yes(self):
        self.recommend_action("تشخيص الفصام")

    @Rule(Answer(ident="schizophrenia_functional_impact", text="لا"))
    def handle_schizophrenia_functional_impact_no(self):
        self.recommend_action("استبعاد الفصام")
        self.halt()

    # Schizoaffective Disorder Rules
    @Rule(Fact(ask="schizoaffective_psychotic_mood_symptoms"),
          NOT(Answer(ident="schizoaffective_psychotic_mood_symptoms")))
    def ask_schizoaffective_psychotic_mood_symptoms(self):
        self.declare(Fact(ask="schizoaffective_psychotic_mood_symptoms"))

    @Rule(Answer(ident="schizoaffective_psychotic_mood_symptoms", text="نعم"))
    def handle_schizoaffective_psychotic_mood_symptoms_yes(self):
        self.declare(Fact(ask="schizoaffective_psychotic_duration"))

    @Rule(Answer(ident="schizoaffective_psychotic_mood_symptoms", text="لا"))
    def handle_schizoaffective_psychotic_mood_symptoms_no(self):
        self.recommend_action("استبعاد الاضطراب الفصامي العاطفي")
        self.halt()

    @Rule(Fact(ask="schizoaffective_psychotic_duration"),
          NOT(Answer(ident="schizoaffective_psychotic_duration")))
    def ask_schizoaffective_psychotic_duration(self):
        self.declare(Fact(ask="schizoaffective_psychotic_duration"))

    @Rule(Answer(ident="schizoaffective_psychotic_duration", text="نعم"))
    def handle_schizoaffective_psychotic_duration_yes(self):
        self.declare(Fact(ask="schizoaffective_mood_duration"))

    @Rule(Answer(ident="schizoaffective_psychotic_duration", text="لا"))
    def handle_schizoaffective_psychotic_duration_no(self):
        self.recommend_action("استبعاد الاضطراب الفصامي العاطفي")
        self.halt()

    @Rule(Fact(ask="schizoaffective_mood_duration"),
          NOT(Answer(ident="schizoaffective_mood_duration")))
    def ask_schizoaffective_mood_duration(self):
        self.declare(Fact(ask="schizoaffective_mood_duration"))

    @Rule(Answer(ident="schizoaffective_mood_duration", text="نعم"))
    def handle_schizoaffective_mood_duration_yes(self):
        self.declare(Fact(ask="schizoaffective_functional_impact"))

    @Rule(Answer(ident="schizoaffective_mood_duration", text="لا"))
    def handle_schizoaffective_mood_duration_no(self):
        self.recommend_action("استبعاد الاضطراب الفصامي العاطفي")
        self.halt()

    @Rule(Fact(ask="schizoaffective_functional_impact"),
          NOT(Answer(ident="schizoaffective_functional_impact")))
    def ask_schizoaffective_functional_impact(self):
        self.declare(Fact(ask="schizoaffective_functional_impact"))

    @Rule(Answer(ident="schizoaffective_functional_impact", text="نعم"))
    def handle_schizoaffective_functional_impact_yes(self):
        self.declare(Fact(ask="schizoaffective_no_other_causes"))

    @Rule(Answer(ident="schizoaffective_functional_impact", text="لا"))
    def handle_schizoaffective_functional_impact_no(self):
        self.recommend_action("استبعاد الاضطراب الفصامي العاطفي")
        self.halt()

    @Rule(Fact(ask="schizoaffective_no_other_causes"),
          NOT(Answer(ident="schizoaffective_no_other_causes")))
    def ask_schizoaffective_no_other_causes(self):
        self.declare(Fact(ask="schizoaffective_no_other_causes"))

    @Rule(Answer(ident="schizoaffective_no_other_causes", text="لا"))
    def handle_schizoaffective_no_other_causes_no(self):
        self.recommend_action("استبعاد الاضطراب الفصامي العاطفي")
        self.halt()

    @Rule(Answer(ident="schizoaffective_no_other_causes", text="نعم"))
    def handle_schizoaffective_no_other_causes_yes(self):
        self.recommend_action("تشخيص الاضطراب الفصامي العاطفي")

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
    engine = SchizophreniaSpectrumExpertSystem()
    engine.reset()
    engine.run()
