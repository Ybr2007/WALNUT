#include "Socket.h"
using namespace std;

namespace SocketNameSpace
{
	void Init()
	{
		WSADATA wsadata;
		WSAStartup(MAKEWORD(2, 2), &wsadata);
	}

	void Quit()
	{
		WSACleanup();
	}

	Socket::Socket()
	{
		socket_ = socket(PF_INET, SOCK_STREAM, 0);
	}

	bool Socket::NoError()
	{
		return socket_ != SOCKET_ERROR;
	}

	bool Socket::Connect(string ip, int port)
	{
		sockaddr_in socketAddr;
		socketAddr.sin_family = PF_INET;
		socketAddr.sin_addr.S_un.S_addr = inet_addr(ip.c_str());
		socketAddr.sin_port = htons(port);
		int cRes = connect(socket_, (SOCKADDR*)&socketAddr, sizeof(SOCKADDR));
		return cRes != SOCKET_ERROR;
	}

	bool Socket::Connect(char* ip, int port)
	{
		sockaddr_in socketAddr;
		socketAddr.sin_family = PF_INET;
		socketAddr.sin_addr.S_un.S_addr = inet_addr(ip);
		socketAddr.sin_port = htons(port);
		int cRes = connect(socket_, (SOCKADDR*)&socketAddr, sizeof(SOCKADDR));
		return cRes != SOCKET_ERROR;
	}

	void Socket::Send(string msg)
	{
		char sendBuf[1024] = "";
		strcpy_s(sendBuf, msg.c_str());
		send(socket_, sendBuf, strlen(sendBuf), 0);
	}

	void Socket::Send(char* msg)
	{
		char sendBuf[1024] = "";
		strcpy_s(sendBuf, msg);
		send(socket_, sendBuf, strlen(sendBuf), 0);
	}

	pair<string, int> Socket::Recv()
	{
		char recvBuf[1024] = {};
		int returnValue = recv(socket_, recvBuf, 1024, 0);
		return make_pair(recvBuf, returnValue);
	}

	void Socket::Close()
	{
		closesocket(socket_);
	}

}