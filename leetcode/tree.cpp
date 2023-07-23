#include "CommonHeader.h"

struct Node {
    int value;
    std::vector<Node*> children;
    Node(int v, Node* parent = nullptr)
        : value(v)
    {
        if(parent) {
            parent->children.push_back(this);
        }
    }
};

std::pair<int, int> getMinSumLevel(Node* root)
{
    std::queue<std::pair<Node*, int> > q; // node:level
    q.push({ root, 1 });

    int curlevel = 1;
    int minLevel = 1;
    int minSumSoFar = INT_MAX;
    int curlevelSum = 0;
    while(!q.empty()) {
        Node* n = q.front().first;
        int level = q.front().second;
        q.pop();

        if(curlevel != level) {
            // we completed this level
            if(curlevelSum < minSumSoFar) {
                minSumSoFar = curlevelSum;
                minLevel = curlevel;
            }
            curlevel = level;
            curlevelSum = 0;
        }
        curlevelSum += n->value;
        std::for_each(n->children.begin(), n->children.end(), [&](Node* child) { q.push({ child, curlevel + 1 }); });
    }
    return { minLevel, minSumSoFar };
}

void test_min_level_sum()
{
    Node n01(50);
    Node n11(6, &n01), n12(2, &n01);
    Node n21(30, &n11), n22(80, &n11), n23(7, &n12);

    std::pair<int, int> res = getMinSumLevel(&n01);
    std::cout << "Level is: " << res.first << ", Sum: " << res.second << std::endl;
}