def translate_text(text, target_lang="en"):
    import requests

    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl={target_lang}&dt=t&q={text}"
    response = requests.get(url)
    return response.json()[0][0][0]
