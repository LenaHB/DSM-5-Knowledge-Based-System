import logging
from experta import *
from chapter1 import MentalHealthExpertSystem
from chapter2 import SchizophreniaSpectrumExpertSystem
from chapter3 import BipolarDisorderExpertSystem
from chapter4 import DepressiveDisordersExpertSystem
from chapter5 import AnxietyDisordersExpertSystem
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Union

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

app = FastAPI()

class GeneralAssessment(Fact):
    """Fact to represent initial general assessment."""
    pass

class NeurodevelopmentalDisorder(Fact):
    """Check if neurodevelopmental disorder evaluation is needed."""
    pass

class PsychoticDisorder(Fact):
    """Check if psychotic disorder evaluation is needed."""
    pass

class MoodDisorder(Fact):
    """Check if mood disorder evaluation is needed."""
    pass

class DepressiveDisorder(Fact):
    """Check if depressive disorder evaluation is needed."""
    pass

class AnxietyDisorder(Fact):
    """Check if anxiety disorder evaluation is needed."""
    pass

class PersonalityDisorder(Fact):
    """Check if personality disorder evaluation is needed."""
    pass

class OCDDisorder(Fact):
    """Check if OCD or related disorder evaluation is needed."""
    pass


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

class SchizophreniaSpectrumDisorder(Fact):
    """Fact to check for Schizophrenia Spectrum Disorders"""
    pass





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



class OCD(Fact):
    """Fact to check if OCD is present"""
    pass

class BodyDysmorphicDisorder(Fact):
    """Fact to check if Body Dysmorphic Disorder is present"""
    pass

class HoardingDisorder(Fact):
    """Fact to check if Hoarding Disorder is present"""
    pass

class Trichotillomania(Fact):
    """Fact to check if Trichotillomania is present"""
    pass

class ExcoriationDisorder(Fact):
    """Fact to check if Excoriation Disorder is present"""
    pass




class Question(Fact):
    """Fact to represent a question"""
    pass

class Answer(Fact):
    """Fact to represent an answer"""
    pass

class UnifiedExpertSystem(KnowledgeEngine):
    @DefFacts()
    def init(self):
        """Initialize with the main entry point questions and the triggering fact."""
        yield Question(ident="general_assessment_needed", text="هل تحتاج إلى تقييم الأعراض العامة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="autism_suspected", text="هل يشتبه في وجود اضطراب طيف التوحد؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="intellectual_disability_suspected", text="هل يشتبه في وجود إعاقة ذهنية؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="psychotic_symptoms", text="هل تعاني من أعراض ذهانية؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="psychotic_symptoms_duration", text="ما هي مدة الأعراض الذهانية؟", valid=["أقل من شهر", "1-6 أشهر", "أكثر من 6 أشهر"], Type="multi")
        yield Question(ident="mood_disorder_suspected", text="هل يشتبه في اضطرابات المزاج؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="mood_episodes", text="هل تعاني من نوبات هوسية أو اكتئابية؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="depressive_disorder_suspected", text="هل يشتبه في اضطرابات اكتئابية؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="life_event_or_loss", text="هل الأعراض تتعلق بحدث حياتي كبير أو خسارة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="substance_use", text="هل هناك استخدام مواد يمكن أن يفسر الأعراض؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="persistent_depressive_symptoms", text="هل الأعراض شديدة ومستمرة لأكثر من سنتين؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="anxiety_disorder_suspected", text="هل يشتبه في اضطرابات القلق؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="gad_symptoms", text="هل تشعر  بالقلق والتوتر أغلب الأيام لمدة 6 أشهر على الأقل؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="panic_attacks", text="هل تعاني  من نوبات هلع متكررة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="social_anxiety", text="هل تخاف  من التفاعل الاجتماعي أو أداء مهام تعرضك للحكم من الآخرين؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="specific_phobia", text="هل تخاف  بشكل مفرط من شيء أو موقف محدد؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="agoraphobia", text="هل تخاف  من وجوده في أماكن يصعب فيها الهروب أو الحصول على المساعدة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="personality_disorder_symptoms", text="هل تعاني المريض من أعراض اضطرابات", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="ocd_disorder_symptoms", text="هل تعاني المريض من أعراض اضطرابات الوسواس القهري؟", valid=["نعم", "لا"], Type="multi")
        
        
        yield Question(ident="developmental", text="هل لاحظت تخلفاً عن معالم التطور أو لديك سلوكيات غير معتادة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="social", text="هل لوحظت عيوب اجتماعية أو سلوكيات متكررة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="academic", text="هل تواجه صعوبة في المواد الأكاديمية مثل القراءة أو الرياضيات، وهل يؤثر ذلك على قدرتك على تلبية التوقعات المتعلقة بالعمر؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="reading", text="هل تعاني  من صعوبات في القراءة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="writing", text="هل تعاني من صعوبات في الكتابة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="math", text="هل تعاني من صعوبات في الرياضيات؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="social_interactions", text="هل لديك مشاكل في التفاعلات الاجتماعية؟", valid=["نعم", "لا"], Type="multi")

        

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
        yield Question(ident="schizophreniform_functional_impact", text="هل تسبب الأعراض تأثيراً كبيراً على الحياة الاجتماعية أوالمهنية؟", valid=["نعم", "لا"], Type="multi")

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




        yield Question(ident="manic_episode", text="هل تعاني من نوبات هوس قوية؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="hypomanic_episode", text="هل تعاني من نوبات هوس خفيف؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="persistent_depressive_disorder", text="هل تعاني من اكتئاب مستمر؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="substance_induced", text="هل هناك أعراض ناتجة عن مواد أو دواء؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="medical_condition", text="هل توجد حالة طبية أخرى تسبب الأعراض؟", valid=["نعم", "لا"], Type="multi")



        yield Question(ident="main_event_related", text="هل الأعراض تتعلق بحدث حياتي كبير أو خسارة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="substance_use_related", text="هل هناك استخدام مواد يمكن أن يفسر الأعراض؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="persistent_depressive_mood", text="هل الأعراض شديدة ومستمرة لأكثر من سنتين؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="premenstrual_related", text="هل الأعراض تتفاقم خلال فترة ما قبل الحيض؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="major_depressive_mood", text="هل تعاني  من مزاج مكتئب معظم اليوم، تقريبا كل يوم، لمدة أسبوعين على الأقل؟", valid=["نعم", "لا"], Type="multi")
        
        yield Question(ident="depressive_mood", text="هل تعاني من مزاج مكتئب لمدة سنتين أو أكثر؟", valid=["نعم", "لا"], Type="multi")
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




        yield Question(ident="main_anxiety", text="هل تشعر بالقلق والتوتر أغلب الأيام لمدة 6 أشهر على الأقل؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="panic_attacks", text="هل تعاني من نوبات هلع متكررة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="social_anxiety", text="هل تخاف من التفاعل الاجتماعي أو أداء مهام تعرضه للحكم من الآخرين؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="specific_phobia", text="هل تخاف بشكل مفرط من شيء أو موقف محدد؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="fear_of_open_crowded_places", text="هل تخاف من وجوده في أماكن يصعب فيها الهروب أو الحصول على المساعدة؟", valid=["نعم", "لا"], Type="multi")

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
        yield Question(ident="severity_of_fear", text="هل تتجنب هذه الأماكن أو تعاني من القلق الشديد عند التعرض لها؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="daily_functioning_impact", text="هل يؤثر هذا الخوف بشكل كبير على حياتك اليومية أو عمله؟", valid=["نعم", "لا"], Type="multi")

        # Questions for Panic Disorder
        yield Question(ident="panic_symptoms", text="تحديد الأعراض خلال النوبات: تسارع القلب، تعرق، رعشة، إحساس بالاختناق، ألم الصدر، الغثيان، دوار، خوف من الموت أو الجنون أو فقدان السيطرة", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="panic_impact", text="هل تتبع النوبات قلقاً بشأن حدوث نوبات أخرى أو عواقب النوبات، أو تغيرات سلوكية كبيرة متعلقة بالنوبات؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="panic_frequency_impact", text="هل تؤدي النوبات إلى قلق دائم ومخاوف من حدوث نوبات مستقبلية أو عواقبها؟", valid=["نعم", "لا"], Type="multi")

        # Questions for Social Anxiety Disorder
        yield Question(ident="fear_of_embarrassment", text="هل هناك خوف من التصرف بطريقة معينة أو إظهار أعراض القلق التي قد تكون محرجة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="social_anxiety_situations", text="ما هي المواقف التي تثير لديك القلق؟ (التحدث أمام الجمهور، المشاركة في الاجتماعات الاجتماعية، تناول الطعام أمام الآخرين)", valid=["التحدث أمام الجمهور", "المشاركة في الاجتماعات الاجتماعية", "تناول الطعام أمام الآخرين"], Type="multi")
        yield Question(ident="social_anxiety_severity", text="هل تتجنب المواقف أو تتحملها بقلق شديد؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="social_anxiety_impact", text="هل يؤثر الخوف بشكل كبير على حياتك اليومية؟", valid=["نعم", "لا"], Type="multi")

        # Questions for Specific Phobia
        yield Question(ident="immediate_fear_response", text="هل يظهر الخوف فوراً عند التعرض للمحفز؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="specific_triggers", text="ما هي المحفزات الخاصة بالرهاب؟ (الحيوانات، الارتفاعات، الطيران، رؤية الدم، العواصف، الظلام)", valid=["الحيوانات", "الارتفاعات", "الطيران", "رؤية الدم", "العواصف", "الظلام"], Type="multi")
        yield Question(ident="avoidance_behavior", text="هل تتجنب بشكل نشط أو يتحمل بشدة المواقف أو الأشياء المخيفة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="specific_phobia_impact", text="هل يؤثر الخوف بشكل كبير على حياتك اليومية؟", valid=["نعم", "لا"], Type="multi")


        yield Question(ident="ocd_suspected", text="هل يشتبه في اضطراب الوسواس القهري (OCD)؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="body_dysmorphic_suspected", text="هل يشتبه في اضطراب تشوه الجسم؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="hoarding_suspected", text="هل يشتبه في اضطراب التخزين؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="trichotillomania_suspected", text="هل يشتبه في هوس نتف الشعر؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="excoriation_suspected", text="هل يشتبه في اضطراب تقشير الجلد؟", valid=["نعم", "لا"], Type="multi")
        # New questions based on detailed flowcharts
        yield Question(ident="ocd_obsessions", text="هل تعاني من وساوس؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="ocd_compulsions", text="هل تعاني من أفعال قهرية؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="ocd_impact", text="هل تستغرق الأعراض وقتاً طويلاً أو تسبب ضيقاً كبيراً أو تأثيراً على الأداء؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="body_dysmorphic_concerns", text="هل هناك انشغال بالعيوب المتصورة في المظهر؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="body_dysmorphic_behaviors", text="هل هناك سلوكيات متكررة أو أفعال عقلية استجابة لمخاوف المظهر؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="body_dysmorphic_impact", text="هل تسبب الأعراض ضيقاً كبيراً أو تأثيراً على الأداء؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="difficulty_discarding", text="هل هناك صعوبة في التخلص من الممتلكات؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="hoarding_accumulation", text="هل هناك تراكم للممتلكات التي تملأ المناطق المعيشية؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="hoarding_impact", text="هل تسبب الأعراض ضيقاً كبيراً أو تأثيراً على الأداء؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="hair_pulling", text="هل تعاني من نتف الشعر المتكرر؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="hair_pulling_attempts", text="هل قمت بمحاولات متكررة للتقليل أو التوقف عن نتف الشعر؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="trichotillomania_impact", text="هل تسبب الأعراض ضيقاً كبيراً أو تأثيراً على الأداء؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="skin_picking", text="هل تعاني من تقشير الجلد المتكرر مما يسبب إصابات جلدية؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="skin_picking_attempts", text="هل قمت بمحاولات متكررة للتقليل أو التوقف عن تقشير الجلد؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="excoriation_impact", text="هل تسبب الأعراض ضيقاً كبيراً أو تأثيراً على الأداء؟", valid=["نعم", "لا"], Type="multi")


        yield Fact(ask="general_assessment_needed")  # Trigger the initial question





    def __init__(self):
        super().__init__()
        self.chapter1 = MentalHealthExpertSystem()
        self.chapter2 = SchizophreniaSpectrumExpertSystem()
        self.chapter3 = BipolarDisorderExpertSystem()
        self.chapter4 = DepressiveDisordersExpertSystem()
        self.chapter5 = AnxietyDisordersExpertSystem()
        # self.chapter6 = PersonalityDisordersExpertSystem()
        # self.chapter7 = OCDandRelatedDisordersExpertSystem()
        self.questions = []
        self.recommendations = []

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
        answer = self.ask_user({"ident": id, "text": text}, Type, valid)
        self.declare(Answer(ident=id, text=answer))


    @Rule(Fact(ask="general_assessment_needed"),
          NOT(Answer(ident="general_assessment_needed")))
    def ask_general_assessment_needed(self):
        self.declare(Fact(ask="general_assessment_needed"))

    @Rule(Answer(ident="general_assessment_needed", text="نعم"))
    def handle_general_assessment_needed_yes(self):
        self.declare(Fact(ask="autism_suspected"))

    @Rule(Answer(ident="general_assessment_needed", text="لا"))
    def handle_general_assessment_needed_no(self):
        self.declare(Fact(ask="psychotic_symptoms"))

    @Rule(Fact(ask="autism_suspected"),
          NOT(Answer(ident="autism_suspected")))
    def ask_autism_suspected(self):
        self.declare(Fact(ask="autism_suspected"))

    @Rule(Answer(ident="autism_suspected", text="نعم"))
    def handle_autism_suspected_yes(self):
        self.declare(Fact(ask="developmental"))

    @Rule(Answer(ident="autism_suspected", text="لا"))
    def handle_autism_suspected_no(self):
        self.declare(Fact(ask="intellectual_disability_suspected"))

    @Rule(Fact(ask="intellectual_disability_suspected"),
          NOT(Answer(ident="intellectual_disability_suspected")))
    def ask_intellectual_disability_suspected(self):
        self.declare(Fact(ask="intellectual_disability_suspected"))

    @Rule(Answer(ident="intellectual_disability_suspected", text="نعم"))
    def handle_intellectual_disability_suspected_yes(self):
        self.declare(Fact(ask="developmental"))

#------------------------------------Chapter1-------------------------------------------
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
        self.declare(Question(ident="academic_challenges", text="هل لديك صعوبة في المواد الدراسية مثل القراءة أو الرياضيات، وهل يؤثر هذا على قدرتك على تلبية توقعات العمر؟", valid=["نعم", "لا"], Type="multi"))

    @Rule(Answer(ident="academic_challenges", text="نعم"))
    def handle_academic_challenges_yes(self):
        self.declare(Fact(ask="word_reading"))

    @Rule(Answer(ident="academic_challenges", text="لا"))
    def handle_academic_challenges_no(self):
        self.recommend_action("لا يوجد عجز مفاهيمي كبير. يفي بالتوقعات العمرية الأكاديمية.")
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
        self.declare(Question(ident="number_sense", text="هل تعاني من صعوبات في فهم الأرقام أو العمليات الحسابية؟", valid=["نعم", "لا"], Type="multi"))

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





#------------------------------------Chapter1-------------------------------------------








    @Rule(Answer(ident="intellectual_disability_suspected", text="لا"))
    def handle_intellectual_disability_suspected_no(self):
        self.recommend_action("النظر في حالات أو تقييمات أخرى")

    @Rule(Fact(ask="psychotic_symptoms"),
          NOT(Answer(ident="psychotic_symptoms")))
    def ask_psychotic_symptoms(self):
        self.declare(Fact(ask="psychotic_symptoms"))

    @Rule(Answer(ident="psychotic_symptoms", text="نعم"))
    def handle_psychotic_symptoms_yes(self):
        self.declare(Fact(ask="psychotic_symptoms_duration"))

    @Rule(Answer(ident="psychotic_symptoms", text="لا"))
    def handle_psychotic_symptoms_no(self):
        self.declare(Fact(ask="mood_disorder_suspected"))

    @Rule(Fact(ask="psychotic_symptoms_duration"),
          NOT(Answer(ident="psychotic_symptoms_duration")))
    def ask_psychotic_symptoms_duration(self):
        self.declare(Fact(ask="psychotic_symptoms_duration"))

    @Rule(Answer(ident="psychotic_symptoms_duration", text="أقل من شهر"))
    def handle_psychotic_symptoms_duration_brief(self):
        self.declare(Fact(ask="psychotic_symptoms"))

    @Rule(Answer(ident="psychotic_symptoms_duration", text="1-6 أشهر"))
    def handle_psychotic_symptoms_duration_schizophreniform(self):
        self.declare(Fact(ask="schizophreniform_delusions"))


    @Rule(Answer(ident="psychotic_symptoms_duration", text="أكثر من 6 أشهر"))
    def handle_psychotic_symptoms_duration_schizophrenia(self):
        self.declare(Fact(ask="schizophreniform_delusions"))


#------------------------------------Chapter2-------------------------------------------



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

#------------------------------------Chapter2-------------------------------------------










    @Rule(Fact(ask="mood_disorder_suspected"),
          NOT(Answer(ident="mood_disorder_suspected")))
    def ask_mood_disorder_suspected(self):
        self.declare(Fact(ask="mood_disorder_suspected"))

    @Rule(Answer(ident="mood_disorder_suspected", text="نعم"))
    def handle_mood_disorder_suspected_yes(self):
        self.declare(Fact(ask="mood_episodes"))

    @Rule(Answer(ident="mood_disorder_suspected", text="لا"))
    def handle_mood_disorder_suspected_no(self):
        self.declare(Fact(ask="depressive_disorder_suspected"))

    @Rule(Fact(ask="mood_episodes"),
          NOT(Answer(ident="mood_episodes")))
    def ask_mood_episodes(self):
        self.declare(Fact(ask="mood_episodes"))

    @Rule(Answer(ident="mood_episodes", text="نعم"))
    def handle_mood_episodes_yes(self):
        self.declare(Fact(ask="manic_episode"))


#------------------------------------Chapter3-------------------------------------------

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
        self.declare(Question(ident="Bipolar_I_Disorder_Diagnostic", text="هل تعاني الشخص من نوبة هوسية تتميز بمزاج مرتفع أو متوسع أو متهيج مستمر ونشاط موجه لأهداف متزايد بشكل غير طبيعي؟", valid=["نعم", "لا"], Type="multi"))

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
        self.declare(Question(ident="Bipolar_II_Disorder_Diagnostic", text="هل تعاني الشخص من نوبة هوس خفيف واحدة على الأقل؟", valid=["نعم", "لا"], Type="multi"))

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



#------------------------------------Chapter3-------------------------------------------



    @Rule(Answer(ident="mood_episodes", text="لا"))
    def handle_mood_episodes_no(self):
        self.declare(Fact(ask="depressive_disorder_suspected"))

    @Rule(Fact(ask="depressive_disorder_suspected"),
          NOT(Answer(ident="depressive_disorder_suspected")))
    def ask_depressive_disorder_suspected(self):
        self.declare(Fact(ask="depressive_disorder_suspected"))

    @Rule(Answer(ident="depressive_disorder_suspected", text="نعم"))
    def handle_depressive_disorder_suspected_yes(self):
        self.declare(Fact(ask="main_event_related"))

#------------------------------------Chapter4-------------------------------------------

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


#------------------------------------Chapter4-------------------------------------------
















    @Rule(Answer(ident="depressive_disorder_suspected", text="لا"))
    def handle_depressive_disorder_suspected_no(self):
        self.declare(Fact(ask="anxiety_disorder_suspected"))

    @Rule(Fact(ask="anxiety_disorder_suspected"),
          NOT(Answer(ident="anxiety_disorder_suspected")))
    def ask_anxiety_disorder_suspected(self):
        self.declare(Fact(ask="anxiety_disorder_suspected"))

    @Rule(Answer(ident="anxiety_disorder_suspected", text="نعم"))
    def handle_anxiety_disorder_suspected_yes(self):
        self.declare(Fact(ask="main_anxiety"))


#------------------------------------Chapter5-------------------------------------------

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

#------------------------------------Chapter5-------------------------------------------















    @Rule(Answer(ident="anxiety_disorder_suspected", text="لا"))
    def handle_anxiety_disorder_suspected_no(self):
        self.declare(Fact(ask="ocd_suspected"))

    @Rule(Fact(ask="ocd_suspected"),
          NOT(Answer(ident="ocd_suspected")))
    def ask_ocd_suspected(self):
        self.declare(Fact(ask="ocd_suspected"))

    @Rule(Answer(ident="ocd_suspected", text="نعم"))
    def handle_ocd_suspected_yes(self):
        self.declare(Fact(ask="ocd_suspected"))



#------------------------------------Chapter6-------------------------------------------

    @Rule(Fact(ask="ocd_suspected"),
          NOT(Answer(ident="ocd_suspected")))
    def ask_ocd_suspected(self):
        self.declare(Fact(ask="ocd_suspected"))

    @Rule(Answer(ident="ocd_suspected", text="نعم"))
    def handle_ocd_suspected_yes(self):
        self.declare(Fact(ask="ocd_obsessions"))

    @Rule(Answer(ident="ocd_suspected", text="لا"))
    def handle_ocd_suspected_no(self):
        self.declare(Fact(ask="body_dysmorphic_suspected"))

    @Rule(Fact(ask="body_dysmorphic_suspected"),
          NOT(Answer(ident="body_dysmorphic_suspected")))
    def ask_body_dysmorphic_suspected(self):
        self.declare(Fact(ask="body_dysmorphic_suspected"))

    @Rule(Answer(ident="body_dysmorphic_suspected", text="نعم"))
    def handle_body_dysmorphic_suspected_yes(self):
        self.declare(Fact(ask="body_dysmorphic_concerns"))

    @Rule(Answer(ident="body_dysmorphic_suspected", text="لا"))
    def handle_body_dysmorphic_suspected_no(self):
        self.declare(Fact(ask="hoarding_suspected"))

    @Rule(Fact(ask="hoarding_suspected"),
          NOT(Answer(ident="hoarding_suspected")))
    def ask_hoarding_suspected(self):
        self.declare(Fact(ask="hoarding_suspected"))

    @Rule(Answer(ident="hoarding_suspected", text="نعم"))
    def handle_hoarding_suspected_yes(self):
        self.declare(Fact(ask="difficulty_discarding"))

    @Rule(Answer(ident="hoarding_suspected", text="لا"))
    def handle_hoarding_suspected_no(self):
        self.declare(Fact(ask="trichotillomania_suspected"))

    @Rule(Fact(ask="trichotillomania_suspected"),
          NOT(Answer(ident="trichotillomania_suspected")))
    def ask_trichotillomania_suspected(self):
        self.declare(Fact(ask="trichotillomania_suspected"))

    @Rule(Answer(ident="trichotillomania_suspected", text="نعم"))
    def handle_trichotillomania_suspected_yes(self):
        self.declare(Fact(ask="hair_pulling"))

    @Rule(Answer(ident="trichotillomania_suspected", text="لا"))
    def handle_trichotillomania_suspected_no(self):
        self.declare(Fact(ask="excoriation_suspected"))

    @Rule(Fact(ask="excoriation_suspected"),
          NOT(Answer(ident="excoriation_suspected")))
    def ask_excoriation_suspected(self):
        self.declare(Fact(ask="excoriation_suspected"))

    @Rule(Answer(ident="excoriation_suspected", text="نعم"))
    def handle_excoriation_suspected_yes(self):
        self.declare(Fact(ask="skin_picking"))

    @Rule(Answer(ident="excoriation_suspected", text="لا"))
    def handle_excoriation_suspected_no(self):
        self.recommend_action("النظر في أشكال أخرى من القلق أو المشاكل الصحية")
        self.halt()

    # OCD Detailed
    @Rule(Fact(ask="ocd_obsessions"),
          NOT(Answer(ident="ocd_obsessions")))
    def ask_ocd_obsessions(self):
        self.declare(Fact(ask="ocd_obsessions"))

    @Rule(Answer(ident="ocd_obsessions", text="نعم"))
    def handle_ocd_obsessions_yes(self):
        self.declare(Fact(ask="ocd_compulsions"))

    @Rule(Answer(ident="ocd_obsessions", text="لا"))
    def handle_ocd_obsessions_no(self):
        self.declare(Fact(ask="ocd_compulsions"))

    @Rule(Fact(ask="ocd_compulsions"),
          NOT(Answer(ident="ocd_compulsions")))
    def ask_ocd_compulsions(self):
        self.declare(Fact(ask="ocd_compulsions"))

    @Rule(Answer(ident="ocd_compulsions", text="نعم"))
    def handle_ocd_compulsions_yes(self):
        self.declare(Fact(ask="ocd_impact"))

    @Rule(Answer(ident="ocd_compulsions", text="لا"))
    def handle_ocd_compulsions_no(self):
        self.recommend_action("إعادة تقييم لاضطرابات ذات صلة أخرى")
        self.halt()

    @Rule(Fact(ask="ocd_impact"),
          NOT(Answer(ident="ocd_impact")))
    def ask_ocd_impact(self):
        self.declare(Fact(ask="ocd_impact"))

    @Rule(Answer(ident="ocd_impact", text="نعم"))
    def handle_ocd_impact_yes(self):
        self.recommend_action("تشخيص اضطراب الوسواس القهري")
        self.halt()

    @Rule(Answer(ident="ocd_impact", text="لا"))
    def handle_ocd_impact_no(self):
        self.recommend_action("النظر في أعراض تحت السريرية أو اضطرابات أخرى")
        self.halt()

    # Body Dysmorphic Disorder Detailed
    @Rule(Fact(ask="body_dysmorphic_concerns"),
          NOT(Answer(ident="body_dysmorphic_concerns")))
    def ask_body_dysmorphic_concerns(self):
        self.declare(Fact(ask="body_dysmorphic_concerns"))

    @Rule(Answer(ident="body_dysmorphic_concerns", text="نعم"))
    def handle_body_dysmorphic_concerns_yes(self):
        self.declare(Fact(ask="body_dysmorphic_behaviors"))

    @Rule(Answer(ident="body_dysmorphic_concerns", text="لا"))
    def handle_body_dysmorphic_concerns_no(self):
        self.recommend_action("النظر في اضطرابات أخرى")
        self.halt()

    @Rule(Fact(ask="body_dysmorphic_behaviors"),
          NOT(Answer(ident="body_dysmorphic_behaviors")))
    def ask_body_dysmorphic_behaviors(self):
        self.declare(Fact(ask="body_dysmorphic_behaviors"))

    @Rule(Answer(ident="body_dysmorphic_behaviors", text="نعم"))
    def handle_body_dysmorphic_behaviors_yes(self):
        self.declare(Fact(ask="body_dysmorphic_impact"))

    @Rule(Answer(ident="body_dysmorphic_behaviors", text="لا"))
    def handle_body_dysmorphic_behaviors_no(self):
        self.recommend_action("النظر في اضطرابات أخرى")
        self.halt()

    @Rule(Fact(ask="body_dysmorphic_impact"),
          NOT(Answer(ident="body_dysmorphic_impact")))
    def ask_body_dysmorphic_impact(self):
        self.declare(Fact(ask="body_dysmorphic_impact"))

    @Rule(Answer(ident="body_dysmorphic_impact", text="نعم"))
    def handle_body_dysmorphic_impact_yes(self):
        self.recommend_action("تشخيص اضطراب تشوه الجسم")
        self.halt()

    @Rule(Answer(ident="body_dysmorphic_impact", text="لا"))
    def handle_body_dysmorphic_impact_no(self):
        self.recommend_action("النظر في اضطرابات أخرى")
        self.halt()

    # Hoarding Disorder Detailed
    @Rule(Fact(ask="difficulty_discarding"),
          NOT(Answer(ident="difficulty_discarding")))
    def ask_difficulty_discarding(self):
        self.declare(Fact(ask="difficulty_discarding"))

    @Rule(Answer(ident="difficulty_discarding", text="نعم"))
    def handle_difficulty_discarding_yes(self):
        self.declare(Fact(ask="hoarding_accumulation"))

    @Rule(Answer(ident="difficulty_discarding", text="لا"))
    def handle_difficulty_discarding_no(self):
        self.recommend_action("النظر في اضطرابات أخرى")
        self.halt()

    @Rule(Fact(ask="hoarding_accumulation"),
          NOT(Answer(ident="hoarding_accumulation")))
    def ask_hoarding_accumulation(self):
        self.declare(Fact(ask="hoarding_accumulation"))

    @Rule(Answer(ident="hoarding_accumulation", text="نعم"))
    def handle_hoarding_accumulation_yes(self):
        self.declare(Fact(ask="hoarding_impact"))

    @Rule(Answer(ident="hoarding_accumulation", text="لا"))
    def handle_hoarding_accumulation_no(self):
        self.recommend_action("النظر في اضطرابات أخرى")
        self.halt()

    @Rule(Fact(ask="hoarding_impact"),
          NOT(Answer(ident="hoarding_impact")))
    def ask_hoarding_impact(self):
        self.declare(Fact(ask="hoarding_impact"))

    @Rule(Answer(ident="hoarding_impact", text="نعم"))
    def handle_hoarding_impact_yes(self):
        self.recommend_action("تشخيص اضطراب التخزين")
        self.halt()

    @Rule(Answer(ident="hoarding_impact", text="لا"))
    def handle_hoarding_impact_no(self):
        self.recommend_action("النظر في اضطرابات أخرى")
        self.halt()

    # Trichotillomania Detailed
    @Rule(Fact(ask="hair_pulling"),
          NOT(Answer(ident="hair_pulling")))
    def ask_hair_pulling(self):
        self.declare(Fact(ask="hair_pulling"))

    @Rule(Answer(ident="hair_pulling", text="نعم"))
    def handle_hair_pulling_yes(self):
        self.declare(Fact(ask="hair_pulling_attempts"))

    @Rule(Answer(ident="hair_pulling", text="لا"))
    def handle_hair_pulling_no(self):
        self.recommend_action("النظر في اضطرابات أخرى")
        self.halt()

    @Rule(Fact(ask="hair_pulling_attempts"),
          NOT(Answer(ident="hair_pulling_attempts")))
    def ask_hair_pulling_attempts(self):
        self.declare(Fact(ask="hair_pulling_attempts"))

    @Rule(Answer(ident="hair_pulling_attempts", text="نعم"))
    def handle_hair_pulling_attempts_yes(self):
        self.declare(Fact(ask="trichotillomania_impact"))

    @Rule(Answer(ident="hair_pulling_attempts", text="لا"))
    def handle_hair_pulling_attempts_no(self):
        self.recommend_action("النظر في اضطرابات أخرى")
        self.halt()

    @Rule(Fact(ask="trichotillomania_impact"),
          NOT(Answer(ident="trichotillomania_impact")))
    def ask_trichotillomania_impact(self):
        self.declare(Fact(ask="trichotillomania_impact"))

    @Rule(Answer(ident="trichotillomania_impact", text="نعم"))
    def handle_trichotillomania_impact_yes(self):
        self.recommend_action("تشخيص هوس نتف الشعر")
        self.halt()

    @Rule(Answer(ident="trichotillomania_impact", text="لا"))
    def handle_trichotillomania_impact_no(self):
        self.recommend_action("النظر في اضطرابات أخرى")
        self.halt()

    # Excoriation Disorder Detailed
    @Rule(Fact(ask="skin_picking"),
          NOT(Answer(ident="skin_picking")))
    def ask_skin_picking(self):
        self.declare(Fact(ask="skin_picking"))

    @Rule(Answer(ident="skin_picking", text="نعم"))
    def handle_skin_picking_yes(self):
        self.declare(Fact(ask="skin_picking_attempts"))

    @Rule(Answer(ident="skin_picking", text="لا"))
    def handle_skin_picking_no(self):
        self.recommend_action("النظر في اضطرابات أخرى")
        self.halt()

    @Rule(Fact(ask="skin_picking_attempts"),
          NOT(Answer(ident="skin_picking_attempts")))
    def ask_skin_picking_attempts(self):
        self.declare(Fact(ask="skin_picking_attempts"))

    @Rule(Answer(ident="skin_picking_attempts", text="نعم"))
    def handle_skin_picking_attempts_yes(self):
        self.declare(Fact(ask="excoriation_impact"))

    @Rule(Answer(ident="skin_picking_attempts", text="لا"))
    def handle_skin_picking_attempts_no(self):
        self.recommend_action("النظر في اضطرابات أخرى")
        self.halt()

    @Rule(Fact(ask="excoriation_impact"),
          NOT(Answer(ident="excoriation_impact")))
    def ask_excoriation_impact(self):
        self.declare(Fact(ask="excoriation_impact"))

    @Rule(Answer(ident="excoriation_impact", text="نعم"))
    def handle_excoriation_impact_yes(self):
        self.recommend_action("تشخيص اضطراب تقشير الجلد")
        self.halt()

    @Rule(Answer(ident="excoriation_impact", text="لا"))
    def handle_excoriation_impact_no(self):
        self.recommend_action("النظر في اضطرابات أخرى")
        self.halt()


#------------------------------------Chapter6-------------------------------------------



    @Rule(Answer(ident="ocd_suspected", text="لا"))
    def handle_ocd_suspected_no(self):
        self.declare(Fact(ask="personality_disorder_suspected"))













    def recommend_action(self, action):
        self.recommendations.append(action)

    def get_current_question(self):
        return self.questions[0] if self.questions else None

# Initialize the expert system
engine = UnifiedExpertSystem()

@app.post("/answer/", response_model=Union[QuestionModel, RecommendationModel])
def answer_question(user_response: UserResponse):
    answer = user_response.answer
    if not engine.questions:
        raise HTTPException(status_code=400, detail="No question to answer.")
    
    current_question = engine.questions.pop(0)
    engine.declare(Answer(ident=current_question["question_id"], text=answer))
    engine.run()
    
    if engine.subchapter_active:
        engine.run_chapter()  # Run the chapter if it's currently active
    
    if engine.recommendations:
        recommendation = engine.recommendations.pop(0)
        return RecommendationModel(recommendation=recommendation)
    elif engine.questions:
        next_question = engine.questions[0]
        return QuestionModel(
            question_id=next_question["question_id"],
            question=next_question["question"],
            type=next_question["type"],
            valid=next_question.get("valid")
        )
    else:
        logging.error("No further questions or recommendations.")
        raise HTTPException(status_code=500, detail="No further questions or recommendations.")

@app.post("/start", response_model=Union[QuestionModel, RecommendationModel])
def start_session():
    engine.reset()
    engine.subchapter_active = False  # Reset subchapter state
    engine.run()
    if engine.questions:
        first_question = engine.questions[0]
        return QuestionModel(
            question_id=first_question["question_id"],
            question=first_question["question"],
            type=first_question["type"],
            valid=first_question.get("valid")
        )
    elif engine.recommendations:
        recommendation = engine.recommendations[0]
        return RecommendationModel(recommendation=recommendation)
    else:
        raise HTTPException(status_code=500, detail="No initial questions available.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
