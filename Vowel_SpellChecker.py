from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word: str) -> str:
            vowels = set('aeiou')
            return ''.join('*' if c in vowels else c for c in word.lower())

        exact_words = set(wordlist)
        case_insensitive = {}
        vowel_mask = {}

        for word in wordlist:
            lower = word.lower()
            masked = devowel(word)

            if lower not in case_insensitive:
                case_insensitive[lower] = word
            if masked not in vowel_mask:
                vowel_mask[masked] = word

        result = []
        for query in queries:
            if query in exact_words:
                result.append(query)
            elif query.lower() in case_insensitive:
                result.append(case_insensitive[query.lower()])
            elif devowel(query) in vowel_mask:
                result.append(vowel_mask[devowel(query)])
            else:
                result.append("")
        return result
