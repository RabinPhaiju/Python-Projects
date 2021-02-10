bid_people = {}

is_other = True
while is_other:
    name = input('Enter you name')
    bid = int(input('Enter bid'))
    bid_people[name] = bid
    if(input("Is there another bid")!='yes'):
        is_other = False

final_bid =0
final_name =''
for bider in bid_people:
    if(final_bid<bid_people[bider]):
        final_bid=bid_people[bider]
        final_name = bider
print(f'The auction is won by {final_name} by {final_bid}')