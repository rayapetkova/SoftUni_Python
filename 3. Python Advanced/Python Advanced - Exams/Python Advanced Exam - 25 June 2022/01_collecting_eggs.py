from collections import deque

eggs = deque(int(n) for n in input().split(", "))
pieces_of_paper = [int(n) for n in input().split(", ")]
boxes = 0

while eggs and pieces_of_paper:
    egg, paper = eggs.popleft(), pieces_of_paper.pop()
    if egg <= 0:
        pieces_of_paper.append(paper)
        continue
    elif egg == 13:
        pieces_of_paper.append(paper)
        pieces_of_paper[0], pieces_of_paper[-1] = pieces_of_paper[-1], pieces_of_paper[0]
        continue
    total = egg + paper
    if total <= 50:
        boxes += 1

if boxes:
    print(f"Great! You filled {boxes} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join(str(e) for e in eggs)}")
if pieces_of_paper:
    print(f"Pieces of paper left: {', '.join(str(p) for p in pieces_of_paper)}")
