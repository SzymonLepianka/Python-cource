int ilecyfr;
system = 2
#printf("ile cyfr ma liczba? : ");
#scanf("%d", &ilecyfr);
int tab[ilecyfr];
char tabb[ilecyfr];
int x;
int i;
for (i=0; i<ilecyfr; i++)
{
    z:
    printf("cyfra nr %d: ", i+1);
    scanf("%d", &x);
    if(x>=0 && x<system)
    {
        tab[i]=x;
    }
    else
    {
        printf("zla cyfra, podaj jeszcze raz: ");
        goto z;
    }
}

int i;
for (i=0; i<ilecyfr; i++)
{
    printf("%d", tab[i]);
}
printf(" \n");
int liczba=0;
int a=0;
int j;
for (j=ilecyfr-1; j>=0; j--, a++)
{
    if(a==0)
    {
        liczba = liczba + tab[j];
        printf("a=%d , liczba=%d, tab[j]=%d , j=%d\n", a,liczba,tab[j],j);
    }
    else
    {
        double y = pow(system,a);
        liczba = liczba + tab[j]*y;
        printf("a=%d , liczba=%d, tab[j]=%d , j=%d , pow=%.0f\n", a,liczba,tab[j],j, y);
    }
}
printf("Liczba w dziesietnym: %d", liczba);
return 0;
}