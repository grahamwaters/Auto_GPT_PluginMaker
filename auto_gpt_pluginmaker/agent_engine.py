import os
import openai
import json

# Set your OpenAI API key based on the OPENAI_API_KEY environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

class AutoGPT:
    def __init__(self, findings_dir='findings'):
        self.findings_dir = findings_dir
        os.makedirs(findings_dir, exist_ok=True)

    def learn(self, task):
        # Check if we already learned this task
        findings_file = os.path.join(self.findings_dir, f'{task}.json')
        if os.path.exists(findings_file):
            with open(findings_file, 'r') as f:
                return json.load(f)

        # If not, learn it
        prompt = f"Create a plugin for GPT-4 that {task}"
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=500)

        # Save the findings
        with open(findings_file, 'w') as f:
            json.dump(response.choices[0].text.strip(), f)

        return response.choices[0].text.strip()

    def execute(self, task):
        plugin_code = self.learn(task)
        exec(plugin_code)

# Usage
agent = AutoGPT()
agent.execute('can translate English text to French')
