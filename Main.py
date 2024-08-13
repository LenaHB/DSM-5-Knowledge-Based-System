from experta import *
from chapter1 import MentalHealthExpertSystem
from chapter2 import SchizophreniaSpectrumExpertSystem
from chapter3 import BipolarDisorderExpertSystem
from chapter4 import DepressiveDisordersExpertSystem
from chapter5 import AnxietyDisordersExpertSystem
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Union

# تعريف نماذج الإدخال لـ FastAPI
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
        yield Question(ident="gad_symptoms", text="هل تشعر بالقلق والتوتر أغلب الأيام لمدة 6 أشهر على الأقل؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="panic_attacks", text="هل تعاني من نوبات هلع متكررة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="social_anxiety", text="هل تخاف من التفاعل الاجتماعي أو أداء مهام تعرضه للحكم من الآخرين؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="specific_phobia", text="هل تخاف بشكل مفرط من شيء أو موقف محدد؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="agoraphobia", text="هل تخاف من وجودك في أماكن يصعب فيها الهروب أو الحصول على المساعدة؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="personality_disorder_symptoms", text="هل تعاني من أعراض اضطرابات الشخصية؟", valid=["نعم", "لا"], Type="multi")
        yield Question(ident="ocd_disorder_symptoms", text="هل تعاني من أعراض اضطرابات الوسواس القهري؟", valid=["نعم", "لا"], Type="multi")
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
        self.ask_user({"ident": id, "text": text}, Type, valid)


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
        print("Redirecting to Autism Spectrum Disorder Assessment...")
        self.chapter1.reset()
        self.chapter1.run()
        self.recommend_action("Completed Autism Spectrum Disorder Assessment")


    @Rule(Answer(ident="autism_suspected", text="لا"))
    def handle_autism_suspected_no(self):
        self.declare(Fact(ask="intellectual_disability_suspected"))

    @Rule(Fact(ask="intellectual_disability_suspected"),
          NOT(Answer(ident="intellectual_disability_suspected")))
    def ask_intellectual_disability_suspected(self):
        self.declare(Fact(ask="intellectual_disability_suspected"))

    @Rule(Answer(ident="intellectual_disability_suspected", text="نعم"))
    def handle_intellectual_disability_suspected_yes(self):
        print("Redirecting to Intellectual Disability Assessment...")
        self.chapter1.reset()
        self.chapter1.run()
        self.recommend_action("Completed Intellectual Disability Assessment")


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
        print("Redirecting to Brief Psychotic Disorder Assessment...")
        self.chapter2.reset()
        self.chapter2.run()
        self.recommend_action("Completed Brief Psychotic Disorder Assessment")

    @Rule(Answer(ident="psychotic_symptoms_duration", text="1-6 أشهر"))
    def handle_psychotic_symptoms_duration_schizophreniform(self):
        print("Redirecting to Schizophreniform Disorder Assessment...")
        self.chapter2.reset()
        self.chapter2.run()
        self.recommend_action("Completed Brief Psychotic Disorder Assessment")

    @Rule(Answer(ident="psychotic_symptoms_duration", text="أكثر من 6 أشهر"))
    def handle_psychotic_symptoms_duration_schizophrenia(self):
        print("Redirecting to Schizophrenia Assessment...")
        self.chapter2.reset()
        self.chapter2.run()
        self.recommend_action("Completed Brief Psychotic Disorder Assessment")

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
        print("Redirecting to Mood Disorders Assessment...")
        self.chapter3.reset()
        self.chapter3.run()



    @Rule(Answer(ident="mood_episodes", text="لا"))
    def handle_mood_episodes_no(self):
        self.declare(Fact(ask="depressive_disorder_suspected"))

    @Rule(Fact(ask="depressive_disorder_suspected"),
          NOT(Answer(ident="depressive_disorder_suspected")))
    def ask_depressive_disorder_suspected(self):
        self.declare(Fact(ask="depressive_disorder_suspected"))

    @Rule(Answer(ident="depressive_disorder_suspected", text="نعم"))
    def handle_depressive_disorder_suspected_yes(self):
        self.declare(Fact(ask="life_event_or_loss"))

    @Rule(Answer(ident="depressive_disorder_suspected", text="لا"))
    def handle_depressive_disorder_suspected_no(self):
        self.declare(Fact(ask="anxiety_disorder_suspected"))

    @Rule(Fact(ask="life_event_or_loss"),
          NOT(Answer(ident="life_event_or_loss")))
    def ask_life_event_or_loss(self):
        self.declare(Fact(ask="life_event_or_loss"))

    @Rule(Answer(ident="life_event_or_loss", text="نعم"))
    def handle_life_event_or_loss_yes(self):
        self.recommend_action("تقييم الحزن الطبيعي مقابل نوبة الاكتئاب الرئيسية")

    @Rule(Answer(ident="life_event_or_loss", text="لا"))
    def handle_life_event_or_loss_no(self):
        self.declare(Fact(ask="substance_use"))

    @Rule(Fact(ask="substance_use"),
          NOT(Answer(ident="substance_use")))
    def ask_substance_use(self):
        self.declare(Fact(ask="substance_use"))

    @Rule(Answer(ident="substance_use", text="نعم"))
    def handle_substance_use_yes(self):
        self.recommend_action("تقييم الاضطراب الاكتئابي المستحث بالمواد")

    @Rule(Answer(ident="substance_use", text="لا"))
    def handle_substance_use_no(self):
        self.declare(Fact(ask="persistent_depressive_symptoms"))

    @Rule(Fact(ask="persistent_depressive_symptoms"),
          NOT(Answer(ident="persistent_depressive_symptoms")))
    def ask_persistent_depressive_symptoms(self):
        self.declare(Fact(ask="persistent_depressive_symptoms"))

    @Rule(Answer(ident="persistent_depressive_symptoms", text="نعم"))
    def handle_persistent_depressive_symptoms_yes(self):
        self.recommend_action("تقييم الاضطراب الاكتئابي المستمر")

    @Rule(Answer(ident="persistent_depressive_symptoms", text="لا"))
    def handle_persistent_depressive_symptoms_no(self):
        self.recommend_action("تقييم الاضطراب الاكتئابي الرئيسي")

    @Rule(Fact(ask="anxiety_disorder_suspected"),
          NOT(Answer(ident="anxiety_disorder_suspected")))
    def ask_anxiety_disorder_suspected(self):
        self.declare(Fact(ask="anxiety_disorder_suspected"))

    @Rule(Answer(ident="anxiety_disorder_suspected", text="نعم"))
    def handle_anxiety_disorder_suspected_yes(self):
        self.declare(Fact(ask="gad_symptoms"))

    @Rule(Answer(ident="anxiety_disorder_suspected", text="لا"))
    def handle_anxiety_disorder_suspected_no(self):
        self.recommend_action("النظر في أشكال أخرى من القلق أو المشاكل الصحية")

    @Rule(Fact(ask="gad_symptoms"),
          NOT(Answer(ident="gad_symptoms")))
    def ask_gad_symptoms(self):
        self.declare(Fact(ask="gad_symptoms"))

    @Rule(Answer(ident="gad_symptoms", text="نعم"))
    def handle_gad_symptoms_yes(self):
        self.recommend_action("GAD Assessment-تقييم اضطراب القلق العام")

    @Rule(Answer(ident="gad_symptoms", text="لا"))
    def handle_gad_symptoms_no(self):
        self.declare(Fact(ask="panic_attacks"))

    @Rule(Fact(ask="panic_attacks"),
          NOT(Answer(ident="panic_attacks")))
    def ask_panic_attacks(self):
        self.declare(Fact(ask="panic_attacks"))

    @Rule(Answer(ident="panic_attacks", text="نعم"))
    def handle_panic_attacks_yes(self):
        self.recommend_action("Panic Disorder Assessment-تقييم اضطراب الهلع")

    @Rule(Answer(ident="panic_attacks", text="لا"))
    def handle_panic_attacks_no(self):
        self.declare(Fact(ask="social_anxiety"))

    @Rule(Fact(ask="social_anxiety"),
          NOT(Answer(ident="social_anxiety")))
    def ask_social_anxiety(self):
        self.declare(Fact(ask="social_anxiety"))

    @Rule(Answer(ident="social_anxiety", text="نعم"))
    def handle_social_anxiety_yes(self):
        self.recommend_action("Social Anxiety Assessment-تقييم القلق الاجتماعي")

    @Rule(Answer(ident="social_anxiety", text="لا"))
    def handle_social_anxiety_no(self):
        self.declare(Fact(ask="specific_phobia"))

    @Rule(Fact(ask="specific_phobia"),
          NOT(Answer(ident="specific_phobia")))
    def ask_specific_phobia(self):
        self.declare(Fact(ask="specific_phobia"))

    @Rule(Answer(ident="specific_phobia", text="نعم"))
    def handle_specific_phobia_yes(self):
        self.recommend_action("Specific Phobia Assessment-تقييم الرهاب المحدد")

    @Rule(Answer(ident="specific_phobia", text="لا"))
    def handle_specific_phobia_no(self):
        self.declare(Fact(ask="agoraphobia"))

    @Rule(Fact(ask="agoraphobia"),
          NOT(Answer(ident="agoraphobia")))
    def ask_agoraphobia(self):
        self.declare(Fact(ask="agoraphobia"))

    @Rule(Answer(ident="agoraphobia", text="نعم"))
    def handle_agoraphobia_yes(self):
        self.recommend_action("Agoraphobia Assessment-تقييم الرهاب الخلوي")

    @Rule(Answer(ident="agoraphobia", text="لا"))
    def handle_agoraphobia_no(self):
        self.recommend_action("النظر في أشكال أخرى من القلق أو المشاكل الصحية")

    def recommend_action(self, action):
        self.current_question = {"recommendation": action}

    def get_current_question(self):
        return self.current_question

# Initialize the expert system
engine = UnifiedExpertSystem()

@app.post("/answer", response_model=QuestionModel)
def answer_question(user_response: UserResponse):
    answer = user_response.answer
    if not engine.questions:
        raise HTTPException(status_code=400, detail="No question to answer.")
    
    current_question = engine.questions.pop(0)
    engine.declare(Answer(ident=current_question["question_id"], text=answer))
    engine.run()
    
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
        raise HTTPException(status_code=500, detail="No further questions or recommendations.")

@app.get("/start", response_model=QuestionModel)
def start_assessment():
    engine.reset()
    engine.run()
    if engine.questions:
        first_question = engine.questions[0]
        return QuestionModel(
            question_id=first_question["question_id"],
            question=first_question["question"],
            type=first_question["type"],
            valid=first_question.get("valid")
        )
    else:
        raise HTTPException(status_code=500, detail="No initial questions available.")

if __name__ == "__main__":
    app.run(app, host="0.0.0.0", port=8000)


