import random

# This list contains the random responses (you can add your own or translate them into your own language too)
random_responses = ["흥미로운 이야기네요. 자세히 말해 주세요.",
                    "그렇군요. 더 말해 줄래요?",
                    "왜 그렇게 생각하나요?",
                    "웃긴 날씨네요, 그렇죠?",
                    "다른 주제에 대해 말해봅시다.",
                    "어젯밤의 경기는 어땠나요?"]

print("안녕하세요, 나는 로봇 마빈입니다.")
print("'그만'을 입력하면 대화를 그만둘 수 있어요.")
print("답변을 입력한 후에 '엔터'를 눌러 주세요.")
print("오늘 기분은 어떠신가요?")

while True:
    # wait for the user to enter some text
    user_input = input("> ")
    if user_input.lower() == "그만":
        # if they typed in 'bye' (or even BYE, ByE, byE etc.), break out of the loop
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("얘기해서 즐거웠어요. 안녕!")