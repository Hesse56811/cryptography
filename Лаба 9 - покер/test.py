"""

#include <iostream>

using namespace std;

bool prime(long int a) // проверка на простоту
{
	if (a <= 1)
		return false;
	for (int i = 2; i * i <= a; i++)
	{
		if (a % i == 0) {
			return false;
		}
	}
	return true;
}



long long int POW(long long int a, long long int x, long long int p) // функция быстрого возведения в степень по модулю
{
	long long int r = 1;
	while (x != 0)
	{
		if (x % 2 == 0)
		{
			a = (a * a) % p;
			x = x / 2;
		}
		else
		{
			x--;
			r = (r * a) % p;
		}
	}
	return r;
}


long long int gen_evklid(long long int a, long long int b) // функция выполняющая обобщенный алгоритм Эвклида (возвращает значение y)
{
	int temp;
	if (a < b)
	{
		temp = a;
		a = b;
		b = temp;
	}
	long long int c, NOD;
	long long int x1 = 1, y1 = 0, x2 = 0, y2 = 1;
	long long int x, y, xr, yr;
	while (b > 0)
	{
		c = a / b;
		NOD = a - b * c;
		if (NOD != 0)
		{
			xr = x1 - c * x2;
			yr = y1 - c * y2;
			x1 = x2;
			y1 = y2;
			x2 = xr;
			y2 = yr;
			a = b;
			b = NOD;
		}
		else
		{
			NOD = b;
			break;
		}
	}
	return yr;
}


int main()
{
	setlocale(LC_ALL, "Russian");
	int a, b, Cb, p, v, Ca, Da, Db, u1, u2, u3, u4, u5, x, x1, z;
	bool flag;



	cout << "Введите p : ";
	cin >> p;
	flag = prime(p);
	if (flag == false)
	{
		cout << "\n ОШИБКА (Было введено не простое число и не выполняет условия ввода)\n" << endl;
		return 0;
	}



	cout << "Введите a (тройка) : ";
	cin >> a;
	if (a < 0)
	{
		cout << "\n ОШИБКА \n" << endl;
		return 0;
	}



	cout << "Введите b (семерка) : ";
	cin >> b;
	if (b < 0)
	{
		cout << "\n ОШИБКА (повторите ввод)\n" << endl;
		return 0;
	}





	cout << "Введите y (туз) : ";
	cin >> v;
	if (v < 0)
	{
		cout << "\n ОШИБКА (повторите ввод)\n" << endl;
		return 0;
	}
	cout << "\n";




	cout << "Выбор Алисы Са: ";
	cin >> Ca;

	cout << "Выбор Боба Сb: ";
	cin >> Cb;
	cout << "\n";




	cout << "Находим по ОАЕ Da и Db" << endl;
	Da = gen_evklid(Ca, (p - 1));
	if (Da < 0)
	{
		Da = Da + (p - 1);
		cout << "Da = " << Da << endl;
	}
	else
	{
		cout << "Da = " << Da << endl;
	}

	Db = gen_evklid(Cb, (p - 1));
	if (Db < 0)
	{
		Db = Db + (p - 1);
		cout << "Db = " << Db << "\n" << endl;

	}
	else
	{
		cout << "Db = " << Db << endl;
		cout << "\n";
	}





	cout << "Алиса вычисляет u1,u2,u3" << endl;
	u1 = POW(a, Ca, p);
	cout << "u1 = " << u1 << endl;

	u2 = POW(b, Ca, p);
	cout << "u2 = " << u2 << endl;

	u3 = POW(v, Ca, p);
	cout << "u3 = " << u3 << "\n" << endl;





	cout << "Алиса перемешала u1,u2,u3 и теперь Боб должен выбрать одно из полученных чисел: ";
	cin >> x;
	if (x == u1)
	{
		u4 = POW(u2, Cb, p);
		cout << "u4 = " << u4 << endl;
		u5 = POW(u3, Cb, p);
		cout << "u5 = " << u5 << "\n" << endl;
		cout << "Карта Алисы при раздаче - тройка " <<  "\n" << endl;
	}
	else if (x == u2)
	{
		u4 = POW(u1, Cb, p);
		cout << "u4 = " << u4 << endl;
		u5 = POW(u3, Cb, p);
		cout << "u5 = " << u5 << "\n" << endl;
		cout << "Карта Алисы при раздаче - семерка " <<  "\n" << endl;
	}
	else if (x == u3)
	{
		u4 = POW(u1, Cb, p);
		cout << "u4 = " << u4 << endl;
		u5 = POW(u2, Cb, p);
		cout << "u5 = " << u5 << "\n" << endl;
		cout << "Карта Алисы при раздаче - туз " << "\n" << endl;
	}
	else
	{
		cout << "ОШИБКА";
		return 0;
	}





	cout << "Алиса должна выбрать одно из полученных чисел Боба: ";
	cin >> x1;
	if (x1 == u4)
	{
		x1 = POW(u4, Da, p);
		cout << "x1 = " << x1 << "\n" << endl;
	}
	else if (x1 == u5)
	{
		x1 = POW(u5, Da, p);
		cout << "x1 = " << x1 << "\n" << endl;
	}
	else
	{
		cout << "ОШИБКА";
		return 0;
	}


	z = POW(x1, Db, p);
	cout << "z = " << z << endl;
	if ((z == a) && (x == u3))
	{
		cout << "Карта Боба - тройка" <<  "\n" << endl;
		cout << "Карта в прикупе - семерка" << "\n" << endl;
	}
	if ((z == a) && (x == u2))
	{
		cout << "Карта Боба - тройка" << "\n" << endl;
		cout << "Карта в прикупе - туз" << "\n" << endl;
	}
	if ((z == b) && (x == u1))
	{
		cout << "Карта Боба - семерка" << "\n" << endl;
		cout << "Карта в прикупе - туз" << "\n" << endl;
	}
	if ((z == b) && (x == u3))
	{
		cout << "Карта Боба - семерка" << "\n" << endl;
		cout << "Карта в прикупе - тройка" << "\n" << endl;
	}
	if ((z == v) && (x == u1))
	{
		cout << "Карта Боба - туз" << "\n" << endl;
		cout << "Карта в прикупе - семерка" << "\n" << endl;
	}
	if ((z == v) && (x == u2))
	{
		cout << "Карта Боба - туз" << "\n" << endl;
		cout << "Карта в прикупе - тройка" << "\n" << endl;
	}
	return 0;
}

"""