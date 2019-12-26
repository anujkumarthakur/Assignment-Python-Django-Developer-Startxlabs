'''QUESTION-1   Write a function which takes two arguments: a list of customers and the number of open cash 
                registers. Each customer is represented by an integer which indicates the amount of time needed 
                to checkout. Assuming that customers are served in their original order, your function should output 
                the minimum time required to serve all customers.
        Example:
                get_checkout_time([5, 1, 3], 1) should return 9
                get_checkout_time([10, 3, 4, 2], 2) should return 10 because while the first register is busy serving 
                customer[0] the second register can serve all remaining customers.
'''

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
    
