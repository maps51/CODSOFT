'''
TASK 1: Build a simple chatbot that responds to user inputs based on
predefined rules. Use if-else statements or pattern matching
techniques to identify user queries and provide appropriate
responses. This will give you a basic understanding of natural
language processing and conversation flow.

'''

#Chatbot with information on London. User asks the chatbot about London. 

import random
import datetime

# User greetings according to time
def greet_user():
    greetings = ["Hi there!",
                 "Good morning!",
                 "Good afternoon!",
                 "Good evening!"]
    current_hour = int(datetime.datetime.now().hour)
    if 5 <= current_hour < 12:
        greeting = greetings[1]
    elif 12 <= current_hour < 17:
        greeting = greetings[2]
    else:
        greeting = greetings[3]
    return greeting

#User input
def get_user_input():
    return input("You: ")

#Response handling
def london(user_input):
    responses = {
        "attractions": ["London has many iconic attractions, including Buckingham Palace, the Tower of London, and the London Eye. \n For art lovers, the British Museum and the National Gallery are must-visits."],
        
        "history": ["London has a rich history dating back to Roman times. You can explore its past at sites like the Tower of London and Westminster Abbey."],
        
        "transportation": ["London has an extensive public transportation system, including the Tube (underground), buses, and taxis."],
        
        "food": ["London is a foodie paradise with cuisine from all over the world. Be sure to try traditional British dishes like fish and chips or a Sunday roast."],
        
        "culture": ["London is a vibrant and multicultural city with a thriving arts scene. Catch a West End show or explore the many museums and galleries."],
        
        "places": ["What kind of other places?"],
        
        "shopping": ["Think Bond Street with its luxury brands like Chanel and Burberry, or Sloane Street with its exclusive boutiques.\nOxford Street offers flagship stores like Primark and Selfridges, while Regent Street has iconic names like Liberty and Hamleys.\nPortobello Road Market is a treasure trove for antiques and collectibles, while Camden Market buzzes with alternative fashion and street food."],
        
        "restaurants":["Recommended famous restaurants:\nThe Fat Duck: Nestled in Bray, just outside of London, this three-Michelin-starred wonderland by Heston Blumenthal is a gastronomic adventure.\nAlain Ducasse at the Dorchester: Experience French culinary finesse at its finest in this opulent setting within the Dorchester Hotel.\nNoma: This Copenhagen import brought its innovative Nordic cuisine and minimalist elegance to London in 2022, and it hasn't disappointed. Chef René Redzepi's hyper-seasonal tasting menus are like artistic expressions on a plate, with unexpected flavor combinations and textures that challenge and delight."],
        
        "hotels": ["For Classic Elegance: The Savoy (luxurious Thames riverside setting), The Ritz (ornate grandeur and afternoon tea tradition), Claridge's (art deco splendor and royal connections).\nFor Modern Chic: The Shangri-La The Shard (breathtaking city views and sky-high infinity pool), Sea Containers London (converted shipping containers with maritime flair), The London EDITION (cool design and buzzy Soho location)."],
        
        "instagram hotspots": ["Some recommended spots are:\nSky Garden: Breathtaking panoramic views from the highest public garden in London.\nLeadenhall Market: Harry Potter's Diagon Alley setting, a charming historic market.\nShoreditch Street Art: Eclectic murals and graffiti covering buildings, perfect for urban vibes.\nLittle Venice: Picturesque canals lined with colorful houseboats, a serene escape. \n Primrose Hill: Panoramic views of Regent's Park and the cityscape, ideal for sunset pictures.\nHamley's Toy Store: Playful window displays and giant teddy bears, a whimsical wonderland. "],
        
        "museums": ["From ancient Egyptian mummies to Viking treasures, British museums brim with history. Dive into two million years at the British Museum, art across centuries at the National Gallery, or explore naval might at the Imperial War Museum. "],
        
        "art galleries": ["Tate Modern: Turbine Hall's ever-changing installations dazzle, while modern masters like Picasso and Rothko captivate in permanent collections.\nNational Gallery: Immerse yourself in Western art's greatest hits, from Van Gogh's Sunflowers to Turner's fiery seascapes."],
        
        "monuments":["Tower of London: Jewel-filled fortress, chilling tales of torture and ghosts, Beefeater guards in red.\n Westminster Abbey: Royal coronations and weddings, Gothic masterpiece soaring in the sky, tombs of kings and queens.\nBuckingham Palace: Changing of the Guard spectacle, peek into Queen's grand home, imagine royal lives within.\nBig Ben: Timekeeper of the nation, iconic silhouette against the Thames, echoing chimes through London's soul."],

        "hi": ["Hello, what do you want to know about london?"],

        "hello": ["Hello, what do you want to know about london?"]
    }

    keywords = ["attractions", "history", "transportation", "food", "culture", "places", "historical gems", "natural wonders", "outdoor adventures", "artistic", "shopping", "instagram hotspots", "hi", "hello", "restaurants", "hotels" , "museums", "art galleries",  "monuments"]
    for keyword in keywords:
        if keyword in user_input.lower():
            return random.choice(responses[keyword])
        if "places" in user_input.lower() and "historical gems" in user_input.lower():
            return "For historical gems recommended places would be, the Bath's Roman baths, York's Viking history, Canterbury's ancient cathedral, Hadrian's Wall's Roman frontier."
        if "places" in user_input.lower() and "natural wonders" in user_input.lower():
            return "For natural wonders recommended places would be, Lake District's rugged mountains and serene lakes, Jurassic Coast's dramatic cliffs and fossils, Peak District's limestone valleys and caves."
        if "places" in user_input.lower() and "outdoor adventures" in user_input.lower():
            return "For outdoor adventures recommended places would be, Surfing in Cornwall, hiking in Snowdonia National Park, cycling the South Downs Way, exploring Northumberland's wild coastline."
        if "places" in user_input.lower() and "artistic" in user_input.lower():
            return "For artistic recommended places would be Bristol's street art and music scene, Brighton's bohemian vibe and beachfront fun, Oxford and Cambridge's prestigious universities and architectural splendor."
        
    return "I'm not sure I understand. Can you rephrase your statement?"

#Start and End of Chat 
def main():
    print(greet_user())
    while True:
        user_input = get_user_input()
        if "bye" in user_input.lower() or "quit" in user_input.lower():
            break
        print(london(user_input))

if __name__ == "__main__":
    main()
