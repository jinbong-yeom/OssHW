#include<stdio.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<string.h>
#include<unistd.h>
#include<fcntl.h>
#define STDIN 0
void main(int argc,char *argv[]){
int i;
FILE* fp;
//int fd;
int count=1;
char arr[100];
//if(argc<2){
//fd=open(argv[1],O_RDWR);
//read(STDIN,arr,100);
//close(fd);
//}
//else {
for(i=1;i<argc;i++){
if (strcmp(argv[1], "-n") == 0){
if (i != 1) {
fp = fopen(argv[i], "r");
while(fgets(arr,100,fp)!=NULL){
printf("%d %s", count, arr);
count++;
}
fclose(fp);
}
}
else {
fp = fopen(argv[i], "r");
while(fgets(arr,100,fp)!=NULL){
printf("%s",arr);
}
fclose(fp);
}
}
//}
}
