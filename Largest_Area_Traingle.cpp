// 🚀 Brute Force Strategy
// Since the number of points is small (≤ 50), we can afford to check all combinations of three points and compute the area for each triangle.

// Here’s a clean and efficient Python implementation:

// python
from itertools import combinations

def largestTriangleArea(points):
    def area(p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2

    max_area = 0
    for p1, p2, p3 in combinations(points, 3):
        max_area = max(max_area, area(p1, p2, p3))
    return max_area
✅ Example Usage
python
print(largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))  # Output: 2.0
print(largestTriangleArea([[1,0],[0,0],[0,1]]))              # Output: 0.5
This approach runs in 
𝑂
(
𝑛
3
)
 time, which is perfectly acceptable for 
𝑛
≤
50
// . If you’re up for a challenge, we could explore convex hull optimization—but for this problem, brute force is both elegant and effective.

// Want to try it with a custom set of points or explore a C++ version next?

// make solution in cpp in Solution class with public access modifier and double largestTriangleArea(vector<vector<int>>& points) {int n = points.length();}
// Here's a complete and correct C++ solution wrapped inside a Solution class, using the Shoelace formula to compute triangle areas. I’ve also fixed the incorrect use of .length()—in C++, we use .size() for vectors.

// ✅ C++ Implementation
// cpp
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

class Solution {
public:
    double largestTriangleArea(vector<vector<int>>& points) {
        int n = points.size();
        double maxArea = 0.0;

        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                for (int k = j + 1; k < n; ++k) {
                    maxArea = max(maxArea, triangleArea(points[i], points[j], points[k]));
                }
            }
        }

        return maxArea;
    }

private:
    double triangleArea(vector<int>& A, vector<int>& B, vector<int>& C) {
        return 0.5 * abs(
            A[0] * (B[1] - C[1]) +
            B[0] * (C[1] - A[1]) +
            C[0] * (A[1] - B[1])
        );
    }
};
// 🧪 Example Usage
// cpp
int main() {
    Solution sol;
    vector<vector<int>> points = {{0,0},{0,1},{1,0},{0,2},{2,0}};
    double result = sol.largestTriangleArea(points);
    printf("%.5f\n", result);  // Output: 2.00000
}
// Next Approach
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    double largestTriangleArea(vector<vector<int>>& points) {
        int n = points.size();
        double maxArea = 0;

        for (int i = 0; i < n; i++) {
            int x1 = points[i][0], y1 = points[i][1];
            for (int j = i + 1; j < n; j++) {
                int x2 = points[j][0], y2 = points[j][1];
                for (int k = j + 1; k < n; k++) {
                    int x3 = points[k][0], y3 = points[k][1];

                    double area = 0.5 * abs(
                        x1 * (y2 - y3) +
                        x2 * (y3 - y1) +
                        x3 * (y1 - y2)
                    );

                    if (area > maxArea) {
                        maxArea = area;
                    }
                }
            }
        }

        return maxArea;
    }
};


// ⚡ Optimized C++ Code Using Cross Product
// cpp
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    double largestTriangleArea(vector<vector<int>>& points) {
        int n = points.size();
        double maxArea = 0;

        for (int i = 0; i < n; ++i)
            for (int j = i + 1; j < n; ++j)
                for (int k = j + 1; k < n; ++k) {
                    int x1 = points[i][0], y1 = points[i][1];
                    int x2 = points[j][0], y2 = points[j][1];
                    int x3 = points[k][0], y3 = points[k][1];

                    // Cross product of vectors (x2 - x1, y2 - y1) and (x3 - x1, y3 - y1)
                    double area = 0.5 * abs((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1));
                    if (area > maxArea) maxArea = area;
                }

        return maxArea;
    }
};
// 🧠 Why This Is Optimal
// Still 
// 𝑂
(
𝑛
3
)
// , but with minimal overhead.

// Cross product avoids extra multiplications and is numerically stable.

// No helper functions, no extra memory—just raw geometry.

// If you ever want to push this further, you could explore Convex Hull + Rotating Calipers, but that’s overkill for this problem.
