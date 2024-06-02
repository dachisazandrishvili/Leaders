def generate_hashtag(s):
    s = s.title()
    s = s.replace(" ","")
    if len(s) < 140 and len(s):
        return "#" + s
    else:
        return False
    