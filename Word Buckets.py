

def split_into_buckets(phrase, n):
    words = phrase.split()
    buckets = []
    current = ""

    for word in words:
        if len(current) + len(word) + (1 if current else 0) <= n:
            current += (" " if current else "") + word
        else:
            buckets.append(current)
            current = word

    if current:
        buckets.append(current)

    return buckets
