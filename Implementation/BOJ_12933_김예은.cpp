#include <iostream>

using namespace std;

int sound[2501];
int main(){
	string s;
	cin >> s;

	int res=0;
	int s_l = s.size();
	int flag = s.size();
	char duck[5] = {'q','u','a','c','k'};

	while(flag > 4){
		if(s[0] != 'q' || s_l%5 != 0) break;

		int now = 0; // q u a c k 인덱스
		for(int i=0; i<s_l; i++){
			if(sound[i] == 1) continue;
			if(s[i]==duck[now]){
				now = (now+1)%5;
				sound[i] = 1;
				flag--;
			}
		}
		
		if(flag > 0){ //q로 시작안하는 경우 바로 종료 -> 이부분 없으면 시간초과남
			for(int i=0; i<s_l; i++){
				if(sound[i] == 1) continue;
				else{
					if(s[i]!=duck[0]){
						flag = -1;
						break;
					}else break;
				}
			}
		}
		res++;
	}

	if(flag != 0) res = -1;
	cout << res;

	return 0;
}


