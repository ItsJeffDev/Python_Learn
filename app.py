def count_words(sentence):
    # Haluin ang sentence sa mga salita gamit ang .split() method
    words = sentence.split()
    # Count ng bilang ng mga salita
    word_count = len(words)
    return word_count

def main():
    print("Word Counter Program")
    print("Magbigay ng isang sentence o paragraph:")
    # Mag-`input` ng sentence mula sa user
    sentence = input()
    # Tumawag sa function para sa counting ng mga salita
    count = count_words(sentence)
    # Ipakita ang resulta
    print(f"Ang bilang ng mga salita ay: {count}")

if __name__ == "__main__":
    main()