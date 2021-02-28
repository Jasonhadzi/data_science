import noshmishmosh
import numpy as np

#In order to get our baseline, we need to first know how many users visit the site in a typical week.

all_visitors = noshmishmosh.customer_visits
total_visitor_count = len(all_visitors)
paying_visitors = noshmishmosh.purchasing_customers
paying_visitor_count = len(paying_visitors)

baseline_percent = (paying_visitor_count/total_visitor_count) *100
print(baseline_percent)


payment_history = noshmishmosh.money_spent

#We need to find how many purchases it would take to reach $1240 in additional revenue using our historical data.
average_payment =np.mean(payment_history)
print(average_payment)
#We want to know how many of these “usual” payments it would take to clear our $1240 mark.
new_customers_needed =np.ceil(1240/average_payment)
print(new_customers_needed)

# find the additional percent of weekly visitors who must make a purchase in order to make this change worthwhile
percentage_point_increase = new_customers_needed/total_visitor_count *100

print(percentage_point_increase)

mde = percentage_point_increase/baseline_percent *100
print(mde)

ab_sample_size = 490
