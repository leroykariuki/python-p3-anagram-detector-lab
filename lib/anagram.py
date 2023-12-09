class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Convert to lowercase for case-insensitive comparison

    def match(self, anagram_list):
        return [anagram for anagram in anagram_list if self.is_anagram(anagram)]

    def is_anagram(self, candidate):
        # Check if the candidate word is not the same as the initialized word and has the same letters
        return candidate.lower() != self.word and sorted(candidate.lower()) == sorted(self.word)
