from google.adk.agents import Agent
# from prompts import TRANSLATION_AGENT_INSTRUCTION_PROMPT

TRANSLATION_AGENT_INSTRUCTION_PROMPT = """
You are the TRANSLATION AGENT.

ROLE:
Translate teacher content into student's native language and simplify it.

INPUT:
- Teacher lecture content
- Target language
- Grade level

OUTPUT FORMAT (JSON ONLY):
{
  "subtitle": "<short translation>",
  "explanation": "<simple explanation>"
}

RULES:
- Always translate into provided language.
- Keep subtitles short.
- Explanation must be simple and accurate.
- Do not add new information.
- No English unless explicitly requested.
- Output JSON only.
"""

# ------------------------------------------------------------------
# TRANSLATION AGENT METADATA
# ------------------------------------------------------------------

TRANSLATION_DESCRIPTION = (
    "Translation Agent. "
    "This agent converts teacher content into the student’s native language "
    "and produces a simplified explanation."
)

# ------------------------------------------------------------------
# TRANSLATION AGENT INITIALIZATION
# ------------------------------------------------------------------

translation_agent = Agent(
    name="translation_agent",
    model="gemini-2.5-flash",
    description=TRANSLATION_DESCRIPTION,
    instruction=TRANSLATION_AGENT_INSTRUCTION_PROMPT
)
