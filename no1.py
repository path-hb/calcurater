# 파이썬 계산기

import tkinter as tk
from tkinter import messagebox

#기본 창 생성
root = tk.Tk()
root.title("사칙연산기")  #창 제목
root.geometry("400x600") #초기 사이즈
root.minsize(300, 500)   #최소 사이즈 제한

#디스플레이 영역 생성
display = tk.Entry(root, font=("Arial", 30), borderwidth=5, relief="flat", justify='right', state="readonly")

#화면에 배치
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=20)
for i in range(4):
    root.columnconfigure(i, weight=1)

#버튼 클릭시 실행될 함수
def on_click(text):
    display.config(state="normal") #디스플레이 참금 해제
    current = display.get() #현재 디스플레이 내용 확인

    #연산기호 연속 입력 방지
    operators = ['+', '-', '×','÷']
    if text in operators:
        if current == "": #처음부터 기호를 누르면 무시
            return
        if current[-1] in operators: #마지막이 기호인데 또 기호를 누르면
            display.delete(len(current)-1, tk.END) #마지막기호 지우고 새 기호로 교체
    
    if text == "C":
        display.delete(0, tk.END) #디스플레이 초기화
    elif text == "=":
        try:
            expression = display.get().replace('×','*').replace('÷','/') #연산기호 변경
            result = eval(expression) #문자열 수식을 숫자로 계산
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception:
            messagebox.showerror("에러", "잘못된 수식입니다.")
            display.delete(0, tk.END)
    else:
        display.insert(tk.END, text)

    #디스플레이 다시 잠금
    display.config(state="readonly")

#키보드 입력
def key_input(event):
    key = event.char
    valid_keys = "0123456789+-*/" #입력가능 키 제한

    if key in valid_keys:
        #화면 표시용 기호로 변환해서 전달
        if key == "*": key = "×"
        if key == "/": key = "÷"
        on_click(key)
    elif event.keysym == "Return":  #엔터키입력 -> =
        on_click("=")
    elif event.keysym == "Escape": #ESC키 입력 -> C
        on_click("C")
    elif event.keysym == "BackSpace": #백스페이스 입력
        display.config(state="normal")
        current = display.get()
        display.delete(len(current)-1, tk.END)
        display.config(state="readonly")

#키보드 이벤트 연결
root.bind("<Key>", key_input)

#버튼 목록
buttons = [
        '7', '8', '9', '÷',
        '4', '5', '6', '×',
        '1', '2', '3', '-',
        'C', '0', '=', '+'
        ]

#버튼 배치
row_idx = 1
col_idx = 0

#반복문으로 버튼 생성과 배치
for btn_text in buttons:
    
    #숫자버튼 색 설정
    btn_bg = "#f9f9f9" 
    btn_fg = "black"

    #기호버튼 색 설정
    if btn_text == 'C':
        btn_bg = "#ff4d4d"
        btn_fg = "white"
    elif btn_text == "=":
        btn_bg = "#4caf50"
        btn_fg = "white"
    elif not btn_text.isdigit():
        btn_bg = "#87ceeb"
        btn_fg = "white"

    btn = tk.Button(root, text=btn_text, font=("Arial", 20), bg=btn_bg, fg=btn_fg, activebackground= "#cccccc", command=lambda t=btn_text: on_click(t))
    btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=5, pady=5)
    
    #열 번호 하나씩 늘림
    col_idx += 1

    #버튼을 4열까지 채우고 다음 행으로 넘어가고 열은 다시 0번으로
    if col_idx > 3:
        col_idx = 0
        row_idx += 1

    #버튼이 있는 행이 늘어나도록 가중치 설정
    for i in range(1, 5):
        root.rowconfigure(i, weight=1)



root.mainloop()
