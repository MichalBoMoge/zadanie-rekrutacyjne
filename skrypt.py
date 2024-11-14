from openai import OpenAI
with open("tresc.txt","r", encoding="utf-8") as file:
    cont = file.read()
client = OpenAI(api_key="TU NALEŻY WSTAWIĆ SWÓJ KLUCZ API")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"""przesyłam ci treść artykułu do obróbki w języku HTML. 
            Użyj odpowiednich tagów do strukturyzacji treści. Określ, w których miejscach warto 
            wstawić grafiki. oznacz je z użyciem tagu <img> z atrybutem src="image_placeholder.jpg". 
            Dodaj atrybut alt do każdego obrazka,którego treść będzie dokładnym promptem ,którego można użyć do wygenerowania grafiki.
            Umieść podpisy pod grafikami używając odpowiedniego tagu HTML.
            Nie dołączaj Kodu CSS, Javascript ani znaczników <html>,<head> ani <body>.
            zwróć uwagę, że jeśli zdanie zaczyna się od nowej linii i nie jest do końca powiązane z 
            poprzednim akapitem, jest to najprawdopodobniej podtytuł.
            oto artykuł: \n
            {cont}
                        """,
        }
    ],
    model="gpt-3.5-turbo",
    
)
resposne = chat_completion.choices[0].message.content
with open("artykul.html","w")as file:
    file.write(resposne)