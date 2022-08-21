#include <Windows.h>

bool RegisterGlobalHotKey()
{
	bool ret;
	ret = RegisterHotKey(NULL, 'Y', MOD_CONTROL, 'Y');
	if (!ret) return ret;
	ret = RegisterHotKey(NULL, 'B', MOD_ALT, 'B');
	if (!ret) return ret;
	ret = RegisterHotKey(NULL, 'R', MOD_ALT, 'R');
	if (!ret) return ret;
	return ret;
}

void UnRegistreGlobalHotKey()
{
	UnregisterHotKey(NULL, 'Y');
	UnregisterHotKey(NULL, 'B');
	UnregisterHotKey(NULL, 'R');
}