from experta import *

class BipolarEpisode(Fact):
    """Fact to check if a Bipolar episode is present"""
    pass

class MajorDepressiveEpisode(Fact):
    """Fact to check if a Major Depressive episode is present"""
    pass

class HypomanicEpisode(Fact):
    """Fact to check if a Hypomanic episode is present"""
    pass

class PersistentDepressiveDisorder(Fact):
    """Fact to check if Persistent Depressive Disorder is present"""
    pass

class SubstanceInducedBipolar(Fact):
    """Fact to check if the symptoms are Substance-Induced Bipolar"""
    pass

class MedicalCondition(Fact):
    """Fact to check if a medical condition is present"""
    pass

class CyclothymicDisorder(Fact):
    """Fact to check if Cyclothymic Disorder is present"""
    pass

class DepressiveEpisode(Fact):
    """Fact to check if a Depressive episode is present"""
    pass

class ManicEpisode(Fact):
    """Fact to check if a Manic episode is present"""
    pass

class MixedFeatures(Fact):
    """Fact to check if Mixed Features are present"""
    pass

class Question(Fact):
    """Fact to represent a question"""
    pass

class Answer(Fact):
    """Fact to represent an answer"""
    pass

class BipolarDisorderExpertSystem(KnowledgeEngine):

    @DefFacts()
    def init(self):
        yield Question(ident="manic_episode", text="هل تعاني من نوبات هوس قوية؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="hypomanic_episode", text="هل تعاني المريض من نوبات هوس خفيف؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="persistent_depressive_disorder", text="هل تعاني من اكتئاب مستمر؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="substance_induced", text="هل هناك أعراض ناتجة عن مواد أو دواء؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="medical_condition", text="هل توجد حالة طبية أخرى تسبب الأعراض؟", valid=["نعم", "لا"], Type="multi")

    def recommend_action(self, action):
        print("أوصي بأن تقوم بـ " + action + "\n")

    @Rule(NOT(Answer(ident="manic_episode")),
          NOT(Fact(ask="manic_episode")))
    def ask_manic_episode(self):
        self.declare(Fact(ask="manic_episode"))

    @Rule(Answer(ident="manic_episode", text="نعم"))
    def handle_manic_episode_yes(self):
        self.declare(BipolarEpisode(type="manic"))
        self.declare(Fact(ask="Bipolar_I_Disorder_Diagnostic"))

    @Rule(Answer(ident="manic_episode", text="لا"),
          NOT(Answer(ident="hypomanic_episode")),
          NOT(Fact(ask="hypomanic_episode")))
    def ask_hypomanic_episode(self):
        self.declare(Fact(ask="hypomanic_episode"))

    @Rule(Answer(ident="hypomanic_episode", text="نعم"))
    def handle_hypomanic_episode_yes(self):
        self.declare(HypomanicEpisode())
        self.declare(Fact(ask="Bipolar_II_Disorder_Diagnostic"))

    @Rule(Answer(ident="hypomanic_episode", text="لا"),
          NOT(Answer(ident="persistent_depressive_disorder")),
          NOT(Fact(ask="persistent_depressive_disorder")))
    def ask_persistent_depressive_disorder(self):
        self.declare(Fact(ask="persistent_depressive_disorder"))

    @Rule(Answer(ident="persistent_depressive_disorder", text="نعم"))
    def handle_persistent_depressive_disorder_yes(self):
        self.declare(PersistentDepressiveDisorder())
        self.recommend_action("تأكيد اضطراب الاكتئاب المستمر")

    @Rule(Answer(ident="persistent_depressive_disorder", text="لا"),
          NOT(Answer(ident="substance_induced")),
          NOT(Fact(ask="substance_induced")))
    def ask_substance_induced(self):
        self.declare(Fact(ask="substance_induced"))

    @Rule(Answer(ident="substance_induced", text="نعم"))
    def handle_substance_induced_yes(self):
        self.declare(SubstanceInducedBipolar())
        self.recommend_action("تأكيد اضطراب ثنائي القطب والاضطرابات ذات الصلة الناجمة عن المادة/الدواء")

    @Rule(Answer(ident="substance_induced", text="لا"),
          NOT(Answer(ident="medical_condition")),
          NOT(Fact(ask="medical_condition")))
    def ask_medical_condition(self):
        self.declare(Fact(ask="medical_condition"))

    @Rule(Answer(ident="medical_condition", text="نعم"))
    def handle_medical_condition_yes(self):
        self.declare(MedicalCondition())
        self.recommend_action("تأكيد اضطراب ثنائي القطب والاضطرابات ذات الصلة الناجمة عن حالة طبية")

    @Rule(Answer(ident="medical_condition", text="لا"))
    def handle_no_clear_diagnosis(self):
        self.recommend_action("لا يوجد تشخيص واضح، استمر في التقييم")

    # Bipolar I Disorder Diagnostic
    @Rule(Fact(ask="Bipolar_I_Disorder_Diagnostic"),
          NOT(Answer(ident="Bipolar_I_Disorder_Diagnostic")))
    def ask_bipolar_i_diagnostic(self):
        self.declare(Question(ident="Bipolar_I_Disorder_Diagnostic", text="هل يعاني الشخص من نوبة هوسية تتميز بمزاج مرتفع أو متوسع أو متهيج مستمر ونشاط موجه لأهداف متزايد بشكل غير طبيعي؟", valid=["نعم", "لا"], Type="multi"))

    @Rule(Answer(ident="Bipolar_I_Disorder_Diagnostic", text="نعم"))
    def handle_bipolar_i_yes(self):
        self.recommend_action("التشخيص: اضطراب ثنائي القطب من النوع الأول")

    @Rule(Answer(ident="Bipolar_I_Disorder_Diagnostic", text="لا"),
          NOT(Answer(ident="depressive_episode")),
          NOT(Fact(ask="depressive_episode")))
    def ask_depressive_episode(self):
        self.declare(Fact(ask="depressive_episode"))

    @Rule(Answer(ident="depressive_episode", text="نعم"),
          NOT(Answer(ident="hypomanic_recurrent")),
          NOT(Fact(ask="hypomanic_recurrent")))
    def ask_hypomanic_recurrent(self):
        self.declare(Question(ident="hypomanic_recurrent", text="هل توجد نوبات هوس خفيف متكررة؟", valid=["نعم", "لا"], Type="multi"))

    @Rule(Answer(ident="hypomanic_recurrent", text="نعم"))
    def handle_hypomanic_recurrent_yes(self):
        self.recommend_action("التشخيص: اضطراب ثنائي القطب من النوع الثاني")

    @Rule(Answer(ident="hypomanic_recurrent", text="لا"))
    def handle_hypomanic_recurrent_no(self):
        self.recommend_action("متابعة التقييم لاضطرابات أخرى")

    @Rule(Answer(ident="depressive_episode", text="لا"))
    def handle_depressive_episode_no(self):
        self.recommend_action("متابعة التقييم لاضطرابات أخرى")

    # Bipolar II Disorder Diagnostic
    @Rule(Fact(ask="Bipolar_II_Disorder_Diagnostic"),
          NOT(Answer(ident="Bipolar_II_Disorder_Diagnostic")))
    def ask_bipolar_ii_diagnostic(self):
        self.declare(Question(ident="Bipolar_II_Disorder_Diagnostic", text="هل تعاني من نوبة هوس خفيف واحدة على الأقل؟", valid=["نعم", "لا"], Type="multi"))

    @Rule(Answer(ident="Bipolar_II_Disorder_Diagnostic", text="نعم"),
          NOT(Answer(ident="major_depressive_episode")),
          NOT(Fact(ask="major_depressive_episode")))
    def ask_major_depressive_episode(self):
        self.declare(Fact(ask="major_depressive_episode"))

    @Rule(Answer(ident="major_depressive_episode", text="نعم"))
    def handle_major_depressive_episode_yes(self):
        self.recommend_action("التشخيص: اضطراب ثنائي القطب من النوع الثاني")

    @Rule(Answer(ident="major_depressive_episode", text="لا"))
    def handle_major_depressive_episode_no(self):
        self.recommend_action("متابعة التقييم لاضطرابات أخرى")

    @Rule(Answer(ident="Bipolar_II_Disorder_Diagnostic", text="لا"))
    def handle_bipolar_ii_no(self):
        self.recommend_action("متابعة التقييم لاضطرابات أخرى")

    # Other Diagnostics
    @Rule(Fact(ask="Bipolar_Medical_Condition"),
          NOT(Answer(ident="Bipolar_Medical_Condition")))
    def ask_bipolar_medical_condition(self):
        self.declare(Question(ident="Bipolar_Medical_Condition", text="هل توجد حالة طبية أخرى تسبب الأعراض؟", valid=["نعم", "لا"], Type="multi"))

    @Rule(Answer(ident="Bipolar_Medical_Condition", text="نعم"),
          NOT(Answer(ident="medical_symptoms")),
          NOT(Fact(ask="medical_symptoms")))
    def ask_medical_symptoms(self):
        self.declare(Fact(ask="medical_symptoms"))

    @Rule(Answer(ident="medical_symptoms", text="نعم"))
    def handle_medical_symptoms_yes(self):
        self.recommend_action("تأكيد اضطراب ثنائي القطب والاضطرابات ذات الصلة الناجمة عن حالة طبية")

    @Rule(Answer(ident="medical_symptoms", text="لا"))
    def handle_medical_symptoms_no(self):
        self.recommend_action("متابعة التقييم لاضطرابات أخرى")

    @Rule(Answer(ident="Bipolar_Medical_Condition", text="لا"))
    def handle_bipolar_medical_condition_no(self):
        self.recommend_action("لا يوجد اضطراب ثنائي القطب والاضطرابات ذات الصلة الناجمة عن حالة طبية")

    @Rule(Fact(ask="Substance_Induced_Bipolar_Disorder"),
          NOT(Answer(ident="Substance_Induced_Bipolar_Disorder")))
    def ask_substance_induced_bipolar_disorder(self):
        self.declare(Question(ident="Substance_Induced_Bipolar_Disorder", text="هل هناك أعراض ناتجة عن مواد أو دواء؟", valid=["نعم", "لا"], Type="multi"))

    @Rule(Answer(ident="Substance_Induced_Bipolar_Disorder", text="نعم"),
          NOT(Answer(ident="substance_symptoms")),
          NOT(Fact(ask="substance_symptoms")))
    def ask_substance_symptoms(self):
        self.declare(Fact(ask="substance_symptoms"))

    @Rule(Answer(ident="substance_symptoms", text="نعم"))
    def handle_substance_symptoms_yes(self):
        self.recommend_action("تأكيد اضطراب ثنائي القطب والاضطرابات ذات الصلة الناجمة عن المادة/الدواء")

    @Rule(Answer(ident="substance_symptoms", text="لا"))
    def handle_substance_symptoms_no(self):
        self.recommend_action("متابعة التقييم لاضطرابات أخرى")

    @Rule(Answer(ident="Substance_Induced_Bipolar_Disorder", text="لا"))
    def handle_substance_induced_bipolar_disorder_no(self):
        self.recommend_action("لا يوجد اضطراب ثنائي القطب والاضطرابات ذات الصلة الناجمة عن المادة/الدواء")

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
    engine = BipolarDisorderExpertSystem()
    engine.reset()
    engine.run()
