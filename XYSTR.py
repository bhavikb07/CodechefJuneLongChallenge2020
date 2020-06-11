def find_max_dance_pairs():
    s=list(input())
    pair_count=0
    
    #Calculating the dance pairs
    j=0
    while j<len(s)-1:
        if s[j]=='x':
            if s[j+1]=='y':
                pair_count+=1
                j+=1
        elif s[j]=='y':
            if s[j+1]=='x':
                pair_count+=1
                j+=1
        j+=1

    return pair_count

def main():
	no_of_test_cases=int(input())
	for i in range(no_of_test_cases):
		print(find_max_dance_pairs())	
	
if __name__=="__main__":
	main()