def on_budget(books, budget):

    bought_loan = {}
    bought = []
    loan = 0
    count = 0
    i = 0
    loan_books = []
    c = 0

    sorted_books = sorted(books)
    
    for i in range(0,len(sorted_books)):
               
        if budget < sorted_books[i]:
            count = 0       
            break
        
        if budget >= sorted_books[i]:
            
            budget = budget - sorted_books[i]
            
            bought = bought + [sorted_books[i]]
            
    for book in sorted_books:
        if book not in bought:
            loan_books = loan_books + [book]
         
        
        
    while c < len(loan_books):
        
        loan = loan + loan_books[c]
        
        c += 1
    if len(bought) == len(sorted_books):
        loan = 0
    else:
        loan = loan - budget
    count = len(bought)

    bought_loan["books_on_budget"] = count
    bought_loan["loan"] = loan


    return bought_loan

    

        
