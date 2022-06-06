#include <iostream>
#include <cstring>
#include <algorithm>
#include <queue>

using namespace std;

int N, M, res = 987654321;
int sX, sY, sD; // start X,Y,Dir
int eX, eY, eD; // end X,Y,Dir
int dx[4] = { 1, 0, -1, 0 }; // 남, 서, 북, 동
int dy[4] = { 0, -1, 0, 1 };
int factory[110][110]; //공장map
int visit[110][110][5]; //(x,y)에 dir 방향으로 방문기록

struct robot {
	int x;
	int y;
	int dir;
};

void bfs()
{
	visit[sX][sY][sD] = 0;
	queue<robot> q;
	q.push({ sX,sY,sD });
	while (!q.empty()) {
		int x = q.front().x;
		int y = q.front().y;
		int dir = q.front().dir;
		q.pop();

		if (x == eX && y == eY && dir == eD) { //종료조건
			res = min(res, visit[x][y][dir]);
			continue;
		}

		int nD = (dir + 1) % 4; // Turn Right
		if (visit[x][y][nD] == -1) { //아직 방문되지 않았을 때
			q.push({ x,y,nD });
			visit[x][y][nD] = visit[x][y][dir] + 1;
		}

		nD = (dir + 3) % 4; // Turn Left
		if (visit[x][y][nD] == -1) {
			q.push({ x,y,nD });
			visit[x][y][nD] = visit[x][y][dir] + 1;
		}

		//Go 1, 2, 3
		for (int i = 1; i <= 3; i++) { //최대 3칸까지 이동가능
			int nx = x + i * dx[dir]; //dir은 현재 방향
			int ny = y + i * dy[dir];

			if (nx<1 || ny<1 || nx>N || ny>M) continue;
			if(factory[nx][ny]==1) break; //벽인 경우는 더이상 진행 불가능.

			if (visit[nx][ny][dir] == -1 || visit[nx][ny][dir] > visit[x][y][dir] + 1) { //다른경로로 해당 위치에 도착했을 때보다 더 짧은 case일 때
				q.push({ nx,ny,dir });
				visit[nx][ny][dir] = visit[x][y][dir] + 1;
			}
		}
	}
}

int main()
{
	cin >> N >> M;
	for (int i = 1; i <= N; i++) 
		for (int j = 1; j <= M; j++) 
			cin >> factory[i][j];
	cin >> sX >> sY >> sD >> eX >> eY >> eD;

	// 시작,끝점 동서남북 조정 --> 0 1 2 3 == 남 서 북 동 (남쪽 기준으로 시계방향 회전)
	if (sD == 1) sD = 3;
	else if (sD == 2) sD = 1;
	else if (sD == 3) sD = 0;
	else sD = 2;

	if (eD == 1) eD = 3;
	else if (eD == 2) eD = 1;
	else if (eD == 3) eD = 0;
	else eD = 2;
	

	memset(visit, -1, sizeof(visit)); //-1로 초기값 설정

	bfs();

	cout << res;
}