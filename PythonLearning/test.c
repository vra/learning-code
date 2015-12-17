/*
 * This is a simple program,when you input "Test",then this program will output "tseTTest"*/
#include<stdio.h>
#include<string.h>

void func(char *s,char *t)
{
	int i,len=strlen(s);
	for(i=0;i<len;i++) t[i]=s[len-1-i];
	for(i=0;i<len;i++) t[len+i]=s[i];
	t[8]='\0';
}
int main()
{
	char s[50],t[50];
	scanf("%s",&s);
	func(s,t);
	printf("%s",t);
	return 0;
}
