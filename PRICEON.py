def calculate_revenue_loss():
	n,k=map(int,input().split(" "))
    	product_prices=list(map(int,input().split(" ")))
    	
	#Storing original product price sum in this
	original_sum=sum(l)

	#In this variable,the price sum after enforcing governemnt ceiling is stored
    	ceil_sum=0
    	for price in product_prices:
        	if price<k:
            		ceil_sum+=price
        	else:
            		ceil_sum+=k 
    	
	return original_sum-ceil_sum 

def main():
	no_of_test_case=int(input())
	for i in range(no_of_test_case):
    		print(calculate_revenue_loss())

if __name__=="__main__":
	main()