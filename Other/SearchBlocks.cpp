//Решение задачи поиска блоков в графе, заданного матрицей смежности
//для курса "Графы и алгоритмы", читаемого на 3 курсе ММФ НГУ
//Литература: В.Е. Алексеев, В.А. Таланов “Графы. Модели Вычислений. Структуры данных”

#include <iostream>
#include <cmath>
using namespace std;

void SmezhSx(int n, int x, int** matrix, int** V){
    for (int j=0;j<n;j++)
    {
        if (matrix[x][j] == 1) V[x][j]=j;
    }
}
void Sort(int size, int arr[])
{
    int temp;
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
void NewBlock(int n, int& k, int& c, int& g, int x, int y, int* S, int** V){
    k+=1;
    int i=0;
    cout << "New Block No.: " << k << " It includes: ";
    int B[n], check =g-1,check1=0;
    B[0]=x;
    for (int i=1;i<g;i++){
        B[i]=S[check];
        S[check]=-1;
        check--;
        check1++;
        if (B[i]==y) {break;}
    }
    g=check+1;
    Sort(check1+1, B);
    for (int i=0;i<=check1;i++){
        cout << B[i] << " "; }
    cout << "\n";
}

int minimum (int x, int y)
{
    if (x<y) return x; else return y;
}

void Blocks (int n, int& k, int& c, int& g, int x, int* Dnum, int* Low, int* S, int** matrix, int **V){
    c+=1;
    Dnum[x]=c;
    Low[x]=c;
    S[g]=x;
    g++;
    SmezhSx(n, x, matrix, V);
    for (int y=0;y<n;y++){
        if (y!=x){
            if ( (V[x][y]!=-1) && (Dnum[y]==0)) {
                Blocks(n, k , c, g, y, Dnum, Low, S, matrix, V);
                Low[x]=minimum(Low[x], Low[y]);
                if (Low[y] == Dnum[x]) {NewBlock(n, k, c, g, x, y, S, V);}
            } else if (V[x][y]!=-1) {Low[x]=minimum(Low[x], Dnum[y]);}
        }
    }
}

int main()
{
    int n;
    cin >> n;
    int** matrix = new int* [n];
    int** V = new int* [n];
    int* Dnum = new int[n];
    int* Low = new int[n];
    int* S = new int[n];
    int k=0, c=0, g=0;

    for (int i = 0; i < n; i++) {
        matrix[i] = new int[n];
        V[i] = new int[n];
    } //создаем двумерные массивы ч/з указатели


    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            cin >> matrix[i][j] ;
        }
    } //заполняем матрицу А

    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            V[i][j]=-1 ;
        }
    } //Заполняем матрицу смежности -1 для дальнейшей проверки смежности вершин
      //-1 так как вершины нумеруются с нуля

    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            cout << matrix[i][j] << "(" << i << "," << j << ")" ;
        }
        cout << "\n";
    } //Поглядим на матрицу А

    for (int i=0;i<n;i++){
        Dnum[i] = 0;
        Low[i]=0;
        S[i]=-1;
    } //По алгоритму зануляе все Dnum и Low, Массив S - стек из вершин,
      //заполняем его -1, т.к. у нас вершины с нуля
    for (int x=0;x<n;x++){
        if (Dnum[x]==0) { Blocks(n, k , c, g, x, Dnum, Low, S, matrix, V);}
    }
}