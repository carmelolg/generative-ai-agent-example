from ollama import chat
from lib import SpellFunctions


messages = [{"role": "user", "content": "What can I do if I call the spell 'Oblivate'?"}]

# pass functions directly as tools in the tools list or as a JSON schema
response = chat(model="qwen3", messages=messages, tools=[SpellFunctions.get_spell_use, SpellFunctions.get_spell_name], think=True)

messages.append(response.message)
if response.message.tool_calls:
  # process each tool call
  for call in response.message.tool_calls:
    # execute the appropriate tool
    if call.function.name == 'get_spell_use':
      result = SpellFunctions.get_spell_use(**call.function.arguments)
    elif call.function.name == 'get_spell_name':
      result = SpellFunctions.get_spell_name(**call.function.arguments)
    else:
      result = 'Unknown tool'
    # add the tool result to the messages
    messages.append({'role': 'tool',  'tool_name': call.function.name, 'content': str(result)})

  # generate the final response
  final_response = chat(model='qwen3', messages=messages, tools=[SpellFunctions.get_spell_use, SpellFunctions.get_spell_name], think=True)
  print(final_response.message.content)