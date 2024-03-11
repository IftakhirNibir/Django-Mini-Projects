from django.shortcuts import render
import json
from difflib import get_close_matches

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        return json.load(file)

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list) -> str or None:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.8)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str or None:
    for q in knowledge_base['questions']:
        if q['question'] == question:
            return q["answer"]
    return None

def chat_bot_response(user_input: str) -> str:
    knowledge_base = load_knowledge_base('knowledge_base.json')
    if user_input.lower() == 'wrong':
        return "Sorry for misunderstanding. Please write your question again."
    
    best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
    if best_match:
        return get_answer_for_question(best_match, knowledge_base) or "Bot: I don't have an answer to that question yet."
    else:
        return "I don't know the answer. Can you teach me?"

def home(request):
    response = ""
    user_input = ""  
    if request.method == "POST":
        user_input = request.POST.get('text', "")
        if "teach_bot" in request.POST or "teach_bot2" in request.POST:
            correct_question = request.POST.get('correct_question')
            correct_answer = request.POST.get('correct_answer')
            if correct_question and correct_answer:
                knowledge_base = load_knowledge_base('knowledge_base.json')
                knowledge_base['questions'].append({"question": correct_question, "answer": correct_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                response = "Thank you! I learned a new response!" if "teach_bot" in request.POST else "Bot: Thank you! I learned correctly!"
            else:
                response = "Please provide both the correct question and answer."
        elif user_input:
            response = chat_bot_response(user_input)
    
    return render(request, "home.html", {'s': response, 'u': user_input})
