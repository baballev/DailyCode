# Implement an URL shortener
# We could also have used a random function and check if the random generated string already exists



sigma = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
static_count = 0
static_hashmap= {}
reverse_hashmap = {}
def shorten(url):
    if url in static_hashmap: return static_hashmap[url]
    else:
        n = len(sigma)
        shorten = ""
        count = static_count
        while len(shorten) < 6:
            r, count = count % n, count // n
            shorten += sigma[r]
        static_count += 1
        static_hashmap[url] = shorten
        reverse_hasmap[shorten] = url
        return shorten

def restore(short):
    if short in reverse_hashmap:
        return reverse_hashmap[short]
    else:
        return None
    
