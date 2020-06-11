def chef_icecream_serving():
    n=int(input())
    customer_money=list(map(int,input().split()))
    
    is_serving_possible=True
    chef_money=[]
    
    for i in range(len(customer_money)):
        if customer_money[i]==5:
            chef_money.append(customer_money[i])
        
        elif customer_money[i]==10 and 5 in chef_money:
            chef_money.append(10)
            chef_money.remove(5)
            
        elif customer_money[i]==15 and (10 in chef_money or chef_money.count(5)>1):
            if 10 in chef_money:
                chef_money.remove(10)
            else:
                chef_money.remove(5)
                chef_money.remove(5)
        
        else:
            is_serving_possible=False
            break
    
    if is_serving_possible==True:
        return "YES"
    else:
        return "NO"
 
def main():   
	no_of_test_case=int(input())
	for i in range(no_of_test_case):
    		result=chef_icecream_serving()
    		print(result)

if __name__=="__main__":
	main()