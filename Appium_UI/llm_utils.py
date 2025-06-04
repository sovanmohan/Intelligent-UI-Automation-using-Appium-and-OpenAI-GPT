import openai
def get_llm_response(prompt_text, selected_llm, gemini_model):
    if selected_llm == "gemini":
        return gemini_model.generate_content(prompt_text).text.strip()
    elif selected_llm == "openai":
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt_text}]
        )
        return response.choices[0].message.content.strip()
    return ""
