#include<stdio.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<dirent.h>
#include<unistd.h>
void main(int argc,char *argv[]){
int i;
FILE* fp1;
FILE* fp2;
char arr[100];
char arr2[100];
struct stat buf;
DIR *dik;
getcwd(arr2,100);
lstat(argv[argc-1],&buf);
if(S_ISDIR(buf.st_mode)){
for(i=1;i<argc-1;i++){
fp1=fopen(argv[i],"r");
chdir(argv[argc-1]);
fp2=fopen(argv[i],"w");
while(fgets(arr,100,fp1)!=NULL){
fprintf(fp2,arr,100);
}
fclose(fp2);
chdir(arr2);
fclose(fp1);
}
}
else {
fp1=fopen(argv[1],"r");
fp2=fopen(argv[2],"w");
while(fgets(arr,100,fp1)!=NULL){
fprintf(fp2,arr,100);
}
fclose(fp2);
fclose(fp1);
}
}
