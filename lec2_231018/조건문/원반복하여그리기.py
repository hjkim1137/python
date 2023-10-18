# 원리가 완벽하게 이해되지는 않음
import turtle as t

n = 60
t.shape('turtle')
t.speed('fastest')
for i in range(n):
    t.circle(120)
    t.right(360/n)

t.mainloop()
