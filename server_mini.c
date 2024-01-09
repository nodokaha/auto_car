#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <arpa/inet.h>
#include <sys/socket.h>

int main(int argc, char *argv[])
{
  int s;
  struct sockaddr_in addr;
  char *buf = calloc(30, sizeof(char *));
  strcpy(buf, "Hello world\n\0");

  if((s=socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) == -1);

  addr.sin_family = AF_INET;
  addr.sin_port = htons(atoi(argv[1]));
  addr.sin_addr.s_addr =  htonl(INADDR_ANY);

  while(1)
    {
      sleep(1);
      if(sendto(s, buf, 100, 0, (struct sockaddr*)&addr, sizeof(addr)) == -1);
    }
  close(s);
  return 0;
}
