#include <Windows.h>

bool consoleMode = false;
int consoleModeKey = 0;

bool GetConsoleMode()
{
	return consoleMode;
}

bool DealMsg(WPARAM wParam)
{
	switch (wParam)
	{
	case 'Y':
		if (consoleModeKey == 0) consoleModeKey = 1;
		else consoleModeKey = 0;

		break;
	case 'B':
		if (consoleModeKey == 1) consoleModeKey = 2;
		else consoleModeKey = 0;

		break;
	case 'R':
		if (consoleModeKey == 2)
		{
			consoleMode = !consoleMode;
			ShowWindow(GetConsoleWindow(), consoleMode);
		}
		consoleModeKey = 0;

		break;
	default:
		break;
	}
	return true;
}