# 파이썬 계산기

import tkinter as tk
from tkinter import messagebox

#기본 창 생성
root = tk.Tk()
root.title("사칙연산기")  #창 제목
root.geometry("400x600") #초기 사이즈
root.minsize(300, 500)   #최소 사이즈 제한

#디스플레이 영역 생성
display = tk.Entry(root, font=("Arial", 30), borderwidth=5, relief="flat", justify='right')

#화면에 배치
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=20)
for i in range(4):
    root.columnconfigure(i, weight=1)


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

    btn = tk.Button(root, text=btn_text, font=("Arial", 20), bg=btn_bg, fg=btn_fg, activebackground= "#cccccc")
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
