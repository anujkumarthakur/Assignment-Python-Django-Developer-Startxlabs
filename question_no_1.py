############################################   QUESTION - NO - FIRST   #######################################

def Get_Check_OutTime(customers, person):
    n = len(customers)
    sum_init = 0
    if(person is None or customers is None):
        return 0
    elif(person==1):
        for i in range(0, n):
            sum_init = sum_init + customers[i]
        print(sum_init)
    else:
        #there are multiple person to serve customers so Logic
        #step-1: customers list sorting
        #step-2: find higest number and calculate other no and comapre with higest no
        #step-3 if higest no greater then sum of another no it mean leave higest no and calculate another number
        for i in range(0, n):
            for j in range(0, n-i-1):
                if customers[j] > customers[j+1]:
                    customers[j], customers[j+1] = customers[j+1], customers[j]
        high_no = customers[-1]
        other_no = 0
        for i in range(0, n-1):
            other_no = other_no + customers[i]
        if(high_no > other_no):
            print(high_no)
        else:
            print(other_no)
    
if __name__ == "__main__":
    #indicates the amount of time to store in cus list
    customers = [] 
    #how many customers do you want
    no_of_customer = int(input("how many customers do you want: "))
    print("Enter number")
    for i in range(0,no_of_customer):
        inp = int(input())
        customers.append(inp)
    #no of person to serve customers
    person = int(input())
    Get_Check_OutTime(customers, person)
    
