from google.adk.agents import Agent
# from prompts import SPEECH_AGENT_INSTRUCTION_PROMPT

SPEECH_AGENT_INSTRUCTION_PROMPT = """
You are the SPEECH AGENT in a multilingual education system.

ROLE:
Convert audio input (teacher or student voice) into clean readable text.

INPUT:
- Audio from classroom (teacher lecture or student question)

OUTPUT FORMAT (JSON ONLY):
{
  "transcript": "<recognized speech>"
}

RULES:
- Transcribe accurately.
- Remove filler words (um, ah, noise).
- Keep original structure.
- Do not translate.
- Do not explain.
- Do not guess missing parts.
- Output JSON only.
"""



SPEECH_DESCRIPTION = (
    "Speech Recognition Agent. "
    "This agent converts spoken classroom audio into accurate text "
    "for downstream translation or explanation."
)


# ------------------------------------------------------------------
# SPEECH AGENT INITIALIZATION
# ------------------------------------------------------------------

speech_agent = Agent(
    name="speech_agent",
    model="gemini-2.5-flash",
    description=SPEECH_DESCRIPTION,
    instruction=SPEECH_AGENT_INSTRUCTION_PROMPT
)
