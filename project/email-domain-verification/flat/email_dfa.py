def email_dfa(email):

    state = "q0"

    for char in email:

        if state == "q0":
            if char.isalnum() or char in "._%+-":
                state = "q1"
            else:
                return False

        elif state == "q1":
            if char.isalnum() or char in "._%+-":
                state = "q1"
            elif char == "@":
                state = "q2"
            else:
                return False

        elif state == "q2":
            if char.isalnum():
                state = "q3"
            else:
                return False

        elif state == "q3":
            if char.isalnum() or char == "-":
                state = "q3"
            elif char == ".":
                state = "q4"
            else:
                return False

        elif state == "q4":
            if char.isalpha():
                state = "q5"
            else:
                return False

        elif state == "q5":
            if char.isalpha():
                state = "q6"
            else:
                return False

        elif state == "q6":
            if char.isalpha():
                state = "q6"
            else:
                return False

    return state == "q6"


# Testing DFA

email = input("Enter Email Address: ")

if email_dfa(email):
    print("Accepted: Valid Email Address")
else:
    print("Rejected: Invalid Email Address")