/*Problem Link - https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/?envType=daily-question&envId=2025-09-13 */
#include <unordered_map>
#include <string>
#include <algorithm>
using namespace std;
class Solution {
public:
    int maxFreqSum(string s) {
        unordered_map<char, int> freq;
        string vowel = "aeiou";
        for (char ch : s) {
            freq[ch]++;
        }
        int maxVowel = 0, maxConsonant = 0;
        for (auto& [ch, count] : freq) {
            if (vowel.find(ch) != string::npos) {
                maxVowel = max(maxVowel, count);
            } else {
                maxConsonant = max(maxConsonant, count);
            }
        } return maxVowel + maxConsonant;
    }
};
