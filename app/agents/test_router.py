from app.agents.router_agent import classify_question


questions = [
    "How many employees are there?",
    "What is the work from home policy?",
    "Which employee has the highest salary?",
    "How many paid leaves do employees get?",
    "Which department has the highest average salary and what is the leave policy?"
]


for question in questions:

    category = classify_question(question)

    print("\nQuestion:")
    print(question)

    print("Category:")
    print(category)