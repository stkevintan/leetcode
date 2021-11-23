#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

struct Seg
{
    double l, r, h;
    short v;
    Seg(double x1, double x2, double y, double _v) : l(x1), r(x2), h(y), v(_v) {}
    bool operator<(const Seg &other) const
    {
        return h < other.h;
    }
};

struct Node
{
    Node *lson, *rson;
    int l, r;
    // 染色次数
    int cover;
    // 有效染色长度
    double sum;
    Node(int _l, int _r) : l(_l), r(_r)
    {
        this->cover = 0;
        this->sum = 0;
        this->lson = NULL;
        this->rson = NULL;
    }
};

vector<double> X;
inline int bin(double val)
{
    return lower_bound(X.begin(), X.end(), val) - X.begin();
}

vector<Seg> segments;



void pushUp(Node *rt)
{
    if (rt->cover)
        rt->sum = X[rt->r + 1] - X[rt->l];
    else if (rt->l == rt->r)
        rt->sum = 0;
    else
        rt->sum = rt->lson->sum + rt->rson->sum;
}

Node *build(int l, int r)
{
    auto rt = new Node(l, r);
    if (l == r)
    {
        return rt;
    }
    int m = (l + r) >> 1;
    rt->lson = build(l, m);
    rt->rson = build(m + 1, r);
    pushUp(rt);
    return rt;
}

void update(Node *rt, int L, int R, int val)
{
    if (L <= rt->l && rt->r <= R)
    {
        rt->cover += val;
        pushUp(rt);
        return;
    }
    int m = (rt->l + rt->r) >> 1;
    if (L <= m)
    {
        update(rt->lson, L, R, val);
    }
    if (m < R)
    {
        update(rt->rson, L, R, val);
    }
    pushUp(rt);
}

int main()
{
    int n, cas = 1;
    while (~scanf("%d", &n) && n)
    {
		X.clear();
		segments.clear();
        while (n--)
        {
            double x1, y1, x2, y2;
            scanf("%lf%lf%lf%lf", &x1, &y1, &x2, &y2);
            X.push_back(x1);
            X.push_back(x2);
            segments.push_back(Seg(x1, x2, y1, 1));
            segments.push_back(Seg(x1, x2, y2, -1));
        }
        // 离散化X
        sort(X.begin(), X.end());
        // 去重
        X.erase(unique(X.begin(), X.end()), X.end());

        sort(segments.begin(), segments.end());

        auto rt = build(0, X.size() - 1);
        double ret = 0;
        for (int i = 0; i < (int)segments.size() - 1; i++)
        {
            int L = bin(segments[i].l);
            int R = bin(segments[i].r) - 1;
            update(rt, L, R, segments[i].v);
            ret += rt->sum * (segments[i + 1].h - segments[i].h);
        }
        printf("Test case #%d\nTotal explored area: %.2lf\n\n", cas++, ret);
    }
}

/*
2
10 10 20 20
15 15 25 25.5
0
*/