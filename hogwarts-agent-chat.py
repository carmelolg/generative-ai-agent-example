from lib.tool import HogwartsSpellTools
from lib.utils import PromptUtils, OllamaUtils

# get available functions
functions = HogwartsSpellTools.available_functions()

# Start chat
while True:
    user_prompt = input('\nUser > ')
    if user_prompt.lower() in ['exit', 'quit']:
        break
    else:
        print('Assistant >', end=' ')
        stream = OllamaUtils.chat_with_tools(user_prompt=user_prompt,
                                             system_prompt=PromptUtils.get_system_prompt(),
                                             #assistant_prompt=PromptUtils.get_assistant_prompt(),
                                             tools=functions)
        # print the response from the chatbot in real-time
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
