print("Enter the principal amount ")  
principal = float (input())
print("Enter the annual interest rate ")
annual_interest_rate = float (input())
print("Enter the duration in years ")
loan_duration = float (input())

percentage_mr = (annual_interest_rate/100)/12
number_of_months = loan_duration * 12

if annual_interest_rate == 0:
    monthly_payment  = principal / number_of_months 
else:
    numerator = percentage_mr * ((1 + percentage_mr ) ** number_of_months )
    denominator = ((1 + percentage_mr ) ** number_of_months ) - 1
    monthly_payment = principal *  (numerator /denominator)

print(f"Monthly payment is: ${monthly_payment: .2f}" )


