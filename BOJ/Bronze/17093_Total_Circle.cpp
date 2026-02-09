#include <iostream>
#include <algorithm>
#define ll long long
using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    ll x[1010] = { 0 }, y[1010] = { 0 }, x2[1010] = { 0 }, y2[1010] = { 0 };
    ll N, M, i, j, mx = 0;

    cin >> N >> M;
    for (i = 1; i <= N; i++)
        cin >> x[i] >> y[i];
    for (i = 1; i <= M; i++)
        cin >> x2[i] >> y2[i];

    for (i = 1; i <= N; i++)
        for (j = 1; j <= M; j++)
            mx = max(mx, (x[i] - x2[j]) * (x[i] - x2[j]) + (y[i] - y2[j]) * (y[i] - y2[j]));
    cout << mx;
}
