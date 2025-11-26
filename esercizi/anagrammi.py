def anagrams(text: str) -> list[str]:
    if text == "":
        return [""]
    
    res = []
    
    for w in text:
        rest_anagrams = anagrams(text.replace(w, ""))
        for perm in rest_anagrams:            
            res.append(w + perm)
    return res
        
text = "abc"
print(anagrams(text))