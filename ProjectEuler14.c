#include <stdio.h>

int main()
{
    unsigned long long number=1ULL,greatest=0,result,count,temp;
    for(number=1ULL;number < 1000000ULL;number++){
        count = 2ULL;
        temp = number;
        while(temp != 1){
            if(temp%2 == 0){
                temp = temp/2;
                count++;
            }
            else {
                temp = (temp*3)+ 1;
                count++;
            }
        }
        if(count > greatest){
            greatest = count;
            result = number;
        }

    }
    printf("%llu",result);
    return 0;
}
