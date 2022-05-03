//C++ 사용
//BOJ 1461

#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;

int N, M;
int nt, pt;
int books[51];
int result;

int main(){
    cin >> N >> M;
    for(int i=0; i<N; i++){
        cin >> books[i];
        if(books[i] < 0) nt++;
    }

    sort(books, books+N);       //오름차순으로 정렬

	for(int i=0; i<nt; i+=M){
		result += abs(books[i]) * 2;
	}
	for(int i=N-1; i>=nt; i-=M){
		result += abs(books[i]) * 2;
	}

	result -= max(abs(books[0]), abs(books[N-1]));
    cout << result << endl;

    return 0;
}
