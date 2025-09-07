##### Calculate Engine #####
## Calculate Engine by Napple7724 in Python on September 7, 2025
#######################################################################
## Version : Dev 1.0
## License : CC BY-NC-SA 2.0 KR
#######################################################################
## Thank you!


def allcalc(str_sign, list_int_num, bool_show_err_message) :
    int_answer = list_int_num[0]
    if str_sign == "+" :
        int_answer = sum(list_int_num)
    elif str_sign in ["-", "*", "/", "^"] :
        for sys_int_r1 in list_int_num[1::] :
            if str_sign == "-" :
                int_answer -= sys_int_r1
            elif str_sign == "*" :
                int_answer *= sys_int_r1
            elif str_sign == "/" :
                int_answer /= sys_int_r1
            else :
                int_answer **= sys_int_r1
    else :
        if bool_show_err_message == True :
            print("Calculate Engine ERROR! : The sign you entered couldn't be found.\n계산 엔진 오류! : 입력하신 부호를 찾을 수 없습니다.")
        return None
    return int_answer