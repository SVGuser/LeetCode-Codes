 https://leetcode.com/problems/vowels-game-in-a-string/?envType=daily-question&envId=2025-09-12 
class Solution {
public:
    bool doesAliceWin(string s) {
        string vowels = "aeiou";
        int vowel_count = 0;

        for (char c : s) {
            if (vowels.find(c) != string::npos) {
                vowel_count++;
            }
        }

        return vowel_count > 0;
    }
};
