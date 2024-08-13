from experta import *

class GeneralizedAnxietyDisorder(Fact):
    """Fact to check if Generalized Anxiety Disorder is present"""
    pass

class Agoraphobia(Fact):
    """Fact to check if Agoraphobia is present"""
    pass

class PanicDisorder(Fact):
    """Fact to check if Panic Disorder is present"""
    pass

class SocialAnxietyDisorder(Fact):
    """Fact to check if Social Anxiety Disorder is present"""
    pass

class SpecificPhobia(Fact):
    """Fact to check if Specific Phobia is present"""
    pass

class Question(Fact):
    """Fact to represent a question"""
    pass

class Answer(Fact):
    """Fact to represent an answer"""
    pass

class AnxietyDisordersExpertSystem(KnowledgeEngine):

    @DefFacts()
    def init(self):
        yield Question(ident="main_anxiety", text="هل تشعر بالقلق والتوتر أغلب الأيام لمدة 6 أشهر على الأقل؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="panic_attacks", text="هل تعاني من نوبات هلع متكررة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="social_anxiety", text="هل تخاف من التفاعل الاجتماعي أو أداء مهام تعرضك للحكم من الآخرين؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="specific_phobia", text="هل تخاف بشكل مفرط من شيء أو موقف محدد؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="fear_of_open_crowded_places", text="هل تخاف من وجودك في أماكن يصعب فيها الهروب أو الحصول على المساعدة؟", valid=["نعم", "لا"], Type="multi")

        # Questions for Generalized Anxiety Disorder
        yield Question(ident="general_anxiety", text="هل تشعر بالقلق والتوتر أغلب الأيام لمدة ستة أشهر على الأقل؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="control_anxiety", text="هل تشعر بصعوبة في التحكم بالقلق؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="tension_irritability", text="هل تشعر بتوتر أو استثارة سهلة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="constant_fatigue", text="هل تشعر بالتعب باستمرار؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="difficulty_concentrating", text="هل تجد صعوبة في التركيز؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="irritability", text="هل تشعر بتهيج؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="sleep_difficulty", text="هل تعاني من صعوبة في النوم؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="social_occupational_impact", text="هل يسبب القلق ضائقة كبيرة أو تأثيراً سلبياً على الحياة الاجتماعية أو المهنية؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="sleep_medication_stimulants", text="هل يوجد استهلاك لمنبهات أو أدوية تؤثر على النوم؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="psychological_stress", text="هل توجد ضغوط نفسية أو قلق؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="high_stress", text="هل تعاني من التوتر أو الضغط العالي؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="medical_problems", text="هل توجد مشاكل طبية مثل خلل هرموني؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="fatigue_medical", text="هل يوجد سبب طبي مثل فقر الدم؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="sleep_insufficient", text="هل هناك قلة في النوم أو نوم غير كاف؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="irritability_medical", text="هل توجد حالات طبية تسبب الاستثارة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="irritability_medication", text="هل تتناول منبهات أو أدوية تزيد الاستثارة؟", valid=["نعم", "لا"], Type="multi")


        # Questions for Agoraphobia
        yield Question(ident="anxiety_places", text="ما هي الأماكن التي تثير القلق؟ (الأماكن العامة، الأسواق، الجسور، وسائل النقل)", valid=["الأماكن العامة", "الأسواق", "الجسور", "وسائل النقل"], Type="multi")
        yield Question(ident="severity_of_fear", text="هل تتجنب هذه الأماكن أو يعاني من القلق الشديد عند التعرض لها؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="daily_functioning_impact", text="هل يؤثر هذا الخوف بشكل كبير على حياتك اليومية أو عمله؟", valid=["نعم", "لا"], Type="multi")

        # Questions for Panic Disorder
        yield Question(ident="panic_symptoms", text="تحديد الأعراض خلال النوبات: تسارع القلب، تعرق، رعشة، إحساس بالاختناق، ألم الصدر، الغثيان، دوار، خوف من الموت أو الجنون أو فقدان السيطرة", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="panic_impact", text="هل تتبع النوبات قلقاً بشأن حدوث نوبات أخرى أو عواقب النوبات، أو تغيرات سلوكية كبيرة متعلقة بالنوبات؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="panic_frequency_impact", text="هل تؤدي النوبات إلى قلق دائم ومخاوف من حدوث نوبات مستقبلية أو عواقبها؟", valid=["نعم", "لا"], Type="multi")

        # Questions for Social Anxiety Disorder
        yield Question(ident="fear_of_embarrassment", text="هل هناك خوف من التصرف بطريقة معينة أو إظهار أعراض القلق التي قد تكون محرجة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="social_anxiety_situations", text="ماهي المواقف التي تثير القلق؟ (التحدث أمام الجمهور، المشاركة في الأحداث الاجتماعية، تناول الطعام أمام الآخرين)", valid=["التحدث أمام الجمهور", "المشاركة في الاجتماعات الاجتماعية", "تناول الطعام أمام الآخرين"], Type="multi")
        yield Question(ident="social_anxiety_severity", text="هل يتم تجنب المواقف أو يتم تحملها بقلق شديد؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="social_anxiety_impact", text="هل يؤثر الخوف بشكل كبير على الحياة اليومية؟", valid=["نعم", "لا"], Type="multi")

        # Questions for Specific Phobia
        yield Question(ident="immediate_fear_response", text="هل يظهر الخوف فوراً عند التعرض للمحفز؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="specific_triggers", text="ماهي المحفزات الخاصة بالرهاب؟ (الحيوانات، الارتفاعات، الطيران، رؤية الدم، العواصف، الظلام)", valid=["الحيوانات", "الارتفاعات", "الطيران", "رؤية الدم", "العواصف", "الظلام"], Type="multi")
        yield Question(ident="avoidance_behavior", text="هل تتجنب بشكل واضح أوتتحمل بشدة المواقف أوالأشياء المخيفة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="specific_phobia_impact", text="هل يؤثر الخوف بشكل كبير على الحياة اليومية؟", valid=["نعم", "لا"], Type="multi")

    

    def recommend_action(self, action):
        print("أوصي بأن تقوم بـ " + action + "\n")

    # Main chart questions
    @Rule(NOT(Answer(ident="main_anxiety")),
          NOT(Fact(ask="main_anxiety")))
    def ask_main_anxiety(self):
        self.declare(Fact(ask="main_anxiety"))

    @Rule(Answer(ident="main_anxiety", text="نعم"))
    def handle_main_anxiety_yes(self):
        self.declare(Fact(ask="general_anxiety"))

    @Rule(Answer(ident="main_anxiety", text="لا"),
          NOT(Answer(ident="panic_attacks")),
          NOT(Fact(ask="panic_attacks")))
    def ask_panic_attacks(self):
        self.declare(Fact(ask="panic_attacks"))

    @Rule(Answer(ident="panic_attacks", text="نعم"))
    def handle_panic_attacks_yes(self):
        self.declare(Fact(ask="panic_symptoms"))

    @Rule(Answer(ident="panic_attacks", text="لا"),
          NOT(Answer(ident="social_anxiety")),
          NOT(Fact(ask="social_anxiety")))
    def ask_social_anxiety(self):
        self.declare(Fact(ask="social_anxiety"))

    @Rule(Answer(ident="social_anxiety", text="نعم"))
    def handle_social_anxiety_yes(self):
        self.declare(Fact(ask="fear_of_embarrassment"))

    @Rule(Answer(ident="social_anxiety", text="لا"),
          NOT(Answer(ident="specific_phobia")),
          NOT(Fact(ask="specific_phobia")))
    def ask_specific_phobia(self):
        self.declare(Fact(ask="specific_phobia"))

    @Rule(Answer(ident="specific_phobia", text="نعم"))
    def handle_specific_phobia_yes(self):
        self.declare(Fact(ask="immediate_fear_response"))

    @Rule(Answer(ident="specific_phobia", text="لا"),
          NOT(Answer(ident="fear_of_open_crowded_places")),
          NOT(Fact(ask="fear_of_open_crowded_places")))
    def ask_fear_of_open_crowded_places(self):
        self.declare(Fact(ask="fear_of_open_crowded_places"))

    @Rule(Answer(ident="fear_of_open_crowded_places", text="نعم"))
    def handle_fear_of_open_crowded_places_yes(self):
        self.declare(Fact(ask="anxiety_places"))

    @Rule(Answer(ident="fear_of_open_crowded_places", text="لا"))
    def handle_fear_of_open_crowded_places_no(self):
        self.recommend_action("النظر في أشكال أخرى من القلق أو المشاكل الصحية")
        self.halt()

    # Generalized Anxiety Disorder rules
    @Rule(Answer(ident="general_anxiety", text="نعم"))
    def handle_general_anxiety_yes(self):
        self.declare(Fact(ask="control_anxiety"))

    @Rule(Answer(ident="general_anxiety", text="لا"))
    def handle_general_anxiety_no(self):
        self.recommend_action("النظر في مدة وبداية الأعراض")
        self.halt()

    @Rule(Answer(ident="control_anxiety", text="نعم"))
    def handle_control_anxiety_yes(self):
        self.declare(Fact(ask="tension_irritability"))

    @Rule(Answer(ident="control_anxiety", text="لا"))
    def handle_control_anxiety_no(self):
        self.recommend_action("النظر في مدة وبداية الأعراض")
        self.halt()

    @Rule(Answer(ident="tension_irritability", text="نعم"))
    def handle_tension_irritability_yes(self):
        self.declare(Fact(ask="constant_fatigue"))

    # @Rule(Answer(ident="tension_irritability", text="لا"))
    # def handle_tension_irritability_no(self):
    #     self.recommend_action("النظر في مدة وبداية الأعراض")
    #     self.halt()

    @Rule(Answer(ident="constant_fatigue", text="نعم"))
    def handle_constant_fatigue_yes(self):
        self.declare(Fact(ask="difficulty_concentrating"))

    # @Rule(Answer(ident="constant_fatigue", text="لا"))
    # def handle_constant_fatigue_no(self):
    #     self.recommend_action("النظر في مدة وبداية الأعراض")
    #     self.halt()


    @Rule(Answer(ident="difficulty_concentrating", text="نعم"))
    def handle_difficulty_concentrating_yes(self):
        self.declare(Fact(ask="irritability"))

    # @Rule(Answer(ident="difficulty_concentrating", text="لا"))
    # def handle_difficulty_concentrating_no(self):
    #     self.recommend_action("النظر في مدة وبداية الأعراض")
    #     self.halt()

    @Rule(Answer(ident="irritability", text="نعم"))
    def handle_irritability_yes(self):
        self.declare(Fact(ask="sleep_difficulty"))

    @Rule(Answer(ident="irritability", text="لا"))
    def handle_irritability_no(self):
        self.recommend_action("النظر في مدة وبداية الأعراض")
        self.halt()

    @Rule(Answer(ident="sleep_difficulty", text="نعم"))
    def handle_sleep_difficulty_yes(self):
        self.declare(Fact(ask="social_occupational_impact"))

    # @Rule(Answer(ident="sleep_difficulty", text="لا"))
    # def handle_sleep_difficulty_no(self):
    #     self.recommend_action("تقديم تقنيات الاسترخاء وتحسين عادات النوم")
    #     self.halt()

    @Rule(Answer(ident="sleep_difficulty", text="لا"))
    def handle_sleep_difficulty_no(self):
        self.declare(Fact(ask="sleep_medication_stimulants"))
    
    @Rule(Answer(ident="sleep_medication_stimulants", text="نعم"))
    def handle_sleep_medication_stimulants_yes(self):
        self.recommend_action("استشارة الطبيب لتعديل الدواء أو تقليل استهلاك المنبهات")
    
    @Rule(Answer(ident="sleep_medication_stimulants", text="لا"))
    def handle_sleep_medication_stimulants_no(self):
        self.declare(Fact(ask="psychological_stress"))
    
    @Rule(Answer(ident="psychological_stress", text="نعم"))
    def handle_psychological_stress_yes(self):
        self.recommend_action("تقديم تقنيات الاسترخاء وتحسين عادات النوم")
    
    @Rule(Answer(ident="psychological_stress", text="لا"))
    def handle_psychological_stress_no(self):
        self.recommend_action("رصد الحالة وربما إجراء فحوصات إضافية للكشف عن أسباب مرضية")
    
    @Rule(Answer(ident="difficulty_concentrating", text="لا"))
    def handle_difficulty_concentrating_no(self):
        self.declare(Fact(ask="high_stress"))
    
    @Rule(Answer(ident="high_stress", text="نعم"))
    def handle_high_stress_yes(self):
        self.recommend_action("تقديم استراتيجيات لإدارة الضغط")
    
    @Rule(Answer(ident="high_stress", text="لا"))
    def handle_high_stress_no(self):
        self.declare(Fact(ask="medical_problems"))
    
    @Rule(Answer(ident="medical_problems", text="نعم"))
    def handle_medical_problems_yes(self):
        self.recommend_action("علاج المشكلة الطبية")
    
    @Rule(Answer(ident="medical_problems", text="لا"))
    def handle_medical_problems_no(self):
        self.recommend_action("رصد الحالة وتقديم دعم نفسي إذا لزم الأمر")
    
    @Rule(Answer(ident="constant_fatigue", text="لا"))
    def handle_constant_fatigue_no(self):
        self.declare(Fact(ask="fatigue_medical"))
    
    @Rule(Answer(ident="fatigue_medical", text="نعم"))
    def handle_fatigue_medical_yes(self):
        self.recommend_action("معالجة الحالة الطبية")
    
    @Rule(Answer(ident="fatigue_medical", text="لا"))
    def handle_fatigue_medical_no(self):
        self.declare(Fact(ask="sleep_insufficient"))
    
    @Rule(Answer(ident="sleep_insufficient", text="نعم"))
    def handle_sleep_insufficient_yes(self):
        self.recommend_action("تحسين نظام النوم")
    
    @Rule(Answer(ident="sleep_insufficient", text="لا"))
    def handle_sleep_insufficient_no(self):
        self.recommend_action("استكشاف الضغوط النفسية والتعامل معها")
    
    @Rule(Answer(ident="tension_irritability", text="لا"))
    def handle_tension_irritability_no(self):
        self.declare(Fact(ask="irritability_medical"))
    
    @Rule(Answer(ident="irritability_medical", text="نعم"))
    def handle_irritability_medical_yes(self):
        self.recommend_action("معالجة الحالة الطبية الأساسية")
    
    @Rule(Answer(ident="irritability_medical", text="لا"))
    def handle_irritability_medical_no(self):
        self.declare(Fact(ask="irritability_medication"))
    
    @Rule(Answer(ident="irritability_medication", text="نعم"))
    def handle_irritability_medication_yes(self):
        self.recommend_action("استشارة الطبيب لتعديل الدواء")
    
    @Rule(Answer(ident="irritability_medication", text="لا"))
    def handle_irritability_medication_no(self):
        self.recommend_action("تقديم تقنيات التقليل من الإجهاد والتحكم بالغضب")
    

    @Rule(Answer(ident="social_occupational_impact", text="نعم"))
    def handle_social_occupational_impact_yes(self):
        self.recommend_action("تشخيص اضطراب القلق العام")

    @Rule(Answer(ident="social_occupational_impact", text="لا"))
    def handle_social_occupational_impact_no(self):
        self.recommend_action("النظر في القلق دون عتبة التشخيص أو التشخيصات البديلة")

    # Agoraphobia rules
    @Rule(Answer(ident="anxiety_places", text="الأماكن العامة") |
          Answer(ident="anxiety_places", text="الأسواق") |
          Answer(ident="anxiety_places", text="الجسور") |
          Answer(ident="anxiety_places", text="وسائل النقل"))
    def handle_anxiety_places(self):
        self.declare(Fact(ask="severity_of_fear"))

    @Rule(Answer(ident="anxiety_places", text=MATCH.anxiety_places),
          NOT(Answer(ident="severity_of_fear")),
          NOT(Fact(ask="severity_of_fear")))
    def ask_severity_of_fear(self, anxiety_places):
        self.recommend_action("استبعاد الرهاب الخلوي")
        self.halt()

    @Rule(Answer(ident="severity_of_fear", text="نعم"))
    def handle_severity_of_fear_yes(self):
        self.declare(Fact(ask="daily_functioning_impact"))

    @Rule(Answer(ident="severity_of_fear", text="لا"))
    def handle_severity_of_fear_no(self):
        self.recommend_action("تقييم الحالات النفسية الأخرى")
        self.halt()

    @Rule(Answer(ident="daily_functioning_impact", text="نعم"))
    def handle_daily_functioning_impact_yes(self):
        self.recommend_action("تشخيص الرهاب الخلوي")

    @Rule(Answer(ident="daily_functioning_impact", text="لا"))
    def handle_daily_functioning_impact_no(self):
        self.recommend_action("النظر في توفير الدعم النفسي دون تشخيص رسمي")

    # Panic Disorder rules
    @Rule(Answer(ident="panic_symptoms", text="نعم"))
    def handle_panic_symptoms_yes(self):
        self.declare(Fact(ask="panic_impact"))

    @Rule(Answer(ident="panic_symptoms", text="لا"))
    def handle_panic_symptoms_no(self):
        self.recommend_action("النظر في اضطرابات القلق الأخرى أو حالات نفسية أخرى")
        self.halt()

    @Rule(Answer(ident="panic_impact", text="نعم"))
    def handle_panic_impact_yes(self):
        self.declare(Fact(ask="panic_frequency_impact"))

    @Rule(Answer(ident="panic_impact", text="لا"))
    def handle_panic_impact_no(self):
        self.recommend_action("تقييم وجود اضطرابات نفسية أخرى مماثلة")
        self.halt()

    @Rule(Answer(ident="panic_frequency_impact", text="نعم"))
    def handle_panic_frequency_impact_yes(self):
        self.recommend_action("تأكيد تشخيص اضطراب الهلع وتوفير الإحالة للعلاج")

    @Rule(Answer(ident="panic_frequency_impact", text="لا"))
    def handle_panic_frequency_impact_no(self):
        self.recommend_action("تقييم أسباب النوبات واستبعاد الحالات الطبية واستخدام المواد")

    # Social Anxiety Disorder rules
    @Rule(Answer(ident="fear_of_embarrassment", text="نعم"))
    def handle_fear_of_embarrassment_yes(self):
        self.declare(Fact(ask="social_anxiety_situations"))

    @Rule(Answer(ident="fear_of_embarrassment", text="لا"))
    def handle_fear_of_embarrassment_no(self):
        self.recommend_action("النظر في اضطرابات القلق الأخرى أو الفوبيا الخاصة")
        self.halt()

    @Rule(Answer(ident="social_anxiety_situations", text="التحدث أمام الجمهور") |
          Answer(ident="social_anxiety_situations", text="المشاركة في الاجتماعات الاجتماعية") |
          Answer(ident="social_anxiety_situations", text="تناول الطعام أمام الآخرين"))
    def handle_social_anxiety_situations(self):
        self.declare(Fact(ask="social_anxiety_severity"))

    @Rule(Answer(ident="social_anxiety_situations", text=MATCH.situations),
          NOT(Answer(ident="social_anxiety_severity")),
          NOT(Fact(ask="social_anxiety_severity")))
    def ask_social_anxiety_severity(self, situations):
        self.recommend_action("استبعاد اضطراب القلق الاجتماعي؛ تقييم اضطرابات أخرى")
        self.halt()

    @Rule(Answer(ident="social_anxiety_severity", text="نعم"))
    def handle_social_anxiety_severity_yes(self):
        self.declare(Fact(ask="social_anxiety_impact"))

    @Rule(Answer(ident="social_anxiety_severity", text="لا"))
    def handle_social_anxiety_severity_no(self):
        self.recommend_action("تقييم الحالات النفسية الأخرى")
        self.halt()

    @Rule(Answer(ident="social_anxiety_impact", text="نعم"))
    def handle_social_anxiety_impact_yes(self):
        self.recommend_action("تشخيص اضطراب القلق الاجتماعي")

    @Rule(Answer(ident="social_anxiety_impact", text="لا"))
    def handle_social_anxiety_impact_no(self):
        self.recommend_action("النظر في تقديم الدعم النفسي دون تشخيص رسمي")

    # Specific Phobia rules
    @Rule(Answer(ident="immediate_fear_response", text="نعم"))
    def handle_immediate_fear_response_yes(self):
        self.declare(Fact(ask="specific_triggers"))

    @Rule(Answer(ident="immediate_fear_response", text="لا"))
    def handle_immediate_fear_response_no(self):
        self.recommend_action("تقييم لمعرفة إذا كان الخوف متناسب مع الخطر الحقيقي")
        self.halt()

    @Rule(Answer(ident="specific_triggers", text="الحيوانات") |
          Answer(ident="specific_triggers", text="الارتفاعات") |
          Answer(ident="specific_triggers", text="الطيران") |
          Answer(ident="specific_triggers", text="رؤية الدم") |
          Answer(ident="specific_triggers", text="العواصف") |
          Answer(ident="specific_triggers", text="الظلام"))
    def handle_specific_triggers(self):
        self.declare(Fact(ask="avoidance_behavior"))

    @Rule(Answer(ident="specific_triggers", text=MATCH.triggers),
          NOT(Answer(ident="avoidance_behavior")),
          NOT(Fact(ask="avoidance_behavior")))
    def ask_avoidance_behavior(self, triggers):
        self.recommend_action("استبعاد الرهاب المحدد؛ تقييم لاضطرابات القلق الأخرى")
        self.halt()

    @Rule(Answer(ident="avoidance_behavior", text="نعم"))
    def handle_avoidance_behavior_yes(self):
        self.declare(Fact(ask="specific_phobia_impact"))

    @Rule(Answer(ident="avoidance_behavior", text="لا"))
    def handle_avoidance_behavior_no(self):
        self.recommend_action("التحقق من استمرارية الخوف وتأثيره على نوعية الحياة")
        self.halt()

    @Rule(Answer(ident="specific_phobia_impact", text="نعم"))
    def handle_specific_phobia_impact_yes(self):
        self.recommend_action("تشخيص الرهاب المحدد")

    @Rule(Answer(ident="specific_phobia_impact", text="لا"))
    def handle_specific_phobia_impact_no(self):
        self.recommend_action("النظر في العلاج النفسي للتقليل من الخوف دون تشخيص رسمي")

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
    engine = AnxietyDisordersExpertSystem()
    engine.reset()
    engine.run()
