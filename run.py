# coding=utf-8

import json
import random

from tqdm import tqdm

from ChatGPT import ChatGPT

seed= random.randint(3, 5)
chatgpt = ChatGPT(headless=True, user_data_dir_seed=seed)

# install_mode = False
# chatgpt = ChatGPT(headless=not install_mode)
#
# query = '''
#     I need you to read a paragraph and tell me what you can learn from the paragraph about a given entity. The paragraph is indicated by []. The given entity is indicated by [unused0] and [unused1]. Let's begin. [the northern attack group for operation torch, the invasion of north africa. the objective assigned to this group was port lyautey in french morocco. the warships arrived off the assault beaches near the village of mehedia early in the morning of 8 november and began preparations for the [unused0] invasion [unused1]. " texas " transmitted lt. general dwight d. eisenhower's first " voice of freedom " broadcast, asking the french not to oppose allied landings on north africa. when the troops went ashore, " texas " did not go into action immediately to support them. at that point in the war, the doctrine]. Now please tell me which few sentences in this paragraph help me deduce the identity of the invasion indicted by [unused0] invasion [unused1]?
#     '''
# response = chatgpt.ask(query)
# print(response)

data = json.load(open('safety_chatgpt.json'))
solved_tasks = []

with open('safety_chatgpt_response.jsonl') as f:
    for line in f:
        items = json.loads(line.strip())
        if items["response"] != -1:
            solved_tasks.append(items["id"])

with open('safety_chatgpt_response.jsonl', 'a', encoding='utf8') as fw:
    for idx, item in tqdm(enumerate(data)):
        if idx in solved_tasks:
            continue
        response = chatgpt.ask(item)
        if response == -1:
            break
        d = {
            "id": idx,
            "utterance": item,
            "response": response
        }
        fw.write(json.dumps(d, ensure_ascii=False))
        fw.write("\n")
        fw.flush()
        break
