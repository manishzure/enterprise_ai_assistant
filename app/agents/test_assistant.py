from app.agents.assistant_agent import ask_assistant


questions = [
    "Which department has the highest average salary and what is the work from home policy?"
]


for question in questions:

    print("\n" + "=" * 70)
    print("QUESTION")
    print("=" * 70)

    print(question)


    result = ask_assistant(question)


    print("\nCATEGORY:")
    print(result["category"])


    print("\nANSWER:")
    print(result["answer"])


    if "sql" in result:

        print("\nSQL:")
        print(result["sql"])