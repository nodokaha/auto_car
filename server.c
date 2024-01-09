#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <arpa/inet.h>
#include <sys/socket.h>

int s;

static void die(int signo)
{
  close(s);
  exit(EXIT_SUCCESS);
}

int main(int argc, char *argv[])
{
  struct sockaddr_in addr;
  struct sigaction *act = calloc(sizeof(act), sizeof(struct sigaction *));

  char *buf = calloc(30, sizeof(char *));
  act->sa_handler = die;

  strcpy(buf, "Hello world\n\0");

  if((s=socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) == -1) die(NULL);

  addr.sin_family = AF_INET;
  addr.sin_port = htons(atoi(argv[1]));
  addr.sin_addr.s_addr =  htonl(INADDR_ANY);

  sigaction(SIGINT, act, NULL);

  while(1)
    {
      sleep(1);
      if(sendto(s, buf, 30, 0, (struct sockaddr*)&addr, sizeof(addr)) == -1) die(NULL);
    }
  close(s);
  return 0;
}
