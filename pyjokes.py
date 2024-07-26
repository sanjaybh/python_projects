import pyjokes

list_of_jokes = pyjokes.get_joke(language="en", category="neutral") 

for i in range(0, 4): 
    print(list_of_jokes[i], sep='\n') 
    
    
# print(joke)