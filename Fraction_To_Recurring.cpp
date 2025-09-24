#include <string>
#include <unordered_map>
class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";
        string result;
        if ((numerator < 0) ^ (denominator < 0)) result += "-";
        long long num = abs((long long)numerator);
        long long den = abs((long long)denominator);
        result += to_string(num / den);
        long long rem = num % den;
        if (rem == 0) return result;
        result += ".";
        unordered_map<long long, int> remPos;
        while (rem != 0) {            
            if (remPos.count(rem)) {
                result.insert(remPos[rem], "(");
                result += ")";
                break;
            }
            remPos[rem] = result.size();
            rem *= 10;
            result += to_string(rem / den);
            rem %= den;
        }
        return result;
    }
};
