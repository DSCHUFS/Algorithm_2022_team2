#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int L, C;
char alpha[16];
char vowels[5] = {'a', 'e', 'i', 'o', 'u'};
vector<vector<int>> v(16);
void dfs(int now, int cnt, bool flag, string code);

int main(){

    cin >> L >> C; 

    for(int i=0; i<C; i++){
        cin >> alpha[i];
    }

    for(int i=0; i<C-1; i++){
        for(int j=i+1; j<C; j++){
            v[i].push_back(j);
        }
    }
    /*
    0 | 1 2 3 4 5
    1 | 2 3 4 5
    2 | 3 4 5
    3 | 4 5
    4 | 5
    */

    sort(alpha, alpha+C);

    //가장 뒷 순서인 모음의 index구하기
    int last_vowel = -1;
    for(int i=0; i<C; i++){
        char now = alpha[i];
        for(int j=0; j<5; j++){
            if(now == vowels[j]){
                last_vowel = i;
            } 
        }
    }
    //a b c d e f g h i j k l m n o p q r s t u v w x y z 


    for(int i=0; i<=min(last_vowel,C-L); i++){
        string code = "";
        code += alpha[i];
        // cout <<"code: " << code << endl;
        dfs(i, 1, false, code);
    }
    


    return 0;
}

void dfs(int now, int cnt, bool flag, string code){
    if(!flag && code.size() == L){ //모음1개, 자음2개 체크
        int c = 0;
        int v = 0;
        for(int i=0; i<code.size(); i++){
            for(int j=0; j<5; j++){
                if(code[i] == vowels[j]){
                    v++;
                } 
            }
        }
        c = code.size() - v;
        if(v >=1 && c >= 2) flag = true;
    }

    if(cnt == L){
        if(flag) cout << code << endl;
        else return;
    }
    for(int i=0; i<v[now].size(); i++){
        dfs(v[now][i], cnt+1, flag, code+alpha[v[now][i]]);
    }
}