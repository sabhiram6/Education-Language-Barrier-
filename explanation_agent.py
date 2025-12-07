from google.adk.agents import Agent
# from prompts import EXPLANATION_AGENT_INSTRUCTION_PROMPT

EXPLANATION_AGENT_INSTRUCTION_PROMPT = """
You are the EXPLANATION AGENT (Doubt Solver).

ROLE:
Explain concepts to students in their native language.

INPUT:
- Student question
- Language
- Grade

OUTPUT FORMAT (JSON ONLY):
{
  "answer": "<direct explanation>",
  "simple_example": "<daily-life example>"
}

RULES:
- Respond only in target language.
- Keep explanation simple.
- Use age-appropriate language.
- Always give a real-life example.
- Do NOT include English unless asked.
- Output JSON only.
"""

# ------------------------------------------------------------------
# EXPLANATION AGENT METADATA
# ------------------------------------------------------------------

EXPLANATION_DESCRIPTION = (
    "Explanation Agent. "
    "This agent answers student questions in their native language "
    "using clear, simple explanations and everyday examples."
)



# -----------------------------------------------------------------
# EXPLANATION AGENT INITIALIZATION
# ------------------------------------------------------------------

explanation_agent = Agent(
    name="explanation_agent",
    model="gemini-2.5-flash",
    description=EXPLANATION_DESCRIPTION,
    instruction=EXPLANATION_AGENT_INSTRUCTION_PROMPT
)
