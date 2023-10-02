class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = (".com", ".bg", ".org", ".net")
while True:
    email = input()

    if email == "End":
        break

    if "@" in email:
        place = email.index("@")
        email_name = email[:place]
        if len(email_name) <= 4:                                                # check name len
            raise NameTooShortError("Name must be more than 4 characters")
    else:                                                                       # check if symbol "@" in email
        raise MustContainAtSymbolError("Email must contain @")

    flag = True
    for domain in valid_domains:                                                # check for valid domain
        if domain in email:
            flag = True

            dot_index = email.index(".")
            email = email.replace(domain[1:], "")       # in case we have .comm/.bgg/.orgg/.nett (line 33-40)
            try:                                        # we remove the part of the email(com/bg/org/net) after the dot
                dot_index = email[dot_index+1]          # so we have for example peter@gmail.comm -> peter@gmail.m
                flag = False                            # if we find a symbol after "." then it isn't valid and we
                break                                   # change the flag to False, break and raise the error
            except IndexError:
                pass
            break
        else:
            flag = False
    if not flag:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")