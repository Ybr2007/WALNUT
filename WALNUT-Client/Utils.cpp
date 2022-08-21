#include <Windows.h>
#include <string>
#include <iostream>

using namespace std;

namespace ConsoleUtils
{
	void HideConsoleCursor()//隐藏光标
	{
		CONSOLE_CURSOR_INFO cursor_info = { 1,0 };
		SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &cursor_info);
	}

	void SetConsoleCursorPosition(int x, int y)//设置光标坐标
	{
		COORD pos = { (short int)x,(short int)y };
		SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), pos);
	}

	void SlowlyPrint(string ch, int t)//逐字输出
	{
		int l = (int)ch.size();
		for (int i = 0; i < l; i++)
		{
			cout << ch[i];
			Sleep((long unsigned int)t);
		}
	}

	void SetConsoleColor(string i) // 设置输出字符颜色
	{
		if (i == "BLUE")SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), FOREGROUND_INTENSITY | FOREGROUND_BLUE);
		else if (i == "WHITE")SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), FOREGROUND_INTENSITY | FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE);
		else if (i == "RED")SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), FOREGROUND_INTENSITY | FOREGROUND_RED);
		else if (i == "YELLOW")SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), FOREGROUND_INTENSITY | FOREGROUND_RED | FOREGROUND_GREEN);
		else if (i == "GREEN")SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), FOREGROUND_INTENSITY | FOREGROUND_GREEN);
		else if (i == "CYAN")SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), FOREGROUND_INTENSITY | FOREGROUND_GREEN | FOREGROUND_BLUE);
	}
}


namespace String
{
	bool startsWith(string str, string subStr)
	{
		if (str.length() < subStr.length())return false;
		if (str.substr(0, subStr.length()) == subStr)return true;
		return false;
	}

	LPCWSTR StringToLPCWSTR(std::string orig)
	{
		size_t origsize = orig.length() + 1;
		const size_t newsize = 100;
		size_t convertedChars = 0;
		wchar_t* wcstring = (wchar_t*)malloc(sizeof(wchar_t) * (orig.length() - 1));
		mbstowcs_s(&convertedChars, wcstring, origsize, orig.c_str(), _TRUNCATE);

		return wcstring;
	}
}

