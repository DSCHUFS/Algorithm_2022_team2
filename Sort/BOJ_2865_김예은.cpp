#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int N, M, K;
float info[101][101];
float res[101];

int main(){

    cin >> N >> M >> K;

    for(int i=0; i<M; i++){
        for(int j=0; j<N; j++){
            int number;
            cin >> number;
            cin >> info[number][i];
        }
    }

    for(int i=1; i<=N; i++){
        float max = -0.5;
        for(int j=0; j<M; j++){
            if(max < info[i][j]){
                max = info[i][j];
            }
        }
        res[i] = max;
    }
    sort(res+1, res + N + 1, greater<float>());
    // for(int i=1; i<=N; i++){
    //     cout << res[i] << "   ";
    // }
    // cout << endl;

    float sum=0;
    for(int i=1; i<=K; i++){
        sum += res[i];
    }

    // sum = round(sum*10) / 10;
    // cout << "sum: " << sum << endl;
    printf("%.1f", sum);

    return 0;
}