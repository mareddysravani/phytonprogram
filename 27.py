#include<stdio.h>
#include<string.h>
int main(void)
{
char a[10];
int s,l,count=0;
scanf("%s",a);
l=strlen(a);
for(s=0;s<l;s++)
	{
if(a[s]=='1'||a[s]=='2'||a[s]=='3'||a[s]=='4'||a[s]=='5'||a[s]=='6'||a[s]=='7'||a[s]=='8'||a[s]=='9'||a[s]=='0')
{
	count++;
   }
	if(count==0)
	printf "no";
	else
	printf "yes";
	return 0;
}
