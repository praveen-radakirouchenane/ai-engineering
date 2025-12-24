## Prompting

# Zero-shot-prompting
- Model is given a direct question or task without prior examples. 

### Prompt styles

## Alpaca prompt

    ### Instructions: <SYSTEM_PROMPT>\n

    ### Input: <USER_QUERY>

    ### Response:\n

## ChatML prompt(OpenAI and Gemini use this style):
    {
        "role": "system" | "user" | "assistant",
        "content": string
    }

## INST prompt(LLaMA-2)

    [INST] what is the time now? [/INST]
