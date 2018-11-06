// Подключение библиотеки для ввода/вывода данных
#include <iostream>
// Подключение стандартного пространства имен
using namespace std;

int func(int n, int m)
{
    if (n == 1)
        return 1;
    int result = 0;
    for (int x = min(n, m); x >= 2; x--)
        if (n % x == 0)
            result += func(n / x, x);
    return result;
}

// main - главная функция, запускается в начале программы
int main() {
    // 1 - название файла, 2 - режим работы ("r" - чтение, "w" - запись)
    // 3 - перевод стандартного потока ввода/вывода на файлы
    // stdin - входной поток, stdout - выходной
    freopen("factor.in", "r", stdin);
    freopen("factor.out", "w", stdout);
    // Создание (объявление) переменных типа int (целочисленные)
    int n, m;
    // Считывание переменных
    cin >> n >> m;
    // return ВСЕГДА должен быть в конце и main и возвращать 0 (это показывает, что
    // программа завершилась без ошибок)
    cout << func(n, m);
    return 0;
}
