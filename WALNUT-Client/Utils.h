#include <string>

using namespace std;

namespace ConsoleUtils
{
	void HideConsoleCursor();
	void SetConsoleCursorPosition(int x, int y);
	void SlowlyPrint(string msg, int dt);
	void SetConsoleColor(string colorKeyStr);
}

namespace String
{
	bool startsWith(string str, string subStr);
	LPCWSTR StringToLPCWSTR(std::string orig);
}
