#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <arpa/inet.h>
#include <sys/socket.h>

int s;

static void terminate(int sig){ write(STDERR_FILENO, "SIGINT!", 7); close(s); exit(0); }

void die(char *s)
{
	perror(s);
	exit(1);
}

int main(int argc, char *argv[])
{
	struct sockaddr_in si_me, si_other;
	int i, slen = sizeof(si_other), recv_len;
	char buf[100], msg[100] = "hello\n\0";


	if(signal(SIGINT, terminate) == SIG_ERR) do { exit(EXIT_FAILURE); }while(0);

	if((s=socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) == -1)
	{
		die("socket");
	}

	memset((char *) &si_me, 0, sizeof(si_me));

	si_me.sin_family = AF_INET;
	si_me.sin_port = htons(atoi(argv[1]));
	si_me.sin_addr.s_addr = htonl(INADDR_ANY);

	if( bind(s, (struct sockaddr*)&si_me, sizeof(si_me)) == -1)
	{
		die("bind");
	}

	while(1)
	{
		printf("Wait...");
		fflush(stdout);
//		if(listen(s, 3) == -1)
//		{
//			die("listen");
//		}
//		if((s=accept(s, (struct sockaddr*)&si_other, &slen)) == -1)
//		{
//			die("accept");
//		}
		if((recv_len = recvfrom(s, buf, 100, 0, (struct sockaddr *) &si_other, &slen)) == -1)
		{
			die("recvfrom()");
		}

		printf("Connected! %s:%d\n", inet_ntoa(si_other.sin_addr), ntohs(si_other.sin_port));
		buf[recv_len] = '\0';
		printf("Data: %s\n", buf);

		if(sendto(s, msg, 100, 0, (struct sockaddr*)&si_other, slen) == -1)
		{
			die("sendto()");
		}
	}
	close(s);
	return 0;
}
