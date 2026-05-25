from transformers import pipeline
import random

# lightweight free model
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

def get_response(user_input):
    text = user_input.lower()

    # -----------------------
    # 💼 JOB / CAREER
    # -----------------------
    if any(word in text for word in ["job", "career", "placement", "interview", "resume"]):
        return (
            "💼 Career Roadmap:\n"
            "✔ Learn DSA (arrays, strings, trees, graphs)\n"
            "✔ Practice coding daily (LeetCode/HackerRank)\n"
            "✔ Build 2–3 real projects (chatbot, ML, web apps)\n"
            "✔ Upload projects on GitHub\n"
            "✔ Improve resume + LinkedIn profile\n"
            "✔ Apply on job portals regularly\n"
        )

    # -----------------------
    # 💻 CODING
    # -----------------------
    if any(word in text for word in ["code", "coding", "python", "programming", "algorithm"]):
        return (
            "💻 Coding Plan:\n"
            "✔ Start with Python basics\n"
            "✔ Learn loops, functions, arrays\n"
            "✔ Practice problem solving daily\n"
            "✔ Focus on logic building, not memorization\n"
        )

    # -----------------------
    # 🧠 STUDY / LEARNING
    # -----------------------
    if any(word in text for word in ["study", "learn", "exam"]):
        return (
            "📚 Study Tips:\n"
            "✔ Make daily study plan\n"
            "✔ Focus on understanding, not memorizing\n"
            "✔ Practice regularly\n"
            "✔ Revise frequently\n"
        )

    # -----------------------
    # 🏥 HEALTH
    # -----------------------
    if any(word in text for word in ["headache", "fever", "pain", "sick"]):
        return (
            "🩺 Health Advice:\n"
            "✔ Drink water and rest\n"
            "✔ Avoid screen for some time\n"
            "✔ Sleep properly\n"
            "⚠ If it continues, consult a doctor\n"
        )

    # -----------------------
    # 👋 GREETING
    # -----------------------
    if any(word in text for word in ["hi", "hello", "hey"]):
        return "Hello 👋 How can I help you today?"

    # -----------------------
    # 🤖 AI FALLBACK (GENERAL CHAT)
    # -----------------------
    response = chatbot(
        user_input,
        max_length=80,
        do_sample=True,
        temperature=0.7
    )

    return response[0]["generated_text"]