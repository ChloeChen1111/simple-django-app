# from django.shortcuts import render, get_object_or_404
# from .models import Counter

# def index(request):
#     if len(Counter.objects.filter(key='counter')) == 0:
#         counter = Counter(key='counter', value=0)
#         counter.save()
#     else:
#         counter = get_object_or_404(Counter, key='counter')
    
#     counter.value+=1
#     counter.save()
#     context = {'value': counter.value}
#     # TODO add backend logic
#     return render(request, 'counter/index.html', context)



import re

def place_element_symbol(element, symbol, user_input):
    return user_input.replace(element, symbol)

def parse_speech(speech, notation, header, body, bullet, image):
    regex_pattern = f"({re.escape(header)}|{re.escape(body)}|{re.escape(bullet)}|{re.escape(image)})"
    matches = re.finditer(regex_pattern, speech)

    last_index = 0
    last_symbol_value = 0

    for match in matches:
        segment = speech[last_index:match.start()].strip()
        if segment:
            notation[segment] = last_symbol_value

        if match.group() == header:
            last_symbol_value = 1
        elif match.group() == body:
            last_symbol_value = 2
        elif match.group() == bullet:
            last_symbol_value = 3
        elif match.group() == image:
            last_symbol_value = 4
        last_index = match.end()

    # Handle the last segment after the final symbol
    if last_index < len(speech):
        segment = speech[last_index:].strip()
        if segment:
            notation[segment] = last_symbol_value

def main():
    header = "<H>"
    body = "<B>"
    bullet = "<Bul>"
    image = "<I>"

    notation = {}

    speech = """
        Header. Hackathon Notes. Body. Create a text to speech web app. Bullet. 
        Write a sample paragraph. Bullet. Create functions to parse string. Bullet. 
        Test application. Image. Display a picture of a dog.
        """

    speech = place_element_symbol("Header.", header, speech)
    speech = place_element_symbol("Body.", body, speech)
    speech = place_element_symbol("Bullet.", bullet, speech)
    speech = place_element_symbol("Image.", image, speech)

    parse_speech(speech, notation, header, body, bullet, image)

    for k, v in notation.items():
        print(f"Key: {k}, Value: {v}")

if __name__ == "__main__":
    main()


