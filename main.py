#반환값과 입력값이 없는 함수

def greeting () :
    print("안녕하세요.")
    print("반갑습니다.")

#반환값과 입력값이 있는 함수

def greeting_2 (a,b) :
    print(a)
    print(b)
    return a+b

bye = greeting_2('안녕하세요','또 만났네요.')
print(bye)

