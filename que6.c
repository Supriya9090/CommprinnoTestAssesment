#include <stdio.h>
int main()
{
long long int cats,dogs,legs,t;
scanf("%lld",&t);
while(t>0)
{
scanf("%lld",&cats);
scanf("%lld",&dogs);
scanf("%lld",&legs);
if(cats<=2*dogs)
{
if((legs<=4*(cats+dogs))&&(legs>=4*dogs)&&((legs%4)==0))
printf("yes\n");
else
printf("no\n");
}
if(cats>2*dogs)
{
if((legs<=4*(cats+dogs))&&(legs>=4*(dogs+(cats-2*dogs)))&&((legs%4)==0))
printf("yes\n");
else
printf("no\n");
}
t=t-1;
}
return 0;
}