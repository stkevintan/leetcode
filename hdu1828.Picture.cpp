#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;
// 从下往上扫
struct Seg
{
	int l, r, h;
	int flag; // 1 下边， -1 上边
	Seg(int x1, int x2, int y, int f) : l(x1), r(x2), h(y), flag(f) {}
	bool operator<(const Seg &other) const
	{
		// 把高度相同的边中的下边排在上边之前
		return h == other.h ? flag > other.flag : h < other.h;
	}
};

vector<Seg> S;
vector<int> X;
inline int bin(int val)
{
	return lower_bound(X.begin(), X.end(), val) - X.begin();
}

struct Node
{
	int cover;
	// 有效(无覆盖）端点的数量
	int endpoints;
	int len;
	// 当前区间左右两端点是否被cover
	bool lcover, rcover;
	int l, r;
	Node *lson, *rson;
	Node(int l, int r)
	{
		this->l = l;
		this->r = r;
		this->cover = 0;
		this->lson = nullptr;
		this->rson = nullptr;
		this->endpoints = 0;
		this->len = 0;
		this->lcover = false;
		this->rcover = false;
	}
};

Node *build(int l, int r)
{
	auto node = new Node(l, r);
	if (l == r)
	{
		return node;
	}
	int m = (l + r) >> 1;
	node->lson = build(l, m);
	node->rson = build(m + 1, r);
	return node;
}

void pushUp(Node *rt)
{
	if (rt->cover)
	{
		rt->lcover = rt->rcover = true;
		rt->len = X[rt->r + 1] - X[rt->l];
		rt->endpoints = 2;
	}
	// 叶子节点，此处代表的是[l, l+1]
	else if (rt->l == rt->r)
	{
		rt->len = rt->endpoints =  0;
		rt->lcover = rt->rcover = false;
	}
	else
	{
		rt->lcover = rt->lson->lcover;
		rt->rcover = rt->rson->rcover;
		rt->len = rt->lson->len + rt->rson->len;
		rt->endpoints = rt->lson->endpoints + rt->rson->endpoints;
		// 两个端点是重合的比如： l = 1,r = 2 代表[1,3], l = 3, r = 4 代表[3,5]
		if (rt->lson->rcover && rt->rson->lcover)
		{
			rt->endpoints -= 2;
		}
	}
}

void update(Node *rt, int L, int R, int flag)
{
	if (L <= rt->l && rt->r <= R)
	{
		rt->cover += flag;
		pushUp(rt);
		return;
	}
	int m = (rt->l + rt->r) >> 1;
	if (L <= m)
	{
		update(rt->lson, L, R, flag);
	}
	if (m < R)
	{
		update(rt->rson, L, R, flag);
	}
	pushUp(rt);
}

int main()
{
	int n;
	while (~scanf("%d", &n))
	{
		X.clear();
		S.clear();
		for (int i = 0; i < n; i++)
		{
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			X.push_back(x1);
			X.push_back(x2);
			S.push_back(Seg(x1, x2, y1, 1));
			S.push_back(Seg(x1, x2, y2, -1));
		}

		sort(S.begin(), S.end());
		sort(X.begin(), X.end());
		X.erase(unique(X.begin(), X.end()), X.end());
		auto rt = build(0, X.size() - 1);
		int ret = 0, last = 0;
		for (int i = 0; i < (int)S.size(); i++)
		{
			int L = bin(S[i].l);
			int R = bin(S[i].r) - 1;
			if(L <= R) update(rt, L, R, S[i].flag);
			if (i < S.size() - 1)
			{
				ret += rt->endpoints * (S[i + 1].h - S[i].h);
			}
			ret += abs(rt->len - last);
			last = rt->len;
		}
		printf("%d\n", ret);
	}
}

/*
7
-15 0 5 10
-5 8 20 25
15 -4 24 14
0 -6 16 4
2 15 10 22
30 10 36 20
34 0 40 16
*/