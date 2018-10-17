def find_even_digit_1000_3000(l):
    l1=[i for i in l if (i//1000%2)==0]
    l2=[i for i in l1 if (i//100%2)==0]
    l3=[i for i in l2 if (i//10%2)==0]
    l4=[i for i in l3 if i%2==0]
#     print the list in a form as required
    for q in l4:
        print(q,",", sep="", end='', flush=True)

# numbers for testing
input_numbers=list(range(1000,3001))

#run function
find_even_digit_1000_3000(input_numbers)
