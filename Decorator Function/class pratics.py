
def deco_result(result_function):
    def distinction(marks):
        for m in marks:
            if m>=75:
                print(m,"Distinction")
        else:
            result_function(marks)
    
    
    
    
@deco_result
def result(marks):
    for m in marks:
        if m >=33:
            pass
        else:
            print("Fail")
            break
    else:
        print("Pass")
marks = [50,33,44,68,95,75]
result(marks)
print()