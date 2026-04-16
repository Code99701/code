def count_word_frequency(file_path):
    word_count = {}

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?()[]{}"\'')
                word_count[word] = word_count.get(word, 0) + 1

    return word_count


file_path = r'E:\ml course\code\4-Functions\examples\sample.txt'
frequency = count_word_frequency(file_path)
print(frequency)