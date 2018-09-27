# This file is used from a problem set to teach 9th and 10th grade students 
# Thank you to Filip for contributing to this code. 
# We are pretty sure this validates to RFC5322, but who knows 
# https://tools.ietf.org/html/rfc5322

valid_domains = ["com","net","pl", "edu","eu"]

while True: 
    email = input("enter an email: ")
    print("The period is at position: ", email.rfind('.'))
    last_period = email.rfind('.')
    top_level_domain = email[(last_period+1):]
    print("The top level domain is: ", top_level_domain)
    if top_level_domain in valid_domains:
        print("ok domain")
        # lets make sure there is only one: 
        if email.count('@') > 1:
            print("invalid domain, only one @ sign allowed!")
        else:
            # now we make sure the @ sign has text before and after it. 
            if email.find('@')==0:
                print("invalid domain, @ must have text before it!")
            else:
                # we must make sure there is no difference between the position of the @ sign and period 
                at_sign = email.find('@')
                if (last_period-at_sign) == 1:
                    print("invalid domain, there must be a domain name between the @ sign and the period.")
                else:
                    print("We have a valid email :-)")    
    else:
        print("invalid domain, no valid top level domain found.")
        break    
