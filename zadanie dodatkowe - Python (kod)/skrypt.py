from openai import OpenAI


client = OpenAI(api_key="TU UMIEŚĆ KLUCZ API")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"""wygeneruj szablon strony w HTMLu o tytule "zadanie rekrutacyjne", do którego będe mógł wstawić artykuł.
            Niech sekcja <body> poza kontenerem na artykuł i miejscem na reklamy po obu stronach artykułu będzie pusta. Strona będzie w języku polskim.
            Załącz bibliotekę Bootstrapa do kodu. Artykuł, który umieszczę
            na stronie, będzie zawierać nagłówki h1 i h2, akapity, zdjęcia oraz ich podpisy.
            Niech szablon będzie również responsywny dla urządzeń mobilnych, wykorzystaj znacznik 
            @media. Na telefonach niech miejsce na artykuł zajmuje cały ekran
                        """,
        }
    ],
    model="gpt-3.5-turbo",
    
)
resposne = chat_completion.choices[0].message.content
with open("szablon.html","w", encoding="utf-8")as file:
    file.write(resposne)