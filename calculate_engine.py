##### Calculate Engine #####
## Calculate Engine by Napple7724 in Python on September 7, 2025
#######################################################################
## Version : Dev 1.0
## License : CC BY-NC-SA 2.0 KR
#######################################################################
## Thank you!


def allcalc(sign, numbers, show_err_msg = True) :
    if type(numbers) != list :
        if show_err_msg :
            print("Calculate Engine ERROR! : 인수 \"numbers\"(은)는 list 형태로 입력되어야 합니다.")
        return None
    if type(show_err_msg) != bool :
        if show_err_msg :
            print("Calculate Engine ERROR! : 인수 \"show_err_msg\"(은)는 bool 형태로 입력되어야 합니다.")
        return None
    int_answer = numbers[0]
    if sign == "+" :
        int_answer = sum(numbers)
    elif sign in ["-", "*", "/", "^"] :
        for r1 in numbers[1::] :
            if sign == "-" :
                int_answer -= r1
            elif sign == "*" :
                int_answer *= r1
            elif sign == "/" :
                int_answer /= r1
            else :
                int_answer **= r1
    else :
        if show_err_msg :
            print(f"Calculate Engine ERROR! : 인수 \"sign\"(은)는 다음 중 하나여야 합니다 : {['+', '-', '*', '/', '^']}")

        return None
    return int_answer

def yagseu(number, show_err_msg=True) :
    if type(number) != int :
        if show_err_msg :
            print("Calculate Engine ERROR! : 인수 \"number\"(은)는 int 형태로 입력되어야 합니다.")
        return None
    if type(show_err_msg) != bool :
        if show_err_msg :
            print("Calculate Engine ERROR! : 인수 \"show_err_msg\"(은)는 bool 형태로 입력되어야 합니다.")
        return None
    list_answer = []
    for r1 in range(1, number // 2 + 1) :
        if number % r1 == 0 :
            list_answer.append(r1)
    list_answer.append(number)
    return list_answer\

def baeseu(number, limit, show_err_msg=True) :
    if type(number) != int :
        if show_err_msg :
            print("Calculate Engine ERROR! : 인수 \"number\"(은)는 int 형태로 입력되어야 합니다.")
        return None
    if type(limit) != int :
        if show_err_msg :
            print("Calculate Engine ERROR! : 인수 \"limit\"(은)는 int 형태로 입력되어야 합니다.")
        return None
    if type(show_err_msg) != bool :
        if show_err_msg :
            print("Calculate Engine ERROR! : 인수 \"show_err_msg\"(은)는 bool 형태로 입력되어야 합니다.")
        return None
    list_answer = []
    for r1 in range(1, limit + 1) :
        list_answer.append(number * r1)
    return list_answer