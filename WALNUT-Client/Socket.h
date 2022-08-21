#define _WINSOCK_DEPRECATED_NO_WARNINGS 
#include <stdio.h>
#include <stdlib.h>
#include<iostream>
#include<string>
#include<cstring>
#include<WS2tcpip.h>
#include <WinSock2.h>
#include<Windows.h>
#pragma comment(lib, "ws2_32.lib")  //╪сть ws2_32.dll
using namespace std;

namespace SocketNameSpace
{
	void Init();
	void Quit();

	class Socket
	{
	public:
		SOCKET socket_ = SOCKET_ERROR;

		Socket();
		bool NoError();
		bool Connect(string ip, int port);
		bool Connect(char* ip, int port);
		void Send(string msg);
		void Send(char* msg);
		pair<string, int> Recv();
		void Close();
	};
}