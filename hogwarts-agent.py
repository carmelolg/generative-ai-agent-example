from lib.tool import HogwartsSpellTools
from lib.utils import PromptUtils, OllamaUtils

#user_prompt = "What can I do if I call the spell 'Wingardium Leviosa'?"
#user_prompt = "What spell would I use to make objects levitate?"
user_prompt = "What spell would I use to turn on a light?"

# get available functions
functions = HogwartsSpellTools.available_functions()

stream = OllamaUtils.chat(user_prompt=user_prompt, system_prompt=PromptUtils.get_system_prompt(), tools=functions)
for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
