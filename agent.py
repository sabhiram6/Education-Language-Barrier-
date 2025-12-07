# # Import sub-agents
# from google.adk.agents import Agent
#
# from agents.explanation_agent import explanation_agent
# # Import sub-agents
# from agents.speech_agent import speech_agent
# from agents.translation_agent import translation_agent
# from prompts_root import MAIN_AGENT_INSTRUCTION_PROMPT
#
# # ------------------------------------------------------------------
# # MAIN AGENT METADATA
# # ------------------------------------------------------------------
#
# MAIN_DESCRIPTION = (
#     "Main Coordinator Agent for Education Language Bridge. "
#     "This agent intelligently routes inputs between speech recognition, "
#     "translation, and explanation agents to help students learn "
#     "classroom content in their native language."
# )
#
#
# # -----------------------------------------------------------------
# # MAIN AGENT DEFINITION
# # ------------------------------------------------------------------
#
# root_agent = Agent(
#     name="main_agent",
#     model="gemini-2.5-flash",
#     description=MAIN_DESCRIPTION,
#     instruction=MAIN_AGENT_INSTRUCTION_PROMPT,
#     sub_agents=[
#         speech_agent,
#         translation_agent,
#         explanation_agent
#     ]
# )



from datetime import datetime
from google.adk.agents import Agent

from agents.speech_agent import speech_agent
from agents.translation_agent import translation_agent
from agents.explanation_agent import explanation_agent


# ------------------------------------------------------------------
# MEMORY STORE (in-session only)
# ------------------------------------------------------------------

SESSION_MEMORY = {
    "last_teacher_text": None,
    "mode": "lecture"   # or "doubt"
}


# ------------------------------------------------------------------
# MAIN AGENT DESCRIPTION
# ------------------------------------------------------------------

MAIN_DESCRIPTION = (
    "Main Coordinator Agent for Education Language Bridge. "
    "Manages translation, student doubts, and audio input while "
    "maintaining lecture continuity."
)


# ------------------------------------------------------------------
# MAIN AGENT INSTRUCTION
# ------------------------------------------------------------------

MAIN_AGENT_INSTRUCTION_PROMPT = f"""
You are the MAIN AGENT for the system "Education Language Bridge".

You manage class flow for students learning in another language.

-------------------------------------------------------
SUPPORTED INPUT TYPES
-------------------------------------------------------

User input can be:
- TEXT (teacher content or student doubt)
- AUDIO FILE (teacher speaks or student speaks)

-------------------------------------------------------
AGENTS YOU CONTROL
-------------------------------------------------------

1. speech_agent
   - Converts audio into text.

2. translation_agent
   - Translates teacher content to student language.

3. explanation_agent
   - Answers student doubts.

-------------------------------------------------------
CLASSROOM STATE MANAGEMENT RULES
-------------------------------------------------------

Maintain session memory:
- Save teacher lecture text.
- Pause translation if student interrupts.
- Resume lecture after doubt is cleared.

SESSION VARIABLES:
- last_teacher_text → stores latest lecture sentence.
- mode → "lecture" or "doubt"

-------------------------------------------------------
INTERRUPTION RULE (IMPORTANT)
-------------------------------------------------------

If user message == "?" OR starts with "?":
→ Switch to DOUBT MODE.

After answering:
→ Resume LECTURE MODE.

-------------------------------------------------------
ROUTING RULES
-------------------------------------------------------

STEP 1: AUDIO CHECK
If input contains audio:
    Route to speech_agent first.
    Use its transcript as new input text.

STEP 2: MODE CHECK

If input begins with "?":
    mode = "doubt"
    Remove "?" from message
    Send cleaned message to explanation_agent

If not a question:
    mode = "lecture"
    Save message into last_teacher_text
    Send to translation_agent

-------------------------------------------------------
OUTPUT FORMAT (STRICT JSON)
-------------------------------------------------------

{{
  "agent_used": "<agent_name>",
  "output": <agent_response>,
  "session": {{
      "mode": "<lecture/doubt>",
      "last_teacher_text": "<latest>"
  }}
}}

-------------------------------------------------------
STRICT RULES
-------------------------------------------------------

- You MUST call EXACTLY ONE agent per request.
- You MUST update session memory.
- You MUST return JSON only.
- You MUST not generate your own answers.
- Do NOT lose lecture context.

-------------------------------------------------------
Current Date: {datetime.now().strftime("%Y-%m-%d")}
"""


# ------------------------------------------------------------------
# ROOT AGENT DEFINITION
# ------------------------------------------------------------------

root_agent = Agent(
    name="main_agent",
    model="gemini-2.5-flash",
    description=MAIN_DESCRIPTION,
    instruction=MAIN_AGENT_INSTRUCTION_PROMPT,
    sub_agents=[
        speech_agent,
        translation_agent,
        explanation_agent
    ]
)
