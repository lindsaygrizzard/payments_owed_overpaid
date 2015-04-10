
melon_cost = 1.00

def find_incorrect_payment_amount(custom_file_path):
    
    payments = open(custom_file_path)

    for payment in payments:
        # Each line has "id|customer|amount melons|payment"
        # We want to split this and get customer, melons and payment

        data_line = payment.split("|")
        customer_name = data_line[1]
        melons_puchased = data_line[2]
        payment_made = data_line[3]

        correct_price = float(melons_puchased) * melon_cost

        owes = (float(correct_price) * melon_cost) - float(payment_made)
        overpaid = float(payment_made) - (float(correct_price) * melon_cost)


        if float(correct_price) < float(payment_made):
            print "%s overpaid by: %s " % (customer_name, overpaid)

        
        elif float(correct_price) > float(payment_made):
            print "%s owes: %s " % (customer_name, owes)

        elif float(correct_price) == payment_made:
            continue 

find_incorrect_payment_amount("customer-orders.txt")



