#include <iostream>
//백준 1268번 임시반장정하기
using namespace std;

int N; 
int students[1001][1001];
int result[1001];

int main(){

    cin >> N;
    for(int i=0; i<N; i++){
        for(int j=0; j<5; j++){
            cin >> students[i][j];
        }
    }

    for(int i=0; i<N; i++){ //다음 학생
        int checkSame[N] = { };
        for(int j=0; j<5; j++){ //다음 학년
            for(int k=0; k<N; k++){ //비교
                if(i==k) continue;
                if(students[i][j]==students[k][j]){
                    checkSame[k] = 1; //같은반 체크
                }
            }
        }
        for(int x=0; x<N; x++){
            if(checkSame[x]==1){ //같은반이었던 적이 있는 친구 체크
                result[i]++;
            }
        }
    }

    int max = -1;
    int maxIndex = -1;
    for(int i=0; i<N; i++){
        if(max < result[i]){
            max = result[i];
            maxIndex = i+1;
        }
    }

    cout<<maxIndex;

    return 0;
}