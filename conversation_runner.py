import subprocess

HISTORY = []

def call_agent(message):
    HISTORY.append(f"USER: {message}")

    full_prompt = "\n".join(HISTORY)

    result = subprocess.run(
        ["adk", "run", "ed_language_barrier_agent", "--input", full_prompt],
        capture_output=True,
        text=True
    )

    response = result.stdout.strip()
    HISTORY.append(f"AGENT: {response}")

    print(response)


print("Type 'exit' to quit.\n")

while True:
    msg = input("You: ")
    if msg.lower() == "exit":
        break

    call_agent(msg)
