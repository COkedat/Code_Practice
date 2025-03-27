"""문제
 
$N$명의 학생들이 단체줄넘기를 하려고 한다. 단체줄넘기를 하기 위해서는 한 줄로 나란히 서야 하고, 학생들은 각자 줄을 잡은 양쪽 방향 중 한 곳을 바라보고 서야 한다.

학생들은 각자 바라보는 방향에 자신보다 키가 크거나 같은 사람이 있다면 점프할 타이밍을 놓쳐 줄에 걸릴 수 있다. 학생들은 최대한 많이 단체줄넘기를 뛰고 싶어 하기 때문에, 줄에 걸릴 수 있는 상황을 만들지 않으려고 한다. 즉 자신이 바라보는 방향에 자신보다 키가 작은 학생들만 앞에 오도록 줄을 서려고 한다.

학생들의 키를 알고 있을 때, 이 중 최대 몇 명의 학생이 단체줄넘기에 참여할 수 있을까? 줄을 돌리는 사람은 주어진 학생에 포함되지 않는다.

입력
첫째 줄에 학생의 수 
$N$이 주어진다. 
$\left( 1\leq N\leq 1\, 000 \right)$ 

둘째 줄에 학생들의 키를 나타내는 정수 
$A_i$가 공백으로 구분되어 주어진다. 
$\left( 1\leq A_i\leq 1\, 000 \right)$ 

출력
줄에 걸릴 수 있는 상황을 만들지 않도록 학생들을 적절히 배치했을 때, 단체줄넘기에 참여할 수 있는 최대 학생 수를 출력한다."""

N = int(input())
students = list(map(int,input().split(" ")))
students.sort()
checked = []
dupes = []
for i in students:
    if i in checked:
        dupes.append(i)
    else:
        checked.append(i)
answer = len(set(dupes))+len(set(students))
print(answer)

