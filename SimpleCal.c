//https://www.careercup.com/question?id=5694850432237568
#include <stdio.h>

	// your code goes here
	float multiply(float x, float y){
		return x*y;	
	}
	float add(float x, float y){
		return x+y;
	}
	float divide(float x, float y){
		if(y==0){
			printf("Invalid input");
			return 0;
		}
		else
			return x/y;
	}
	float sub(float x, float y){
		return x-y;
	}
	float min(float x, float y){
		return x>y?y:x;
	}
	float max(float x, float y){
		return x>y?x:y;
	}
	
	int main(){
		float a,b,r;
		char op;
		do{
			printf("\nnumber op number?");
			scanf("%f %c %f", &a, &op, &b);
			switch(op){
				case '+' : 
					r = add(a,b);
					break;
				case '-':
					r = sub(a,b);
					break;
				case '*':
					r = multiply(a,b);
					break;
				case '/':
					r = divide(a,b);
					break;
				case 'm':
					r = min(a,b);
					break;
				case 'M':
					r = max(a,b);
					break;
				case 'q':
					break;
				default :
					op = '?';
			}
			if(op=='?'){
				printf("Unknown operator");
			}else if(op=='q'){
				printf("Bye\n");
			}else{
				printf("%f %c %f = %f", a,op,b,r);
			}
		}while(op != 'q');
		return 0;
	}
