def build_postorder(pre):
    if not pre:
        return []

    root = pre[0]
    left = []
    right = []

    for x in pre[1:]:
        if x < root:
            left.append(x)
        else:
            right.append(x)

    return build_postorder(left) + build_postorder(right) + [root]


# ===== MAIN =====
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    post = build_postorder(a)
    print(" ".join(map(str, post)))
"""
Duyệt theo pre order 
def pre_order(post):
    if not post :
    return []

    root = post[-1]
    left = []
    right = []
    
    for x in post[:-1]:
        if x < root :
            left.append(x)
        else:
            right.append(x)
    return [root] + pre_order(left)+pre_order(right)
"""
